#!/usr/bin/env python
# coding: utf-8

# 版本
from core.Utils import EDITION
# 包导入
import sys

if __name__ == '__main__':
    import argparse
    # 参数处理
    ap = argparse.ArgumentParser(description="Generating your TRPG replay video from logfile.")
    ap.add_argument("-l", "--LogFile", help='The standerd input of this programme, which is mainly composed of TRPG log.',type=str)
    ap.add_argument("-d", "--MediaObjDefine", help='Definition of the media elements, using real python code.',type=str)
    ap.add_argument("-t", "--CharacterTable", help='The correspondence between character and media elements, using tab separated text file or Excel table.',type=str)
    ap.add_argument("-o", "--OutputPath", help='Choose the destination directory to save the project timeline and breakpoint file.',type=str,default=None)
    ap.add_argument("-i", "--TimeLine", help='Timeline (and break_point with same name), which was generated by replay_generator.',type=str)
    # 选项
    ap.add_argument("-F", "--FramePerSecond", help='Set the FPS of display, default is 30 fps, larger than this may cause lag.',type=int,default=30)
    ap.add_argument("-W", "--Width", help='Set the resolution of display, default is 1920, larger than this may cause lag.',type=int,default=1920)
    ap.add_argument("-H", "--Height", help='Set the resolution of display, default is 1080, larger than this may cause lag.',type=int,default=1080)
    ap.add_argument("-Z", "--Zorder", help='Set the display order of layers, not recommended to change the values unless necessary!',type=str,
                    default='BG2,BG1,Am3,Am2,Am1,AmS,Bb,BbS')
    # 用于语音合成的key
    ap.add_argument("-K", "--AccessKey", help='Your AccessKey, to use with --SynthsisAnyway',type=str,default="Your_AccessKey")
    ap.add_argument("-S", "--AccessKeySecret", help='Your AccessKeySecret, to use with --SynthsisAnyway',type=str,default="Your_AccessKey_Secret")
    ap.add_argument("-A", "--Appkey", help='Your Appkey, to use with --SynthsisAnyway',type=str,default="Your_Appkey")
    ap.add_argument("-U", "--Azurekey", help='Your Azure TTS key.',type=str,default="Your_Azurekey")
    ap.add_argument("-R", "--ServRegion", help='Service region of Azure.', type=str, default="eastasia")
    # 用于导出视频的质量值
    ap.add_argument("-Q", "--Quality", help='Choose the quality (ffmpeg crf) of output video, to use with --ExportVideo.',type=int,default=24)
    # Flags
    ap.add_argument('--ExportXML',help='Export a xml file to load in Premiere Pro, some .png file will be created at same time.',action='store_true')
    ap.add_argument('--ExportVideo',help='Export MP4 video file, this will disables interface display',action='store_true')
    ap.add_argument('--SynthesisAnyway',help='Execute speech_synthezier first, and process all unprocessed asterisk time label.',action='store_true')
    ap.add_argument('--FixScreenZoom',help='Windows system only, use this flag to fix incorrect windows zoom.',action='store_true')
    # 语音合成预览flag
    ap.add_argument('--PreviewOnly',help='Ignore the input files, and open a speech preview gui windows.',action='store_true')
    ap.add_argument('--Init',help='The initial speech service in preview.',type=str,default='Aliyun')
    # 语言
    ap.add_argument("--Language",help='Choose the language of running log',default='en',type=str)
    ap.add_argument('--Modules',help='Choose subprogram. Choice: replay_generator, speech_synthesizer, export_xml, export_video.',type=str,default='replay_generator')
    # 版本
    ap.add_argument('-v','--version',action='version',version=EDITION,help='Display version')
    args = ap.parse_args()
    # 主程序
    if args.Modules == 'replay_generator':
        from replay_generator import ReplayGenerator
        ReplayGenerator(args=args)
    # 语音合成模块
    elif args.Modules == 'speech_synthesizer':
        from speech_synthesizer import SpeechSynthesizer,SpeechStudio
        if args.PreviewOnly == True:
            SpeechStudio(args=args)
        else:
            SpeechSynthesizer(args=args)
    # 导出PR项目模块 
    elif args.Modules == 'export_xml':
        from export_xml import ExportXML
        ExportXML(args=args)
    # 导出视频模块
    elif args.Modules == 'export_video':
        from export_video import ExportVideo
        ExportVideo(args=args)
    else:
        sys.exit(-1)
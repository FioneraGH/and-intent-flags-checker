#!/usr/bin/python3
#coding=utf-8
'''
@author fionera
@date 2021/7/18
'''

FLAG_GRANT_READ_URI_PERMISSION = 0x00000001
FLAG_GRANT_WRITE_URI_PERMISSION = 0x00000002
FLAG_FROM_BACKGROUND = 0x00000004
FLAG_DEBUG_LOG_RESOLUTION = 0x00000008
FLAG_EXCLUDE_STOPPED_PACKAGES = 0x00000010
FLAG_INCLUDE_STOPPED_PACKAGES = 0x00000020
FLAG_GRANT_PERSISTABLE_URI_PERMISSION = 0x00000040
FLAG_GRANT_PREFIX_URI_PERMISSION = 0x00000080
FLAG_IGNORE_EPHEMERAL = 0x00000200
FLAG_ACTIVITY_NO_HISTORY = 0x40000000
FLAG_ACTIVITY_SINGLE_TOP = 0x20000000
FLAG_ACTIVITY_NEW_TASK = 0x10000000
FLAG_ACTIVITY_MULTIPLE_TASK = 0x08000000
FLAG_ACTIVITY_CLEAR_TOP = 0x04000000
FLAG_ACTIVITY_FORWARD_RESULT = 0x02000000
FLAG_ACTIVITY_PREVIOUS_IS_TOP = 0x01000000
FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS = 0x00800000
FLAG_ACTIVITY_BROUGHT_TO_FRONT = 0x00400000
FLAG_ACTIVITY_RESET_TASK_IF_NEEDED = 0x00200000
FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY = 0x00100000
FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET = 0x00080000
FLAG_ACTIVITY_NEW_DOCUMENT = FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET
FLAG_ACTIVITY_NO_USER_ACTION = 0x00040000
FLAG_ACTIVITY_REORDER_TO_FRONT = 0X00020000
FLAG_ACTIVITY_NO_ANIMATION = 0X00010000
FLAG_ACTIVITY_CLEAR_TASK = 0X00008000
FLAG_ACTIVITY_TASK_ON_HOME = 0X00004000
FLAG_ACTIVITY_RETAIN_IN_RECENTS = 0x00002000
FLAG_ACTIVITY_LAUNCH_ADJACENT = 0x00001000
FLAG_ACTIVITY_MATCH_EXTERNAL = 0x00000800
FLAG_ACTIVITY_REQUIRE_NON_BROWSER = 0x00000400
FLAG_ACTIVITY_REQUIRE_DEFAULT = 0x00000200
FLAG_RECEIVER_REGISTERED_ONLY = 0x40000000
FLAG_RECEIVER_REPLACE_PENDING = 0x20000000
FLAG_RECEIVER_FOREGROUND = 0x10000000
FLAG_RECEIVER_OFFLOAD = 0x80000000
FLAG_RECEIVER_NO_ABORT = 0x08000000
FLAG_RECEIVER_REGISTERED_ONLY_BEFORE_BOOT = 0x04000000
FLAG_RECEIVER_BOOT_UPGRADE = 0x02000000
FLAG_RECEIVER_INCLUDE_BACKGROUND = 0x01000000
FLAG_RECEIVER_EXCLUDE_BACKGROUND = 0x00800000
FLAG_RECEIVER_FROM_SHELL = 0x00400000
FLAG_RECEIVER_VISIBLE_TO_INSTANT_APPS = 0x00200000

import sys as _system

sys_args_length = len(_system.argv)
if (sys_args_length < 2):
    print('Please Input Flags Code')
    exit(0)
else:
    print('Parsing Intent Flags: ' + _system.argv[1])

intent_flags = int(_system.argv[1])

if (intent_flags & FLAG_GRANT_READ_URI_PERMISSION != 0):
    print('FLAG_GRANT_READ_URI_PERMISSION')

if (intent_flags & FLAG_GRANT_WRITE_URI_PERMISSION != 0):
    print('FLAG_GRANT_WRITE_URI_PERMISSION')

if (intent_flags & FLAG_FROM_BACKGROUND != 0):
    print('FLAG_FROM_BACKGROUND')

if (intent_flags & FLAG_DEBUG_LOG_RESOLUTION != 0):
    print('FLAG_DEBUG_LOG_RESOLUTION')

if (intent_flags & FLAG_EXCLUDE_STOPPED_PACKAGES != 0):
    print('FLAG_EXCLUDE_STOPPED_PACKAGES')

if (intent_flags & FLAG_INCLUDE_STOPPED_PACKAGES != 0):
    print('FLAG_INCLUDE_STOPPED_PACKAGES')

if (intent_flags & FLAG_GRANT_PERSISTABLE_URI_PERMISSION != 0):
    print('FLAG_GRANT_PERSISTABLE_URI_PERMISSION')

if (intent_flags & FLAG_GRANT_PREFIX_URI_PERMISSION != 0):
    print('FLAG_GRANT_PREFIX_URI_PERMISSION')

if (intent_flags & FLAG_IGNORE_EPHEMERAL != 0):
    print('FLAG_IGNORE_EPHEMERAL')

if (intent_flags & FLAG_ACTIVITY_NO_HISTORY != 0):
    print('FLAG_ACTIVITY_NO_HISTORY')

if (intent_flags & FLAG_ACTIVITY_SINGLE_TOP != 0):
    print('FLAG_ACTIVITY_SINGLE_TOP')

if (intent_flags & FLAG_ACTIVITY_NEW_TASK != 0):
    print('FLAG_ACTIVITY_NEW_TASK')

if (intent_flags & FLAG_ACTIVITY_MULTIPLE_TASK != 0):
    print('FLAG_ACTIVITY_MULTIPLE_TASK')

if (intent_flags & FLAG_ACTIVITY_CLEAR_TOP != 0):
    print('FLAG_ACTIVITY_CLEAR_TOP')

if (intent_flags & FLAG_ACTIVITY_FORWARD_RESULT != 0):
    print('FLAG_ACTIVITY_FORWARD_RESULT')

if (intent_flags & FLAG_ACTIVITY_PREVIOUS_IS_TOP != 0):
    print('FLAG_ACTIVITY_PREVIOUS_IS_TOP')

if (intent_flags & FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS != 0):
    print('FLAG_ACTIVITY_EXCLUDE_FROM_RECENTS')

if (intent_flags & FLAG_ACTIVITY_BROUGHT_TO_FRONT != 0):
    print('FLAG_ACTIVITY_BROUGHT_TO_FRONT')

if (intent_flags & FLAG_ACTIVITY_RESET_TASK_IF_NEEDED != 0):
    print('FLAG_ACTIVITY_RESET_TASK_IF_NEEDED')

if (intent_flags & FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY != 0):
    print('FLAG_ACTIVITY_LAUNCHED_FROM_HISTORY')

if (intent_flags & FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET != 0):
    print('FLAG_ACTIVITY_CLEAR_WHEN_TASK_RESET')

if (intent_flags & FLAG_ACTIVITY_NEW_DOCUMENT != 0):
    print('FLAG_ACTIVITY_NEW_DOCUMENT')

if (intent_flags & FLAG_ACTIVITY_NO_USER_ACTION != 0):
    print('FLAG_ACTIVITY_NO_USER_ACTION')

if (intent_flags & FLAG_ACTIVITY_REORDER_TO_FRONT != 0):
    print('FLAG_ACTIVITY_REORDER_TO_FRONT')

if (intent_flags & FLAG_ACTIVITY_NO_ANIMATION != 0):
    print('FLAG_ACTIVITY_NO_ANIMATION')

if (intent_flags & FLAG_ACTIVITY_CLEAR_TASK != 0):
    print('FLAG_ACTIVITY_CLEAR_TASK')

if (intent_flags & FLAG_ACTIVITY_TASK_ON_HOME != 0):
    print('FLAG_ACTIVITY_TASK_ON_HOME')

if (intent_flags & FLAG_ACTIVITY_RETAIN_IN_RECENTS != 0):
    print('FLAG_ACTIVITY_RETAIN_IN_RECENTS')

if (intent_flags & FLAG_ACTIVITY_LAUNCH_ADJACENT != 0):
    print('FLAG_ACTIVITY_LAUNCH_ADJACENT')

if (intent_flags & FLAG_ACTIVITY_MATCH_EXTERNAL != 0):
    print('FLAG_ACTIVITY_MATCH_EXTERNAL')

if (intent_flags & FLAG_ACTIVITY_REQUIRE_NON_BROWSER != 0):
    print('FLAG_ACTIVITY_REQUIRE_NON_BROWSER')

if (intent_flags & FLAG_ACTIVITY_REQUIRE_DEFAULT != 0):
    print('FLAG_ACTIVITY_REQUIRE_DEFAULT')

if (intent_flags & FLAG_RECEIVER_REGISTERED_ONLY != 0):
    print('FLAG_RECEIVER_REGISTERED_ONLY')

if (intent_flags & FLAG_RECEIVER_REPLACE_PENDING != 0):
    print('FLAG_RECEIVER_REPLACE_PENDING')

if (intent_flags & FLAG_RECEIVER_FOREGROUND != 0):
    print('FLAG_RECEIVER_FOREGROUND')

if (intent_flags & FLAG_RECEIVER_OFFLOAD != 0):
    print('FLAG_RECEIVER_OFFLOAD')

if (intent_flags & FLAG_RECEIVER_NO_ABORT != 0):
    print('FLAG_RECEIVER_NO_ABORT')

if (intent_flags & FLAG_RECEIVER_REGISTERED_ONLY_BEFORE_BOOT != 0):
    print('FLAG_RECEIVER_REGISTERED_ONLY_BEFORE_BOOT')

if (intent_flags & FLAG_RECEIVER_BOOT_UPGRADE != 0):
    print('FLAG_RECEIVER_BOOT_UPGRADE')

if (intent_flags & FLAG_RECEIVER_INCLUDE_BACKGROUND != 0):
    print('FLAG_RECEIVER_INCLUDE_BACKGROUND')

if (intent_flags & FLAG_RECEIVER_EXCLUDE_BACKGROUND != 0):
    print('FLAG_RECEIVER_EXCLUDE_BACKGROUND')

if (intent_flags & FLAG_RECEIVER_FROM_SHELL != 0):
    print('FLAG_RECEIVER_FROM_SHELL')

if (intent_flags & FLAG_RECEIVER_VISIBLE_TO_INSTANT_APPS != 0):
    print('FLAG_RECEIVER_VISIBLE_TO_INSTANT_APPS')


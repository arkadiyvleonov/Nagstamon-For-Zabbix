# -*- mode: python -*-
a = Analysis(['..\\\\Nagstamon\\\\nagstamon.py'],
             pathex=['c:\\NAGSTAMON_SRC\\Nagstamon-patch-1\\build'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='nagstamon.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False , icon='..\\Nagstamon\\resources\\nagstamon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='nagstamon')

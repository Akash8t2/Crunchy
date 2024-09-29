Traceback (most recent call last):
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 31, in <module>
    start(fakepyfile,mainpyfile)
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 30, in start
    exec(open(mainpyfile).read(),  __main__.__dict__)
  File "<string>", line 272, in <module>
  File "/data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.9/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "/data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.9/asyncio/base_events.py", line 642, in run_until_complete
    return future.result()
  File "<string>", line 261, in main
  File "/data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.9/site-packages/telegram/ext/_application.py", line 627, in start
    self._check_initialized()
  File "/data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.9/site-packages/telegram/ext/_application.py", line 480, in _check_initialized
    raise RuntimeError(
RuntimeError: This Application was not initialized via `Application.initialize`!

[Program finished]
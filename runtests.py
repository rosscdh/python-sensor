import sys
import nose
from distutils.version import LooseVersion

command_line = [__file__, '--verbose']

if (LooseVersion(sys.version) < LooseVersion('3.5.3')):
    command_line.extend(['-e', 'asynqp', '-e', 'aiohttp'])

if (LooseVersion(sys.version) >= LooseVersion('3.7.0')):
    command_line.extend(['-e', 'sudsjurko'])

print("Nose arguments: %s" % command_line)
result = nose.main(argv=command_line)

exit(result)

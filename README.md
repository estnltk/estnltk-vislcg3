export LDFLAGS='-licuuc -licuio -licui18n'
python3 setup.py build
python3 setup.py install

from estnltk_vislcg3 import vislcg3

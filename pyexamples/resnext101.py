import sys

sys.path.append('../')
from pycore.blocks import *

arch = [
    to_head('..'),
    to_cor(),
    to_begin(),

    # input

    to_input('../examples/fcn8s/cats.jpg'),

    to_Conv(
        name='conv1', s_filer="{32x3}", n_filer=224,
        width=4, height=40, depth=45,
        offset="(1, 0, 0)"
    ),

    to_Conv(name='batch_norm', s_filer="{32x64}", n_filer=112,
            width=8, height=40, depth=45,
            offset="(2, 0, 0)"
            ),

    to_Conv(name='relu', s_filer="{32x64}", n_filer=112,
            width=4, height=40, depth=45,
            offset="(3, 0, 0)"
            ),

    to_Pool(name='maxpooling',
            width=4, height=40, depth=45,
            offset="(4, 0, 0)"
            ),

    # ResNext block
    to_Conv(name='conv1x1', s_filer="{32x64}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(20, 0, 0)"
            ),

    to_Conv(name='batch_norm2', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(22, 0, 0)"
            ),

    to_Conv(name='relu2', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(24, 0, 0)"
            ),

    to_Conv(name='conv3x3', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(26, 0, 0)"
            ),

    to_Conv(name='batch_norm3', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(28, 0, 0)"
            ),

    to_Conv(name='relu3', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(30, 0, 0)"
            ),

    to_Conv(name='conv1x1_2', s_filer="{32x256}", n_filer=56,
            width=3, height=20, depth=25,
            offset="(32, 0, 0)"
            ),

    to_Conv(name='batch_norm4', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(34, 0, 0)"
            ),

    to_Conv(name='add', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(36, 0, 0)"
            ),

    to_Conv(name='add2', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(38, 0, 0)"
            ),

    to_Conv(name='relu4', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(42, 0, 0)"
            ),

    to_Conv(name='glavgpooling', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(45, 0, 0)"
            ),

    to_Conv(name='flatten', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(48, 0, 0)"
            ),

    to_Conv(name='fc', s_filer="{32x256}", n_filer=56,
            width=4, height=20, depth=25,
            offset="(51, 0, 0)"
            ),

    to_connection("maxpooling", "conv1x1"),
    to_connection("conv1x1", "batch_norm2"),
    to_connection("batch_norm2", "relu2"),
    to_connection("relu2", "conv3x3"),
    to_connection("conv3x3", "relu3"),
    to_connection("relu3", "conv1x1_2"),
    to_connection("conv1x1_2", "batch_norm4"),
    to_connection("batch_norm4", "add"),
    to_connection("add", "add2"),
    to_connection("add2", "relu4"),
    to_connection("relu4", "glavgpooling"),
    to_connection("glavgpooling", "flatten"),
    to_connection("flatten", "fc"),
    to_connection("add2", "conv1x1"),


    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()

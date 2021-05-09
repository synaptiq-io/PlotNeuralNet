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
        name='conv1', s_filer=93, n_filer=3,
        width=3, height=40, depth=45,
        offset="(1, 0, 0)"
    ),
    
    
    to_Conv(name='conv2_1', s_filer=93, n_filer=9,
            width=9, height=40, depth=45,
            offset="(10, 10, 0)"
            ),
    to_Conv(name='conv2_2', s_filer=93, n_filer=3,
            width=3, height=40, depth=45,
            offset="(10, -10, 0)"
            ),
    
    
    to_Conv(name='conv3', s_filer=93, n_filer="3, 3",
            width="{4, 4}", height=40, depth=45,
            offset="(15, 0, 0)"
            ),


    to_Conv(name='conv4', s_filer=93, n_filer="3, 3",
            width="{4, 4}", height=40, depth=45,
            offset="(25, 0, 0)"
            ),

    to_Conv(name='conv5', s_filer=93, n_filer="3, 3",
            width="{2, 2}", height=40, depth=45,
            offset="(30, 0, 0)"
            ),


    to_Conv(name='conv6', s_filer=93, n_filer="3, 3",
            width="{2, 2}", height=40, depth=45,
            offset="(35, 0, 0)"
            ),


    to_Conv(name='conv7', s_filer=93, n_filer="3, 3",
            width="{2, 2}", height=40, depth=45,
            offset="(40, 0, 0)"
            ),
    

    to_Conv(name='conv8', s_filer=93, n_filer="3, 3",
            width="{2, 2}", height=40, depth=45,
            offset="(45, 0, 0)"
            ),
    

    to_Conv(name='conv9', s_filer=93, n_filer="3, 3",
            width="{2, 2}", height=40, depth=45,
            offset="(50, 0, 0)"
            ),
    

    to_Conv(name='conv10', s_filer=93, n_filer=3,
            width=3, height=40, depth=45,
            offset="(55, 0, 0)"
            ),

    to_connection("conv1", "conv2_1"),
    to_connection("conv1", "conv2_2"),
    to_connection("conv2_1", "conv3"),
    to_connection("conv2_2", "conv3"),
    to_connection("conv3", "conv4"),
    to_connection("conv4", "conv5"),
    to_connection("conv5", "conv6"),
    to_connection("conv6", "conv7"),
    to_connection("conv7", "conv8"),
    to_connection("conv8", "conv9"),
    to_connection("conv9", "conv10"),


    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()

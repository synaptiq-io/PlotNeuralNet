
import sys
sys.path.append('../')
from pycore.tikzeng import *
from pycore.blocks import *
# defined your arch
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),

    #input

    to_input( 'cats.jpg' ),

    #ResBlock
    to_ConvRes( name='ccr_b1', s_filer=256, n_filer=(24,24), offset="(10,-5,0)", to="(0,0,0)", width=(6,6), height=40, depth=40  ),
    #*block_2ConvPool( name='ccr_b1', botton='input', top='pool_b1', s_filer=64,  n_filer=512, offset="(1,0,0)", size=(16,16,5.5), opacity=0.5 ),
    to_connection( "input", "ccr_b1"),
    to_ConvRes( name='ccr_b2', s_filer=256, n_filer=(8,8), offset="(10,5,0)", to="(0,0,0)", width=(2,2), height=40, depth=40  ),
    #*block_2ConvPool( name='ccr_b2', botton='pool_b1', top='pool_b2', s_filer=64,  n_filer=512, offset="(1,0,0)", size=(16,16,5.5), opacity=0.5 ),
    to_connection( "input", "ccr_b2"),
    #to_Sum("sum1", offset="(1.5,0,0)", to="(ccr_b1-ccr_b2)", radius=2.5, opacity=0.6),
    #to_Conv( name='ccr_b3', s_filer=256, n_filer=(8,8), offset="(15,0,0)", to="(0,0,0)", width=(8,8), height=40, depth=40  ),
    #to_connection( "ccr_b1", "ccr_b3"),
    #to_connection( "ccr_b2", "ccr_b3"),

    #to_ConvRes("conv1", 512, 8, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    #to_Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    #to_ConvRes("conv2", 128, 16, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    #to_connection( "pool1", "conv2"), 
    #to_Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    #to_SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    #to_connection("pool2", "soft1"),    
    #to_Sum("sum1", offset="(1.5,0,0)", to="(soft1-east)", radius=2.5, opacity=0.6),
    #to_connection("soft1", "sum1"),
    to_end()
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()

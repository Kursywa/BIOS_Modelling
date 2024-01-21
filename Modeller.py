from modeller import *
from modeller.automodel import *

def main():
    env = Environ()
    a = AutoModel(env, alnfile = './Preprocessing_Data/MSA_Alignment.pir',
    knowns = ('3j4q', '6f14', '1CTP'), sequence = 'UN_SEQ')
    a.starting_model = 1
    a.ending_model = 5
    a.make()
    a.write('Final_Model', format ='PDB')

# 6yz5, 1CTP,
if __name__ == '__main__':
    main()
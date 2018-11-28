#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>

#include <string>
#include <math.h>

using namespace std;

int main()
{

    ifstream fin("C-small-1-attempt1.in");
    ofstream fout("C-small.out");

    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;

    int case_number,N_number,K_number,key_number,split_number,key_max;
    fin >> case_number;

    for (int i = 0; i < case_number; i++)
    {
        fin >> N_number >> K_number;

        int array1[K_number+1],array2[K_number+1];

        array1[0]=N_number;
        array2[0]=N_number;

        key_number=0;
        split_number=1;

        for (int j=0; j<K_number-1; j++)
        {
            array2[key_number]=floor( (array1[key_number]-1) /2 );
            array2[key_number+1]=array1[key_number]-1-array2[key_number];
            split_number++;

            for(int k=0; k<(split_number-key_number-2); k++)
            {
                array2[key_number+2+k]=array1[key_number+1+k];
            }

            for(int k=0; k<split_number; k++)
            {
                array1[k]=array2[k];
            }

            key_number=key_max=0;

            for(int k=0; k<split_number; k++)
            {
                if(array1[k]>key_max)
                {
                    key_max=array1[k];
                }            
            }

            for(int k=0; k<split_number; k++)
            {
                if(array1[k]==key_max)
                {
                    key_number=k;
                    break;
                }            
            }
            
        }
        
        int min=floor( (array1[key_number]-1) /2);
        int max=array1[key_number]-1-min;
        
        fout << "Case #" << (i + 1) << ": " << max << " " << min << endl;

     }

}

#include <iostream>
#include <fstream>
#include <string>
#include <stdio.h>      /* printf */
#include <stdlib.h>
#include <iomanip>
#include <locale>
#include <sstream>
#include <typeinfo>
#include<conio.h>

using namespace std;

int main()
{

    string line;
    ifstream myfile;
    ofstream out;
    out.open("output.txt");
    myfile.open("input.txt");
    int i=0;
    while ( getline (myfile,line) )
    {
        if(i==0)
        {
            int T;
            if ( ! (istringstream(line) >> T) ) T = 0;

        }
        else
        {

            int L=line.length();

            int num[L];

            for(int j=0; j<L; j++)
            {

                char c=line.at(j);
                num[j]=c-48;

            }
            for (int j=L-1; j>=0; j--)
            {
                int a=num[j];
                if(j!=0)
                {
                    for(int k=(j-1); k>=0; k--)
                    {

                        if(a<num[k])
                        {
                            for(int l=k+1; l<L; l++)
                            {
                                num[l]=9;
                            }

                            int j2=k+1;
                            int neg=1;
                            while(neg!=0)
                            {

                                j2=j2-1;
                                //cout<<"k= "<<k<<"  j2="<<j2<<"  num[j2]="<<num[j2]<<endl;

                                num[j2]=num[j2]-1;
                                if(num[j2]>=0)
                                {
                                    neg=0;
                                }
                                if(num[j2]<0)
                                {
                                    num[j2]=9;
                                }
                            }

                             break;
                        }



                    }

                }

            }
        out<<"Case #"<<i<<": ";
        int newL=L;
        for(int m=0; m<L; m++){
            if(num[m]!=0){break;}
            if(num[m]==0){
                for(int m2=0; m2<(L-1); m2++){
                   num[m2]=num[m2+1];
                }
               newL=L-1;
            }
        }

        for(int m=0; m<newL; m++)
        {
            out<<num[m];
        }
        out<<endl;

                                       // getchar();
        }
    i++;
    }



myfile.close();
out.close();

}



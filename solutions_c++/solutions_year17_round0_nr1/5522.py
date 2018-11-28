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
        //cout<<"i= "<<i<<endl;
        if(i==0)
        {
            int T;
            if ( ! (istringstream(line) >> T) ) T = 0;

        }
        else
        {
            int j=0;
            int L=line.length();
            int Smax=L-2;
            int series[Smax];

            while(j<Smax)
            {
                char pm2=line.at(j);
                stringstream ss;
                string pm;
                ss << pm2;
                ss >> pm;
                if(pm=="+")
                {
                    series[j]=2;
                    j++;
                }
                else if(pm=="-")
                {
                    series[j]=1;
                    j++;
                }
                else{break;}


            }
            int S=j;
           /* for(int k=0; k<S; k++)
            {
                cout<<series[k]<<endl;
            }*/


            string end3=line.substr(S,(L-S));
           int K;
if ( ! (istringstream(end3) >> K) ) K = 0;
            /*char c =line.at(j+1);
            int K = c-48;*/

            //cout<<"j+1=  "<<j+1<<"  K= "<<K<<endl;

            /*for(int l=0; l<S; l++)
            {
                cout<<series[l]<<endl;
            }

            cout<<endl;*/
            int flip=0;
            string result;
             for(int i=0; i<=(S-K); i++)
        {

            if((series[i] % 2)!=0)
            {
                for(int j=i; j<(i+K); j++)
                {

                    series[j]++;
                }
                flip++;
            }
        }
          /*     for(int k=0; k<S; k++)
        {
            cout<<series[k]<<endl;
        }*/

        stringstream ss3;
ss3 << flip;
string str = ss3.str();
result=str;
        for(int k=0; k<S; k++)
        {
            if((series[k]%2)!=0){

                result="IMPOSSIBLE";
            }
        }

        out<<"Case #"<<i<<": "<<result<<endl;
        }
        i++;
    }



    myfile.close();
    out.close();
}

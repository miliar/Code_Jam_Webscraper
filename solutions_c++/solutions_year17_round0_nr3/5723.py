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
    int t, N,K ;
    int finalmin,finalmax;
    myfile >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    myfile >> N >> K;

    int baths[N+2];
    for(int k=0;k<(N+2); k++){
        baths[k]=0;
    }
    baths[0]=1;
    baths[N+1]=1;

    for(int k=1; k<=K; k++){

                int mint=0;
                int maxt=0;
                int sfin=0;
        for(int s=1;s<(N+1);s++){

            if(baths[s]==0){
               //right
               int rstry=0;
               for(int r=1; r<=(N-s);r++){
                if(baths[s+r]==1){break;}
                rstry++;
                }
             //left
                int lstry=0;
                 for(int l=1; l<s;l++){
                if(baths[s-l]==1){break;}
                lstry++;
                }
                int mini=min(lstry,rstry);
                int maxi=max(lstry,rstry);
             if(mini>mint){
                sfin=s;
                mint=mini;
                maxt=maxi;
                }
             if(mini==mint){
                if(maxi>maxt){
                  sfin=s;
                  mint=mini;
                  maxt=maxi;
                }
                if(maxi==maxt){
                  if(s<sfin){
                    sfin=s;
                    mint=mini;
                    maxt=maxi;
                  }
                }
             }


            }


        }
        baths[sfin]=1;
        if(k==K){
            finalmin=mint;
            finalmax=maxt;
        }


    }

    out<<"Case #"<<i<<": "<<finalmax<<" "<<finalmin<<endl;

  }

myfile.close();
out.close();

}



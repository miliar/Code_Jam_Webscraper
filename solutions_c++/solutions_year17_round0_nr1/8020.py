#include<iostream>
#include<fstream>
#include<math.h>
#include<string>

using namespace std;
ifstream infile("A-large.in");
ofstream outfile("A_sol_large.in");

int main(){
    int lin;
    string k;
    int sz;
    int r=1;
    infile>>lin;
 //   cout<<lin<<endl;
    while(lin--){
        int time=0;
        infile>>k;
 //       cout<<k<<endl;
        int lt=k.length();
        infile>>sz;
 //       cout<<sz<<endl;
        int i=0;
        int j=0;
        for(i=0;i<= lt-sz;i++){
            if(k[i]=='-'){
                for(j=0;j<sz;j++){
                    if(k[i+j]=='+')
                        k[i+j]='-';
                    else
                        k[i+j]='+';
 //               cout<<k<<endl;
                }
                j=0;
            time++;
            }


        }
        int b=0;
        for(i=0;i<lt;i++){
            if(k[i]=='-'){
                b=1;
                break;
                }
            }
        if(b==0)
            outfile<<"Case #"<<r<<": "<<time<<endl;
        else
            outfile<<"Case #"<<r<<": IMPOSSIBLE"<<endl;

       r++;



}
}

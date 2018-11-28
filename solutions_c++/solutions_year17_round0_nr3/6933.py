#include<fstream>
#include<iostream>
#include<math.h>
using namespace std;


int main() {
    int t,x;
    unsigned long long n,k,y,l,pwr,top;
    ifstream fi("filein3.txt",ios::in);
    ofstream fo("fileout3.txt",ios::out);
    fi>>t;
    for(int h=0; h<t; h++) {
        fi>>n>>k;
        for (x=1;pow(2,x)-1<k;x++);
        pwr=pow(2,x-1);
        top=n-pwr+1;
        y=top/pwr;
        l=top-(y*pwr);
        n=(k-pwr+1)<=l?y+1:y;
        fo<<"case #"<<h+1<<": "<<n/2<<" "<<n/2- ((n%2)?0:1)<<"\n" ;
    }
}

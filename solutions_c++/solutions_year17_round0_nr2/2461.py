#include <iostream>
#include <stdlib.h>
#include <fstream>
using namespace std;
int main()
{
    ifstream cin2("B-large.in");
    ofstream cout2("salida2.out");
    string n;
    int k;
    cin2>>k;
    for(int u=1;u<=k;u++){
    cin2>>n;
    for(int i=1;i<n.size();i++){
        if(n[i]<n[i-1]){
            n[i-1]=(int)(n[i-1])-1;
            for(int j=i;j<n.size();j++){
                n[j]='9';
            }
            i=0;
        }
    }
    long long aux=atoll(n.c_str());
    cout2<<"Case #"<<u<<": "<<aux<<"\n";
    }
    return 0;
}

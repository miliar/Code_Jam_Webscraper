#include <iostream>
#include <map>
#include <queue>
#include <fstream>
using namespace std;
int main()
{
    ifstream cin2("A-large.in");
    ofstream cout2("salida2.out");
    string x;
    int n,c,c2,k;
    cin2>>n;
    for(int i=1;i<=n;i++){
        cin2>>x>>k;
        c=0;
        c2=0;
        for(int j=0;j<x.size();j++){
            if(x[j]=='-'&&j<=x.size()-k){
                c++;
                c2++;
                for(int u=j;u<j+k;u++){
                    if(x[u]=='+')x[u]='-';
                    else x[u]='+';
                }
            }
            else if(x[j]=='+')c++;
        }
        cout2<<"Case #"<<i<<": ";
        if(c==x.size())cout2<<c2<<"\n";
        else cout2<<"IMPOSSIBLE\n";
    }
    return 0;
}

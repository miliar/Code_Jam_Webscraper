#include<bits/stdc++.h>
using namespace std;
int main()
{
    fstream plik1,plik2;
    plik1.open( "C:\\Users\\G500\\Desktop\\plik\\inputb.txt",ios::in );
    plik2.open( "C:\\Users\\G500\\Desktop\\plik\\outputb.txt",ios::out ); //| ios::app );
    int T;
    long long k,n;
    string V;
    V.resize(20);
    plik1>>T;
    for(int t=1;t<=T;t++)
    {
        plik1>>V;
        n=V.size();
        for(int i=n-1;i>=0;i--)
        {
            if(V[i]<V[i-1])
            {
                V[i-1]--;
                for(int j=i;j<n;j++)
                {
                    V[j]='9';
                }
            }
        }
        plik2<<"Case #"<<t<<": ";
        for(int i=0;i<n;i++)
        {
            if(i==0 && V[i]=='0') continue;
            plik2<<V[i];
        }
        plik2<<"\n";
    }
    plik1.close();
    plik2.close();
    return 0;
}

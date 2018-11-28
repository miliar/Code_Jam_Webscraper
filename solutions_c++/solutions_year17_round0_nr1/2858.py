#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    fstream plik1,plik2;
    plik1.open( "C:\\Users\\G500\\Desktop\\plik\\inputa.txt",ios::in );
    plik2.open( "C:\\Users\\G500\\Desktop\\plik\\outputa.txt",ios::out ); //| ios::app );
    bool czy=0;
    int T,k,licznik=0,n;
    string S;
    plik1>>T;
    for(int t=1;t<=T;t++)
    {
        czy=0;
        licznik=0;
        plik1>>S>>k;
        n=S.size();
        for(int i=0;i<=n-k;i++)
        {
            if(S[i]=='+') continue;
            licznik++;
            for(int j=i;j<k+i;j++)
            {
                if(S[j]=='-') S[j]='+';
                else S[j]='-';
            }
        }
        for(int i=n-k+1;i<n;i++)
        {
            if(S[i]=='-')
            {
                czy=1;
                break;
            }
        }
        plik2<<"Case #"<<t<<": ";
        if(czy) plik2<<"IMPOSSIBLE\n";
        else plik2<<licznik<<"\n";
    }
    plik1.close();
    plik2.close();
    return 0;
}

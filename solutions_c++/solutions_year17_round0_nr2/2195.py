#include <iostream>
#include <cstring>
#include<fstream>
using namespace std;
char s[1000];
int v[1000];
int i,j,t,n,dim,poz;
bool verif(int dim)
{
    for(int i=1;i<dim;++i)
        if(v[i]>v[i+1])return 0;
    return 1;
}
int main()
{
    ifstream fin("text,in");
    fin>>n;
    ofstream fout("text.out");
    for(i=1;i<=n;++i)
    {
        fin>>(s+1);
        dim=strlen(s+1);
        for(j=1;j<=dim;++j)
            v[j]=s[j]-'0';
        poz=dim;
        while(!verif(dim))
        {
            while(v[poz-1]>=v[poz])--poz;
            --v[poz];
            for(j=poz+1;j<=dim;++j)v[j]=9;
        }
        fout<<"Case #"<<i<<": ";
        poz=1;while(!v[poz])++poz;
        for(j=poz;j<=dim;++j)fout<<v[j];
        fout<<'\n';
    }
    return 0;
}

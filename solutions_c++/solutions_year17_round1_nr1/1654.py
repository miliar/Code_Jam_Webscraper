#include <iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
int t,n,m,i,j,it;
char a[40][40];
void umplere (int i,int j)
{
    int poz;
    char val=a[i][j];
    poz=i-1;
    while(poz>0 && a[poz][j]=='?')
    {
        a[poz][j]=val;
        --poz;
    }
    poz=i+1;
    while(poz<=n && a[poz][j]=='?')
    {
        a[poz][j]=val;
        ++poz;
    }
}
void extindere(int i,int j)
{
    int poz;
    char val=a[i][j];
    poz=j-1;
    while(poz>0 && a[i][poz]=='?')
    {
        a[i][poz]=val;
        --poz;
    }
    poz=j+1;
    while(poz<=m && a[i][poz]=='?')
    {
        a[i][poz]=val;
        ++poz;
    }
}
int main()
{
    ifstream fin("text.in");
    ofstream fout("text.out");
    fin>>t;
    for(it=1;it<=t;++it)
    {
        fin>>n>>m;
        for(i=1;i<=n;++i)
            for(j=1;j<=m;++j)
            fin>>a[i][j];
        for(i=1;i<=n;++i)
            for(j=1;j<=m;++j)
            if(a[i][j]!='?')
                umplere(i,j);
        for(i=1;i<=n;++i)
            for(j=1;j<=m;++j)
            if(a[i][j]!='?')
                extindere(i,j);
        fout<<"Case #"<<it<<":\n";
        for(i=1;i<=n;++i)
        {
            for(j=1;j<=m;++j)
                fout<<a[i][j];
            fout<<'\n';
        }
    }
    return 0;
}

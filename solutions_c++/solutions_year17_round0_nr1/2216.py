#include <iostream>
#include<fstream>
#include<cstring>
using namespace std;
int v[2010],i,j,k,n,it,t,sol,ok;
char s[1010];
int main()
{
    ifstream f("text.in");
    f>>t;
    ofstream g("text.out");
    for(it=1;it<=t;++it)
    {
        f>>(s+1);n=strlen(s+1);
        for(i=1;i<=n;++i)
            if(s[i]=='+')v[i]=1;
                else v[i]=0;
        f>>k;
        sol=0;
        for(i=1;i<=n-k+1;++i)
            if(!v[i])
        {
            ++sol;
            for(j=i;j<i+k;++j)v[j]=(v[j]+1)%2;
        }
        ok=1;
        for(i=1;i<=n;++i)
            if(!v[i])ok=0;
        if(ok)
            g<<"Case #"<<it<<": "<<sol<<'\n';
        else
            g<<"Case #"<<it<<": "<<"IMPOSSIBLE"<<'\n';
    }
    return 0;
}

#include<bits/stdc++.h>
using namespace std;

int val[10000],in[10000];

int mv,n;

bool ok(int z)
{
    memset(val,0,sizeof val);
    int v=0,ck=1;
    for(int i=0; i<n; i++)
    {
        if((v%2==0 && in[i]==1)||(v%2==1 && in[i]==0))
        {
            if(i+z-1<n)
            {
                mv++;
                v++,val[i+z-1]--;
            }
            else return 0;
        }
        v+=val[i];
    }
    return 1;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    int t,k,i;
    scanf("%d",&t);
    for(int ca=1; ca<=t; ca++)
    {
        string str;
        cin >> str >> k;
        n=str.size();
        for(i=0; i<str.size(); i++)
        {
            if(str[i]=='-') in[i]=1;
            else in[i]=0;
        }
        mv=0;
        if(ok(k))
        {
            printf("Case #%d: %d\n",ca,mv);
        }
        else printf("Case #%d: IMPOSSIBLE\n",ca);
    }
}


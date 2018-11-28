#include<bits/stdc++.h>
#define X first
#define Y second
#define MEM(x,y) memset(x,y,sizeof x)
using namespace std;
string s;
bool f(int i,int mmin)
{
    if(i==s.size())return 1;
    if(s[i]-'0'<mmin)
    {
        for(int j=i;j<s.size();j++)s[j]='9';
        return 0;
    }
    if(!f(i+1,s[i]-'0'))
    {
        if(s[i]=='0')
        {
            s[i]='9';
            return 0;
        }
        else
        {
            s[i]--;
            if(s[i]-'0'<mmin)
            {
                for(int j=i;j<s.size();j++)s[j]='9';
                return 0;
            }
            return 1;
        }
    }
    return 1;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas,lzero,i;
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        cin>>s;
        f(0,0);
        printf("Case #%d: ",cas);
        lzero=1;
        for(i=0;i<s.size();i++)
        {
            if(lzero&&s[i]=='0')continue;
            lzero=0;
            printf("%c",s[i]);
        }
        printf("\n");
    }
}

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;

const int maxn=1005;

int N;
int dir[maxn],f[maxn];

int calc(int k)
{
    memset(f,0,sizeof(f));
    int res=0;
    int sum=0;   //f的总和
    for(int i=0;i+k<=N;i++)
    {
        if((dir[i]+sum)%2!=0)
        {
            res++;
            f[i]=1;
        }
        sum+=f[i];
        if(i-k+1>=0)
            sum-=f[i-k+1];     //考虑前面的翻转对后面的影响
    }

    for(int i=N-k+1;i<N;i++)
    {

        if((dir[i]+sum)%2!=0)
            return -1;
        if(i-k+1>=0)
            sum-=f[i-k+1];
    }
    return res;
}

void solve()
{
    int t;
    cin>>t;
    for(int id=1;id<=t;id++)
    {
        string s;
        cin>>s;
        int k;
        cin>>k;
        N=s.size();
        for(int i=0;i<N;i++)
        {
            if(s[i]=='+')
                dir[i]=0;
            else if(s[i]=='-')
                dir[i]=1;
        }
        int ans=calc(k);
        cout<<"Case #"<<id<<": ";
        if(ans==-1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<ans<<endl;
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    solve();
    return 0;
}

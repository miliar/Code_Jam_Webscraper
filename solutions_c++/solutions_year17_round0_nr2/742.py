//created by missever

#include<bits/stdc++.h>
#define MAX 1000000007
using namespace std;
typedef long long LL;

int a[20];
int b[20];

bool dfs(int k,int d,bool vis)
{
    if(k == 19) return true;
    if(!vis)
    {
        if(a[k] >= d && dfs(k + 1,a[k],0))
        {
            b[k] = a[k];
            return true;
        }
        for(int i = a[k] - 1; i >= d; i--)
        {
            if(dfs(k + 1,i,1))
            {
                b[k] = i;
                return true;
            }
        }
    }
    else
    {
        for(int i = 9; i >= d; i--)
        {
            if(dfs(k + 1,i,1))
            {
                b[k] = i;
                return true;
            }
        }
    }
    return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    LL n;
    int t,i;
    cin>>t;
    for(int cas = 1; cas <= t; cas++)
    {
        cin>>n;
        for(i = 0; i < 19; i++)
        {
            a[18 - i] = n % 10;
            n /= 10;
        }
        dfs(0,0,0);
        cout<<"Case #"<<cas<<": ";
        for(i = 0; i < 19; i++)
        {
            if(b[i]) break;
        }
        for(i = i; i < 19; i++) cout<<b[i];
        cout<<endl;
    }
    return 0;
}

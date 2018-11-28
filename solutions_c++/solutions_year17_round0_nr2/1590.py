#include <bits/stdc++.h>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define FOR(i,j,k) for(int i=j;i<=k;i++)
#define REV(i,j,k) for(int i=j;i>=k;i--)
#define FORR(i,j,k,l) for(int i=j;i<=k;i+=l)
#define inf         freopen("in.txt", "r", stdin)
#define outf        freopen("out.txt", "w", stdout)
#define pf          printf
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c)    scanf("%d %d %d", &a, &b, &c)
#define minn          (long long)-1000000000000000000
#define maxx          (long long) 1000000000000000000
#define mod          1000000007
#define LL           long long
#define NL '\n'
#define cnd tree[idx]
#define lnd (2*idx)
#define rnd ((2*idx)+1)
#define PB push_back
#define F first
#define S second
#define MK make_pair
typedef pair<int,int> pr;

string str,ans;
int main()
{
    ios::sync_with_stdio(false);
    inf;
    outf;
    int tc;
    cin>>tc;
    FOR(tt,1,tc)
    {
        LL i,j,x,y,n,m,a=0,b=1,c=0,k;
        char ch;
        cin>>str; n=str.size();
        ans=str;
        while(b==1)
        {
            b=0;
            FOR(i,0,n-2)
            {
                if(b==0&&(str[i]>str[i+1]))
                {
                    str[i]--;
                    b=1;
                }
                else if(b==1) str[i]='9';
            }
            if(b==1) str[n-1]='9';
        }
        while(str[0]=='0')
        {
            str.erase(0,1);
        }
        cout<<"Case #"<<tt<<": "<<str<<NL;

    }
    return 0;
}



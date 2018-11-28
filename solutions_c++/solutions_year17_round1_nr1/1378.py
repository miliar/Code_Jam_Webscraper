/* ***********************************************
Author        :yby
Created Time  :2017年04月15日 星期六 09时07分59秒
File Name     :a.cpp
************************************************ */

#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define per(i,a,b) for(int i=a;i>=b;i--)
#define foreach(i,a) for(int i=head[a];i>=0;i=e[i].next)
#define Foreach(i,a) for(__typeof((a).begin())i=(a).begin();i!=(a).end();i++)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define mp make_pair
#define m0(x) memset(x,0,sizeof(x))
#define mff(x) memset(x,0xff,sizeof(x))
#define fi first
#define se second
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define SZ(x) ((int)(x).size())
#define abs(x) ((x)>0?(x):-(x))
#define sqr(x) ((x)*(x))
#define C1(x) cout<<(x)<<endl
#define C2(x,y) cout<<(x)<<" "<<(y)<<endl
#define C3(x,y,z) cout<<(x)<<" "<<(y)<<" "<<(z)<<endl
typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef pair<int,pair<int,int> > PIII;
typedef vector<PIII> VPIII;
typedef vector< pair<int,int> > VPII;
const ll mod=1e9+7;
const ll maxn=1e5+7;
const ll maxe=1e6+7;
const ll INF=1e9+7;
const double PI=acos(-1);
int dx[4]={0,0,1,-1};
int dy[4]={-1,1,0,0};
int T,n,m;
vector<int> v;
vector<int> vv;
string ans[30];
string g;
int main()
{
    //freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;    
    for(int ca=1;ca<=T;ca++)
    {
        v.clear();
        vv.clear();
        printf("Case #%d: \n",ca);
        cin>>n>>m;
        int ok=1;
        for(int i=1;i<=n;i++)
        {
            string s;
            cin>>s;
            ans[i]=s;
            v.clear();
            for(int j=0;j<m;j++)
            {
                if(s[j]!='?')v.pb(j);
            }
            if(v.size())
            {
                int be=0;
                for(int k=0;k<v.size();k++)
                {
                    int now=s[v[k]];
                    for(int j=ok;j<=i;j++)
                    {
                        for(int w=be;w<=v[k];w++)ans[j][w]=now;
                    }
                    be=v[k]+1;
                }
                    for(int j=ok;j<=i;j++)
                    {
                        for(int w=be;w<m;w++)ans[j][w]=s[v[SZ(v)-1]];
                    }
                ok=i+1;
                vv=v;
                g=s;
            }
        }
                v=vv;
                string s=g;
                int be=0;
                for(int k=0;k<v.size();k++)
                {
                    int now=s[v[k]];
                    for(int j=ok;j<=n;j++)
                    {
                        for(int w=be;w<=v[k];w++)ans[j][w]=now;
                    }
                    be=v[k]+1;
                }
                    for(int j=ok;j<=n;j++)
                    {
                        for(int w=be;w<m;w++)ans[j][w]=s[v[SZ(v)-1]];
                    }
        for(int i=1;i<=n;i++)cout<<ans[i]<<endl;
    }
    return 0;
}

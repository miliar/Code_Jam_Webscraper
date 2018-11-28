#include <bits/stdc++.h>
using namespace std;
#define MEM(a) memset(a,0,sizeof(a))
#define rp(i,a,n) for ( i=a;i<n;i++)
#define pr(i,a,n) for ( i=n-1;i>=a;i--)
#define S(x) scanf("%d",&x)
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(),(x).end()
#define sz(x) ((int)(x).size())
#define F first
#define S second
#define IT(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define MAX 105000
typedef vector<int> vi;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<ll> vll;
const ll mod=1000000007;
int dr[8] = {1,1,0,-1,-1,-1, 0, 1};
int dc[8] = {0,1,1, 1, 0,-1,-1,-1};
int dh[4] = {0, 1, 0, -1};
int dv[4] = {-1, 0, 1, 0};
void solve(int x)
{
    ll n,ans;
    int i,j,k;
    cin>> n;
    char q[100]={0};
    sprintf( q,"%lld",n);
    cout<<"Case #"<<x<<": ";

    if(strlen(q)==1){cout<<n<<endl; return ;}
    rp(i,1,strlen(q)) if(q[i]<q[i-1]) break;
    if(i==strlen(q)){cout<<n<<endl; return ;}


    int n0=0,n1=0,n2=0;
    ans=0;
    rp(i,0,strlen(q)-1)
    {
        ans=ans*10 + 9;
    }
    rp(i,0,strlen(q)-1)
    {
        if(q[i]=='0') n0++;
        else if(q[i]=='1') n1++;
        else n2++;
        if(q[i]=='0'&&n2==0)  break;
    }
    if(n2==0) { cout<<ans<<endl;return;}
    if(i<(strlen(q)-1)) { cout<<ans<<endl;return;}
     rp(i,0,strlen(q)-1)
    {
        if((q[i+1]<q[i])&&q[i]>'1')
        {
            q[i]--;
            rp(j,i+1,strlen(q)) q[j]='9';
            pr(j,0,i)
            {
                if(q[j]<=q[j+1]) break;
                else
                {
                    q[j]--;
                    q[j+1]='9';
                }
            }
             break;
        }

    }
    cout<<q<<endl;
}
int main()
{
    int t,i;
   freopen("in.in","r",stdin);
   freopen("out.txt","w",stdout);
    cin>>t;
    rp(i,1,t+1) solve(i);
    return 0;
}

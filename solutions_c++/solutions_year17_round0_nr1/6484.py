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
    string s;
    int ans=-1;
    int i,j,k,l;
    cin>>s>>k;
    string t=s;
    l=0;
    rp(i,0,s.length()-k+1)
    {
        if(s[i]=='-')
        {
            l++;
            rp(j,i,i+k)
            {
                if(s[j]=='-')  s[j]='+';
                else s[j]='-';
            }
        }
       // cout<<s<<endl;
    }
    rp(i,0,s.length())  if(s[i]=='-') break;
    if(i==s.length()) ans=l;

   /* l=0;
    pr(i,k-1,t.length())
    {
        if(t[i]=='-')
        {
            l++;
            pr(j,i-k+1,i+1)
            {
                if(t[j]=='-')  t[j]='+';
                else t[j]='-';
            }
        }
    }
    rp(i,0,t.length())  if(t[i]=='-') break;
    if(i==t.length()) {
        if(ans==-1) ans=l;
        else ans=min(ans,l);
    }*/
    cout<<"Case #"<<x<<": ";
    if(ans==-1) cout<<"IMPOSSIBLE"<<endl;
        else cout<<ans<<endl;

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

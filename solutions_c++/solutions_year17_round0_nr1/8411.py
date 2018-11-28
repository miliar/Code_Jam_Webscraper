#include<bits/stdc++.h>
using namespace std;

#define In freopen("F:/input.txt","r",stdin)
#define Out freopen("F:/output.txt","w",stdout)
#define fast ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define ll long long
#define int long long
#define mod 1000000007
#define rep(i,x,y) for (__typeof(y) i=x;i<=y;i++)
#define brep(i,x,y) for(__typeof(x) i=x;i>=y;i--)
#define all(c) (c).begin(),(c).end()
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>


int power(int a , int b)
{
    int res = 1 ;
    while(b)
    {
        if(b%2) {
            res = (res * a) % mod ;
        }
        b/=2 ;
        a = (a*a) % mod ;
    }
    return res ;
}

int test,k,ans;
string s;

int32_t main()
{
    #ifndef ONLINE_JUDGE
        In;
        Out;
    #endif
    fast;
    cin>>test;
    rep(t,1,test) {
        cout<<"Case #"<<t<<": ";
        cin>>s>>k;
        ans=0;
        rep(i,0,s.length()-k) if(s[i]=='-') {
            ans++;
            rep(j,0,k-1) s[i+j]=(s[i+j]=='+') ? '-' : '+';
        }
        rep(i,0,s.length()-1) if(s[i]=='-') ans=-1; 
        if(ans==-1) cout<<"IMPOSSIBLE";
        else cout<<ans;
        cout<<endl;
    }
    return 0;
}

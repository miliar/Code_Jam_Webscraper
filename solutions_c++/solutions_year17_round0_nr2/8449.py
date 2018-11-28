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

int t,len;
string s;
bool flag;

void solve(int i) {
    if(i==len) return;
    if(s.substr(i+1) >= string(len-i-1,s[i])) {
        if(s[i]!='0') flag=1;
        if(s[i]!='0' || flag) cout<<s[i];
        solve(i+1);
    }
    else {
        char c=s[i]-1;
        if(c!='0') flag=1;
        if(c!='0' || flag) cout<<c;
        cout<<string(len-1-i,'9');
    }
}

int32_t main()
{
    #ifndef ONLINE_JUDGE
        In;
        Out;
    #endif
    fast;
    cin>>t;
    rep(i,1,t) {
        cout<<"Case #"<<i<<": ";
        cin>>s;
        flag=0;
        len=s.length();
        solve(0);
        cout<<endl;
    }
    return 0;
}

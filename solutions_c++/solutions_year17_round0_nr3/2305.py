using namespace std;
#include <bits/stdc++.h>
#define rep(i,n) for(auto i=0; i<(n); i++)
#define mem(x,val) memset((x),(val),sizeof(x));
#define rite(x) freopen(x,"w",stdout);
#define read(x) freopen(x,"r",stdin);
#define all(x) x.begin(),x.end()
#define sz(x) ((int)x.size())
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define clr clear()
#define inf (1<<30)
#define ins insert
#define xx first
#define yy second
#define eps 1e-9
#define MOD 1000000007
#define foreach(it, l) for (auto it = l.begin(); it != l.end(); it++)
typedef long long i64;
typedef unsigned long long ui64;
typedef string st;
typedef vector<int> vi;
typedef vector<st> vs;
typedef map<int,int> mii;
typedef map<st,int> msi;
typedef set<int> si;
typedef set<st> ss;
typedef pair<int,int> pii;
typedef vector<pii> vpii;
#define mx 0
int flog2(i64 n)
{
    int r=0;
    while(n>>=1) r++;
    return r;
}
int main() {
    ios_base::sync_with_stdio(0);
    int t,s,count;
    i64 j,n,i,k,y,p;
    cin>>t;
    count=1;
    while(count<=t)
    {
        count++;
        cin>>n>>k;
        s=flog2(k);
        y=1UL<<s;
        i=(n-y+1)/y;
        p=(n-y+1)%y;
        if(k-y+1<=p)
            j=i+1;
        else
            j=i;    
        cout<<"Case #"<<count-1<<": ";
        cout<<j/2<<" "<<(j-1)/2;
        cout<<endl;
    }
    return 0;
}

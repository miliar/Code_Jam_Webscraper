#include<bits/stdc++.h>
#include <iomanip>
using namespace std;
 
typedef long long ll;
typedef vector < long long > vll;
typedef unsigned long long ull;
typedef pair < long long,  long long > pll;
typedef pair < int,  int > pii;
typedef pair < int, pii > ppi;
typedef vector < int > vii;
typedef vector < pii > vpii;
 

#define endl '\n'
#define Endl '\n'
#define ff first
#define ss second
#define sz size()
#define clr clear()
#define len length()
#define pb push_back
#define mp make_pair
#define finp cin.sync_with_stdio(0);cin.tie(0);
#define test int t;cin>>t;while(t--)
#define test1 int t;cin>>t;for(int tt=1;tt<=t;tt++)
#define rep(i,n) for(int i=0;i<n;i++)
#define frep(i,a,b) for(int i=a;i<=b;i++)
#define brep(i,n) for(int i=n-1;i>=0;i--)
#define fbrep(i,a,b) for(int i=a;i>=b;i--)
 
const int N = 1e5 + 500;
const ll mod = 1e9 + 7;
const ll INF = 1LL << 57LL;
 
//Fast expo
 
ll expo(ll a , ll b)
{
    if(b==0)
        return 1;
    else if(b%2==0)
        return expo(a*a,b/2);
    else
        return a*expo(a*a,b/2);
}
 
ll hcf(ll a, ll b){
    a = abs(a); b =abs(b);
    return (b==0) ? a : hcf(b, a%b);
  }
 
//comparing pair wrt to 2nd
 
/*bool compare2(const pii &i, const pii &j)
{
    return i.ss < j.ss;
}*/

ll abs(ll a , ll b)
{
    if(a>b)
        return a-b;
    return b-a;
}

string solve(string s)
{
    string ans="";
    brep(i,s.sz-1)
    {
        if(s[i]>s[i+1])
        {
            s[i]-=1;
            frep(j,i+1,s.sz-1)
            {
                s[j]='9';
            }
        }
    }
    bool init = true;
    rep(i,s.sz)
    {
        if(init && s[i]=='0')
        {
            continue;
        }
        else
        {
            init = false;
            ans+=s[i];
        }
    }
    return ans;
}
 
int main()
{
    finp
    #ifdef HEXCHEX
        freopen("input1.txt","r",stdin);
        freopen("output1.txt","w",stdout);
    #endif
    test1{
        string s;
        cin>>s;
        cout<<"Case #"<<tt<<": "<<solve(s)<<endl;
    }
    
    // cout<<"\nTime elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC << " s.\n";
    return 0;
} 
#include<bits/stdc++.h>
#include <ext/numeric>
using namespace std;
#define sc(a) scanf("%d",&a)
#define sc2(a,b) scanf("%d%d",&a,&b)
#define sc3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sc4(a,b,c,d) scanf("%d%d%d%d",&a,&b,&c,&d)
#define scd(a) scanf("%lf",&a)
#define scd2(a,b) scanf("%lf%lf",&a,&b)
#define scd3(a,b,c) scanf("%lf%lf%lf",&a,&b,&c)
#define scd4(a,b,c,d) scanf("%lf%lf%lf%lf",&a,&b,&c,&d)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define ALL(x) x.begin(), x.end()
#define BUFF ios::sync_with_stdio(false);
#define endl "\n"
#define power(a,x) __gnu_cxx::power(a, x)
#define forN(i,n) for(int i=0;i<n;i++)
#define eps 1e-5
#define INF INT_MAX
#define INFLL LLONG_MAX
#define gcd(a,b) __gcd(a,b)
typedef unsigned long long int ull;
typedef long long int ll;
typedef long double ld;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vector<int> >vvi;
#define MAXN 1100
#define cin in
#define cout out
bool v[MAXN];
bool en[MAXN];
int solve(int i,string s)
{
    if(i==s.size())return i;
    if(s[i]<s[i-1])return i;
    return solve(i+1,s);
}
int main()
{
    ifstream in;
    ofstream out;
    in.open ("in.in");
    out.open ("out.txt");
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string s;
        cin>>s;
        int bad=solve(1,s);
        if(bad<s.size())
        {
            for(int i=bad;i<s.size();i++)s[i]='9';
            for(int i=bad-1;i>=0;i--)
            {
                s[i]--;
                if(s[i]<'0')
                {
                    s[i]='9';
                }
                else if(i>0 && s[i]<s[i-1])
                {
                    s[i]='9';
                }
                else break;
            }
            if(s[0]=='0')s=s.substr(1);
        }
        cout<<"Case #"<<tt<<": "<<s<<endl;
    }
    in.close();
    out.close();
    return 0;
}

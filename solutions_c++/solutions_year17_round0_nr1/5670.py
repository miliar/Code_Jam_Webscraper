///Abdullah Al Mahmud
///Khulna University

#include<bits/stdc++.h>

using namespace std;

const int MOD = (int) 1e9 + 7;
const int INF = (int) 1e9+21;
const long long LINF = (long long) 1e18;
const long double PI = 2 * acos((long double)0);

typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pi> vii;

#define Mahmud main()
#define endl "\n"
///STL
#define pb push_back
#define pf push_front
#define fi first
#define se second
#define sz(x) ((int)(x).size())
#define all(x) x.begin(),x.end()
///Debug
#define dbg1(x) std::cerr<<#x<<"="<<(x)<<endl;
#define dbg2(x,y) std::cerr<<#x<<"="<<(x)<<','<<#y<<"="<<(y)<<endl;
#define dbg3(x,y,z) std::cerr<<#x<<"="<<(x)<<','<<#y<<"="<<(y)<<','<<#z<<"="<<(z)<<endl;
#define dbgArr(arr,n) cerr<<#arr<<"=["; printArray(arr,n,0,93); cerr<<endl;
///traversing
#define rep(n) for(int i=0;i<n;++i)
#define trv(i,t) for(__typeof(t.begin()) i=t.begin();i!=t.end();++i)
///necessary functions
inline ll Int()
{
    ll _x=0,_tmp=1;
    char _tc=getchar();
    while( (_tc<'0'||_tc>'9')&&_tc!='-' ) _tc=getchar();
    if( _tc == '-' ) _tc=getchar(), _tmp = -1;
    while(_tc>='0'&&_tc<='9') _x*=10,_x+=(_tc-'0'),_tc=getchar();
    return _x*_tmp;
}
inline long double Double()
{
    long double d;
    scanf("%Lf",&d);
    return d;
}
ll lcm(ll a,ll b)
{
    return a/__gcd(a,b)*b;
}
int ton(string x)
{
    int y;
    std::istringstream ss(x);
    ss >> y;
    return y;
}
template<typename T>
string tostring(T x)
{
    ostringstream ss;
    ss << x ;
    return ss.str();
}

///Current Code vars
#define MAX 100000
long long n,k,c,d;
int arr[MAX+1],brr[MAX+1];
///Current Code functions


void solve()
{
    int t = Int();
    for(int cs=1;cs<=t;++cs)
    {
        string s;int ks;
        cin>>s;
        ks = Int();
        int ans = 0;
        bool ok = true;
        for(int i=0;i<sz(s);++i)
        {
            //dbg2(i,s);
            if(s[i]=='-')
            {
                if(i+ks <= sz(s))
                {
                    ans++;
                    for(int j = i;j < i+ks;++j)
                    {
                        if(s[j]=='-') s[j]='+';
                        else s[j]='-';
                    }
                }
                else
                {
                    ok = false;
                    break;
                }
            }
        }
        printf("Case #%d: ",cs);
        if(ok) printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
}

int Mahmud
{
    freopen("A-large.in", "r", stdin);
   // freopen("A-L.out", "w", stdout);
    solve();

//#ifdef _LOCAL_
    //printf("\nTime elapsed: %dms", 1000 * clock() / CLOCKS_PER_SEC);
//#endif
    return 0;
}




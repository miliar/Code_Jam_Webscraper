/* Eat a live frog first thing in the morning,
   and nothing worse will happen to you the rest of the day */

/* You can't connect the dots looking forward 
   you can only connect them looking backwards. */

/* Nothing is impossible; impossible itself says "I'm possible" */

#include<bits/stdc++.h>
#define ll long long
#define ld long double
#define ull unsigned long long
#define boost ios_base::sync_with_stdio(false);cin.tie(0);cout.precision(10);cout << fixed;
#define dbset(x) for(int i=0 ; i<x.size(); i++) cerr << x[i] << " "; cerr << endl;
#define inf 1000000007
#define INF 1000000000000000000LL
#define PI 3.14159265358979323846
#define mod 1000000007
#define mod1 1000696969
#define flusz fflush(stdout);
#define VI vector<int>
#define VPI vector < pair<int,int> >
#define PII pair<int, int>
#define BIT bitset<N>
#define st first
#define nd second
#define pb push_back
#define mp make_pair
#define eb emplace_back
#define endl '\n'
#define REP(x, y) for(int x = 0; x < (y); ++x)
#define FOR(x, y, z) for(int x = y; x <= (z); ++x)
#define FORR(x, y, z) for(int x = y; x >= (z); --x)
using namespace std;

template<class TH> void _dbg(const char *sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<"="<<h<<","; _dbg(sdbg+1, a...);
}
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)

#define int long long
#define N 1007

int test;

int n,c,m; // ile miejsc, ile klientow, ile biletow

int t[N];
int kl[N];

void solve()
{
    cin >> n >> c >> m;

    FOR(i,1,1000){
        t[i]=0;kl[i]=0;
    }

    FOR(i,1,m){
        int a,b; // pozycja, kupujacy
        cin >> a >> b;
        kl[b]++;
        t[a]++;
    }

    int res=0;

    FOR(i,1,c){
        res=max(res,kl[i]);
    }

    int pom=0;

    FOR(i,1,n){
        pom+=t[i];
        res=max(res,pom/i+(pom%i!=0));
    }

    int res2=0;

    FOR(i,1,n){
        res2+=max((ll)0,t[i]-res);
    }

    cout << res << " " << res2 << endl;

    return;
}

int32_t main()
{
    boost

    cin >> test;

    FOR(i,1,test)
    {
        cout << "Case #" << i << ": ";
        solve();
    }

  return 0;
}

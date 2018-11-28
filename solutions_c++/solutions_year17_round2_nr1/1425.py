// sahilarora.535 - NeverSettle
#include<bits/stdc++.h>
using namespace std;
#define fio             ios_base::sync_with_stdio(false); cin.tie(NULL)
#define tr(c,i)         for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define rep(i,begin,end)for(__typeof(end) i=(begin)-((begin)>(end));i!=(end)-((begin)>(end));i+=1-2*((begin)>(end)))
#define present(c,x)    ((c).find(x) != (c).end()) 
#define cpresent(c,x)   (find(all(c),x) != (c).end()) 
#define ll              long long
#define ii              pair<int,int>
#define pll             pair<ll,ll>
#define mp              make_pair
#define ff              first
#define ss              second
#define all(a)          a.begin(), a.end()
#define pb              push_back 
#define vi              vector< int >
#define vvi             vector< vi >
#define vll             vector< long long >
#define vvll            vector< vll >
#define vii             vector< ii >
#define vvii            vector< vii >
#define sz(C)           int((C).size()) 
#define sd(t)           scanf("%d",&t)
#define pd(t)           printf("%d\n",t)
#define slld(t)         scanf("%lld",&t)
#define plld(t)         printf("%lld\n",t)
#define sc(t)           scanf("%c",&t)
#define M_PI            3.14159265358979323846
#define EPS             1e-6

const ll INF = ~0ull >> 2;
const ll MAX = 100005;
const ll mod = 1e9+7;
// #define LOG
 
int main(int argc, char const *argv[]){
    fio;
    int test;
    cin>>test;
    for (int CASE = 1; CASE <= test; ++CASE) {
        cout << "Case #"<< CASE << ": ";
        ll n;
        double d;
        cin >> d >> n;
        vector<pair<ll, double>> v(n);
        vector<double> times(n, 0);
        rep (i, 0, n) cin >> v[i].ff >> v[i].ss;
        sort(all(v));
        times[n-1] = (d - v[n-1].ff) / v[n-1].ss;
        rep (i, n - 1, 0) {
            times[i] = (d - v[i].ff) / v[i].ss;
            if (times[i] < times[i+1]) times[i] = times[i+1];
        }
        cout << fixed << setprecision(6) << d / times[0] << "\n";
#ifdef LOG
#endif
    } 
    return 0;
}
 
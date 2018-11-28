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
    map<ll, ll, greater<ll>> MAP;
    for (int CASE = 1; CASE <= test; ++CASE) {
        cout << "Case #"<< CASE << ": ";
        ll n, k, y, z;  // y = max(Ls, Rs), z = min(Ls, Rs) 
        cin >> n >> k;
        --k;
        MAP.clear();
        MAP[n] = 1;
        ll temp = 0;
        while (!MAP.empty() && temp <= k) {
            auto it = MAP.begin();
            ll max_size = it -> ff;
            if(max_size % 2 && (max_size >> 1)) { MAP[max_size >> 1] += 2 * it -> ss; }
            else  {
                if (max_size >> 1) MAP[max_size >> 1] += it -> ss;
                if ((max_size >> 1) - 1) MAP[(max_size >> 1) - 1] += it -> ss;
            }
            temp += it -> ss;
            if (temp <= k) { MAP.erase(it); }
            else { break; }
        }
#ifdef LOG
        cout << "\n";
        tr (MAP, it) {
            cout << it->ff << " -- " << it->ss << "\n";
        }
#endif
        if (MAP.empty()) {
            cout << "0 0\n";
            continue;
        }
        z = y = MAP.begin() -> ff;
        z = (z % 2 ? z >> 1 : (z >> 1) - 1);
        if (z < 0) { z = 0; }
        y >>= 1;
        cout << y << " " << z << "\n";
    } 
    return 0;
}

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
 

bool check(string& s) {
    int n = s.size();
    if (n > 1 && s[0] == s[n-1]) return false;
    rep (i, 0, n-1) if(s[i] == s[i+1]) return false;
    return true;
}

string fix (string s) {
    int n = s.size();
   while(check(s) == false) {
    int idx = 0;
    swap(s[n-1], s[n-2]);
   }
   return s;
}

int main(int argc, char const *argv[]){
    fio;
    int test;
    cin>>test;
    for (int CASE = 1; CASE <= test; ++CASE) {
        cout << "Case #"<< CASE << ": ";
        int n;
        vector<pair<int, char>> v(6);
        cin >> n;
        int temp = n;
        string out;
        rep (i, 0, 6) cin >> v[i].ff;
        v[0].ss = 'R', v[1].ss = 'O', v[2].ss = 'Y', v[3].ss = 'G', v[4].ss = 'B', v[5].ss = 'V'; 
        int r, y, b;
        r = v[0].ff, y = v[2].ff, b = v[4].ff;
        int maxx = max(r, max(y, b)), minn = min(r, min(y, b));
        int midd = r + y + b - maxx - minn;
        if (maxx > midd + minn) {
            cout << "IMPOSSIBLE\n";
            continue;
        }
        set<pair<int, char>, greater<pair<int, char>>> SET;
        SET.insert(v[0]), SET.insert(v[2]), SET.insert(v[4]);
        auto it = *SET.begin();
        auto itr = SET.begin();
        // --itr;
        // if(n > 1) {
        //     --n;
        //     while((*itr).ff <= 0) --itr;
        //     SET.erase(itr);
        //     it = *itr;
        //     out.pb(it.ss);
        //     --it.ff;
        //     SET.insert(it);
        // }
        while (n--) {
            it = *SET.begin();
            char ch = it.ss;
            SET.erase(SET.begin());
            out.pb(it.ss);
            --(it.ff);
            SET.insert(it);
            if (n && (*SET.begin()).ss == ch) {
                itr = SET.begin();
                ++itr;
                it = *itr;
                out.pb(it.ss);
                // cout << it.ss;
                --it.ff;
                --n;
                SET.erase(itr);
                SET.insert(it);
            } 
        } 
        cout << fix(out) << "\n";
        if (count(all(out), 'R') != r || count(all(out), 'Y') != y || count(all(out), 'B') != b) {
            cout << "ERROR!!!\n";
        }
        if (out.size() != temp ) { cout << "NOOOOOO!!!\n";}
#ifdef LOG
#endif
    } 
    return 0;
}
 
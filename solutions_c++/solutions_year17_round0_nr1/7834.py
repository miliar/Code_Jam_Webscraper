#include <bits/stdc++.h>

#define all(x) x.begin(), x.end()
#define UN -1
#define VIS -2
#define EX 0
#define mp(a, b) make_pair(a, b)
#define pb push_back
#define clr(a) (a).clear()
#define sz(a) (int)(a).size()
#define forn(i, n) for(int i = 0; i < n; i++)
#define foren(i, n) for(int i = 1; i <= n; i++)
#define llm LONG_LONG_MAX
#define llmn LONG_LONG_MIN
#define intm INT_MAX
#define intmn INT_MIN
#define mod 1000000007
#define pi 3.14159265358979323
#define fio ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
using namespace std;
typedef long long ll; typedef vector<ll> vll; typedef pair<ll, ll> pll; typedef vector<pll> vpll;
typedef vector<int> vi; typedef pair<int, int> ii; typedef vector<ii> vii; typedef vector<vi> vvi;
typedef pair<int, ii> iii; typedef pair<ii, ii> iiii; typedef vector<iiii> viiii; typedef pair<ll, pll> tll;
typedef vector<vii> vvii; typedef vector<vll> vvll; typedef vector<char> vc; typedef vector<vc> vvc;
typedef vector<bool> vb; typedef vector<vb> vvb; typedef queue<int> qi; typedef queue<ll> qll;
typedef queue<ii> qii; typedef vector<tll> vtll; typedef vector<iii> viii; typedef pair<pll, pll> ppll;
typedef vector<ppll> vppll; typedef priority_queue<int> pqi; typedef priority_queue<ll> pqll;
typedef priority_queue<ii> pqii; typedef pair<int, ii> ti; typedef vector<ti> vti; typedef pair<ii, iiii> tii;
typedef vector<string> vs; typedef vector<double> vd; typedef vector<vc> vvc; typedef unordered_set<int> uset;
// TODO solve www.spoj.com/problems/VOCV/

int main() { fio
    ifstream in("/home/danza/ClionProjects/spoj/ot.txt");
    ofstream out("/home/danza/ClionProjects/spoj/out.txt");
    int TC, k, c;
    in >> TC;
    string s;
    bool ok;
    foren(tc, TC) {
        in >> s >> k;
        c = 0;
        ok = true;
        forn(i, sz(s) - k + 1) {
            if(s[i] == '-') {
                c++;
                for(int j = i; j < i + k; j++) s[j] = (s[j] == '-' ? '+' : '-');
            }
        }
        forn(i, sz(s)) {
            if(s[i] == '-') {
                out << "Case #" << tc << ": IMPOSSIBLE\n";
                ok = false;
                break;
            }
        }
        if(ok) out << "Case #" << tc << ": " << c << '\n';
    }

//    forn(i, 1000) cout << (rand() % 2 ? '+' : '-');


    return 0;
}


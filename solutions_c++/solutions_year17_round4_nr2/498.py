//This is getting accepted!
// I HATE BUG
// God Of The Bugs
// 12/11/2016
#include<bits/stdc++.h>

using namespace std;

#define ms(s, n) memset(s, n, sizeof(s))
#define FI first
#define SE second
#define pb push_back
#define mp make_pair
#define ll long long
#define sz(a) ((int)(a).size())
#define __builtin_popcount __builtin_popcounll
#define ld long double

typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<int, pii> ppi;

const double PI = acos(0) * 2;
const double EPS = 1e-8;
const ll MOD = 1e9 + 7;
const int MAXN = 1e5 + 5;
const int oo = 1e9;
const double foo = 1e30;

template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }
template<class T> int cntbit(T s) { return __builtin_popcounll(s);}
template<class T> T sqr(T x) { return x * x; }

inline void addmod(int& a, int val, int p = MOD) {if ((a = (a + val)) >= p) a -= p;}
inline void submod(int& a, int val, int p = MOD) {if ((a = (a - val)) < 0) a += p;}
inline int mult(int a, int b, int p = MOD) {return (ll) a * b % p;}

struct HopcroftKarp {
    static const int MAXV = 1e3 + 5;
    static const int MAXE = 1e6 + 5;
    int nx, ny, E, adj[MAXE], nxt[MAXE], lst[MAXV], cur[MAXV], lev[MAXV], que[MAXV], matx[MAXV], maty[MAXV];
    void init(int nx, int ny) {
        this->nx = nx, this->ny = ny;
        E = 0, fill_n(lst, nx + 1, -1);
        fill_n(matx, nx + 1, -1), fill_n(maty, ny + 1, -1);
    }
    void add(int x, int y) {
        adj[E] = y, nxt[E] = lst[x], lst[x] = E++;
    }
    int bfs() {
        int qsize = 0;
        for (int x = 1; x <= nx; x++) if (matx[x] != -1) lev[x] = -1;
        else {
            lev[x] = 0;
            que[qsize++] = x;
        }
        int found = 0;
        for (int i = 0; i < qsize; i++) {
            for (int x = que[i], e = lst[x]; e != -1; e = nxt[e]) {
                int y = adj[e];
                if (maty[y] == -1) found = 1;
                else if (lev[maty[y]] == -1) {
                    lev[maty[y]] = lev[x] + 1;
                    que[qsize++] = maty[y];
                }
            }
        }
        return found;
    }
    int dfs(int x) {
        for (int &e = cur[x]; e != -1; e = nxt[e]) {
            int y = adj[e];
            if (maty[y] == -1 || (lev[maty[y]] == lev[x] + 1 && dfs(maty[y]))) {
                matx[x] = y;
                maty[y] = x;
                return 1;
            }
        }
        return 0;
    }
    int maxmat() {
        int res = 0;
        while (bfs()) {
            for (int x = 1; x <= nx; x++) cur[x] = lst[x];
            for (int x = 1; x <= nx; x++) if (matx[x] == -1) res += dfs(x);
        }
        return res;
    }
} hopkarp;

int T, has[1010][1010], pos[1010], id[1010], seat[1010], play[1010];
vector<int> v[2];
int n, m, cus, tc;

int main() {
//#ifndef ONLINE_JUDGE
//    freopen("inp.txt", "r", stdin);
//    freopen("out.txt", "w", stdout);
//#endif

	cin >> T;
	while (T--) {
		cin >> n >> cus >> m;
		for (int i=0; i<cus; i++) for (int j=0; j<n; j++) has[i][j] = 0;
		for (int i=0; i<cus; i++) play[i] = 0;
		for (int i=0; i<n; i++) seat[i] = 0;
		for (int i=0; i<m; i++) {
			cin >> pos[i] >> id[i];
			pos[i]--;
			id[i]--;
			has[id[i]][pos[i]]++;
			play[id[i]]++;
			seat[pos[i]]++;
		}
		
		int ans1 = 0;
		for (int i=0; i<cus; i++) ans1 = max(ans1, play[i]);
		int l = ans1, r = m, find = -1, gg = -1;
		while (l <= r) {
			int mid = (l + r) >> 1;
			int now = 0;
			int ok = 1;
			int tot = 0;
			for (int i=0; i<n; i++) {
				if (seat[i] > mid) {
					int rem = seat[i] - mid;
					if (now < rem) {
						ok = 0;
						break;
					}
					else {
						now -= rem;
						tot += rem;
					}
				}
				else now += (mid - seat[i]);
			}
			if (ok) {
				find = mid;
				gg = tot;
				r = mid - 1;
			}
			else {
				l = mid + 1;
			}
		}
		
		cout << "Case #" << ++tc << ": " << find << " " << gg << '\n';
	}


}


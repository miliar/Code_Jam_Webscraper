#include <bits/stdc++.h>
 
#define gc getchar
#define ii(x) scanf(" %d", &x)
#define ill(x) scanf(" %lld", &x)
#define ll long long
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(),x.end()
#define fill(a,b) memset(a, b, sizeof(a))
#define rep(i,a,b) for(i=a;i<b;i++)
#define per(i,a,b) for(i=a;i>=b;i--)
#define pii pair<int, int>
 
using namespace std;
 
void in(int &x){
    register int c=gc();
    x=0;
    for(;(c<48||c>57);c=gc());
    for(;c>47&&c<58;c=gc()){x=(x<<1)+(x<<3)+c-48;}
}

const int N = 55, MAXVAL = 1e6 + 6;
int q[N][N], r[N], st[N][MAXVAL], vis[N][N];
std::multiset<int> ss[N];

void update(int ind, int l, int r){
	int i;
	rep(i, l, r + 1) st[ind][i]++;
}

int solve(int p){
	int i, j, ret = 0;
	rep(i, 1, MAXVAL){
		int cnt = 1e9;
		rep(j, 0, p){
			cnt = min(cnt, st[j][i]);
		}
		ret += cnt;
	}
	return ret;
}

int main()
{
	int t, i, j, n, p, tt;
	cin >> t; rep(tt, 1, t + 1){
		cin >> n >> p;
		rep(i, 0, n) ss[i].clear();
		fill(st, 0);
		fill(vis, 0);
		rep(i, 0, n) cin >> r[i];
		rep(i, 0, n){
			rep(j, 0, p){
				cin >> q[i][j];
				ss[i].insert(q[i][j]);
			}
			sort(q[i], q[i] + p);
		}
		int col, ret = 0;
		rep(col, 0, p){
			int val = q[0][col];
			double dl = val / (r[0] * 1.1), dr = val / (r[0] * 0.9);
			int l = ceil(dl), rr = floor(dr), mul;
			if(l > rr) continue;
			std::vector<int> v;
			v.clear();
			rep(i, 1, n){
				double minNeed = l * 0.9 * r[i], maxNeed = rr * 1.1 * r[i];
				int mini = ceil(minNeed), maxi = floor(maxNeed);
				auto it = ss[i].lower_bound(mini);
				if(it == ss[i].end()) break;
				int itval = *it;
				if(itval > maxNeed) break;
				v.pb(itval);
			}
			if(v.size() == n - 1){
				ret++;
				i = 1;
				for(int x : v){
					ss[i].erase(ss[i].find(x));
					i++;
				}
			}
			/*
			rep(mul, l, rr + 1){
				v.clear();
				rep(i, 1, n){
					rep(j, 0, p) if(!vis[i][j]){
						int val1 = q[i][j];
						double dl1 = val1 / (r[i] * 1.1), dr1 = val1 / (r[i] * 0.9);
						int l1 = ceil(dl1), r1 = floor(dr1);
						if(l1 <= mul && r1 >= mul){
							v.pb(mp(i, j));
							break;
						}
					}
				}
				if(v.size() == n - 1){
					ret++;
					for(pii p : v){
						int x = p.F, y = p.S;
						vis[x][y] = 1;
					}
					break;
				}
			}
			*/
		}
		cout << "Case #" << tt << ": " << ret << endl;
	}

	return 0;
}
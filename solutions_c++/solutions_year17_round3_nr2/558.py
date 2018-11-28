#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <utility>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

#define INF_LL (ll)1e18
#define INF (int)1e9
#define REP(i, n) for(int i = 0;i < (n);i++)
#define FOR(i, a, b) for(int i = (a);i < (b);i++)
#define all(x) x.begin(),x.end()
using ll = long long;
using PII = pair<int, int>;

template<typename A, typename B>inline void chmin(A &a, B b){if(a > b) a = b;}
template<typename A, typename B>inline void chmax(A &a, B b){if(a < b) a = b;}

class Union_find{
private:
	vector<int> par;
	vector<int> rank;
	int n;

public:
	Union_find(int a){
		n = a;
		for(int i = 0;i < n;i++){
			par.push_back(i);
			rank.push_back(0);
		}
	}

	int find(int x){
		if(par[x] == x){
			return x;
		}else{
			return par[x] = find(par[x]);
		}
	}

	void unite(int x, int y){
		x = find(x);
		y = find(y);
		if(x == y) return;

		if(rank[x] < rank[y]){
			par[x] = y;
		}else{
			par[y] = x;
			if(rank[x] == rank[y]) rank[x]++;
		}
	}

	bool same(int x, int y){
		return find(x) == find(y);
	}
};

class LazySegTree{
private:
	int n;
	vector<ll> node, lazy;
	vector<bool> lazyFlag;
public:
	LazySegTree(vector<ll> v){
		int sz = v.size();
		n = 1; while(n < sz) n *= 2;
		node.resize(2*n-1, 0);
		lazy.resize(2*n-1, 0);
		lazyFlag.resize(2*n-1, false);
		REP(i, sz) node[i+n-1] = v[i];
		for(int i = n-2;i >= 0;i--) node[i] = node[2*i+1]+node[2*i+2];
	}

	void eval(int k, int l, int r){
		if(lazyFlag[k]){
			node[k] += lazy[k] * (r-l);
			if(r-l > 1){
				lazy[2*k+1] += lazy[k];
				lazy[2*k+2] += lazy[k];
				lazyFlag[2*k+1] = lazyFlag[2*k+2] = true;
			}
			lazy[k] = 0;
			lazyFlag[k] = false;
		}
	}

	void add(int a, int b, ll x, int k=0, int l=0, int r=-1){
		if(r < 0) r = n;
		eval(k, l, r);
		if(b <= l || r <= a) return;

		if(a <= l && r <= b){
			lazy[k] += x;
			lazyFlag[k] = true;
			eval(k, l, r);
		}else{
			add(a, b, x, k*2+1, l, (l+r)/2);
			add(a, b, x, k*2+2, (l+r)/2, r);
			node[k] = node[k*2+1] + node[k*2+2];
		}
	}

	ll query(int a, int b, int k=0, int l=0, int r=-1){
		if(r < 0) r = n;
		eval(k, l, r);

		if(b <= l || r <= a) return 0;
		if(a <= l && r <= b) return node[k];

		return query(a, b, k*2+1, l, (l+r)/2) + query(a, b, k*2+2, (l+r)/2, r);
	}
};

class Bucket{
private:
	int n, bs, bn; // 要素数、バケットサイズ、バケットの数
	vector<ll> data;
	vector<ll> bucket, lazy;
	vector<bool> lazyFlag;
public:
	Bucket(vector<ll> v, int sz){
		data = v;
		n = v.size();
		bs = sz;
		bn = (n + bs - 1) / bs;
		data.resize(bn*bs, INF_LL);
		bucket.assign(bn, INF_LL);
		lazy.assign(bn, 0);
		lazyFlag.assign(bn, 0);
		REP(i, bn){
			ll minx = INF_LL;
			REP(j, bs){
				chmin(minx, data[i*bs+j]);
			}
			bucket[i] = minx;
		}
	}

	void eval(int k){
		if(lazyFlag[k]){
			lazyFlag[k] = false;
			FOR(i, bs*k, bs*(k+1)){
				data[i] = lazy[k];
			}
			lazy[k] = 0;
		}
	}

	void update(int s, int t, int x){
		REP(k, bn){
			int l = k*bs, r = (k+1)*bs;
			if(r <= s || t <= l) continue;
			if(s <= l && r <= t){
				lazyFlag[k] = true;
				bucket[k] = x;
				lazy[k] = x;
			}else{
				eval(k);
				FOR(i, max(s, l), min(t, r)){
					data[i] = x;
				}
				bucket[k] = INF_LL;
				FOR(i, l, r){
					chmin(bucket[k], data[i]);
				}
			}
		}
	}

	ll query(int s, int t){
		ll res = INF_LL;
		REP(k, bn){
			int l = k*bs, r = (k+1)*bs;
			if(r <= s || t <= l) continue;
			if(s <= l && r <= t){
				chmin(res, bucket[k]);
			}else{
				eval(k);
				FOR(i, max(s, l), min(t, r)){
					chmin(res, data[i]);
				}
			}
		}
		return res;
	}

};

using piii = pair<pair<int, int>, int>;
#define fst first
#define snd second

int main(void){
	cin.tie(0);
	ios::sync_with_stdio(false);
	int T;
	cin >> T;
	REP(t, T){
		int Ac, Aj;
		vector<piii> b;
		cin >> Ac >> Aj;
		int tim[2] = {}, tp[2] = {};
		REP(i, Ac){
			int c, d;
			cin >> c >> d;
			tim[0] += d-c;
			b.push_back({{c, d}, 0});
		}
		REP(i, Aj){
			int j, k;
			cin >> j >> k;
			tim[1] += k-j;
			b.push_back({{j, k}, 1});
		}
		sort(all(b));
		vector<PII> cost;
		int f = 0;
		int res = 1;
		tp[b[0].snd] += b[0].fst.fst;
		REP(i, b.size()){
			if(i < b.size()-1){
				if(b[i].snd == b[i+1].snd){
					tp[b[i].snd] += b[i+1].fst.fst-b[i].fst.snd;
				}else{
					f += b[i+1].fst.fst-b[i].fst.snd;
					res++;
				}
			}else{
				tp[b[i].snd] += 1440-b[i].fst.snd;
			}
		}
		int m;
		if(tp[0]+tim[0] < 720){
			m = 0;
		}else{
			m = 1;
		}
		if(tp[m]+tim[m]+f < 720){
			int l = 0;
			REP(i, b.size()){
				if(i < b.size()-1){
					if(b[i].snd == b[i+1].snd && b[i].snd != m){
						cost.push_back({b[i+1].fst.fst-b[i].fst.snd, 2});
					}
				}else{
					if(b[i].snd != m){
						cost.push_back({1440-b[i].fst.snd, 1});
					}
				}
			}
			if(b[0].snd != m){
				cost.push_back({b[0].fst.fst, 1});
			}
			int dp[300][2000] = {};
			REP(i, 300) REP(q, 2000) dp[i][q] = INF;
			dp[0][0] = 0;
			REP(i, cost.size()){
				REP(k, 1500){
					if(dp[i][k] != INF){
						REP(s, cost[i].fst+1){
							dp[i+1][k+s] = min(dp[i+1][k+s], dp[i][k] + cost[i].snd);
						}
					}
					dp[i+1][k] = min(dp[i+1][k], dp[i][k]);
				}
			}
			res += dp[cost.size()][720-(tp[m]+tim[m]+f)];
		}
		cout << "Case #" << t+1 << ": " << res-res%2 << endl;
	}
}

#include <bits/stdc++.h>
using namespace std;

namespace {
#define all(x) begin(x), end(x)
#define rall(x) rbegin(x), rend(x)
#define len(x) (int)((x).size())
#define X first
#define Y second

#define FOR(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))

#ifndef ONLINE_JUDGE
#include "debug.h"
#else
#define DEBUG(...) 
#define DEBUG_2D(...)
#endif  // ONLINE_JUDGE
  
typedef long long int ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
template<typename T> using minpq = priority_queue<T, vector<T>, greater<T>>;

ll expmod(ll a,ll b,ll mod) {ll res=1;a%=mod;for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
template<typename T> T sqr(const T& x) { return x*x; }
ll flog(const ll x) { return 63 - __builtin_clzll(x); }
template<typename T> void sort(T& t) { sort(all(t)); }
template<typename T> void undupe(vector<T>& v) { sort(v); v.erase(unique(all(v)), v.end()); }

struct _IOS { _IOS() { ios::sync_with_stdio(0); cin.tie(0); } } _IOS;
}

const ll MOD = 1000000009;
const ll INF = 1e15;
const double EPS = 1e-8;

int N, C, M;
vi P, B;
map<int,vi> held_by;

int min_promos(int rides) {
	


}

void solve_large() {
	cin >> N >> C >> M;
	P.resize(N);
	B.resize(N);
	FOR(i,0,N) cin >> P[i] >> B[i];
	
	held_by.clear();
	int atleast = 0;
	FOR(i,0,N) {
		held_by[B[i]].push_back(P[i]);
		atleast = max(atleast, (int)held_by[B[i]].size());
	}
	
	// binary search
	int lo = atleast - 1, hi = M;
	while (lo < hi - 1) {
		int mid = (lo + hi) / 2;
		if (min_promos(mid) == -1) lo = mid;
		else hi = mid;
	}
	
	// Answer
	cout << hi << ' ' << min_promos(hi) << '\n';
}

void solve_small() {
	cin >> N >> C >> M;
	P.resize(M);
	B.resize(M);
	FOR(i,0,M) cin >> P[i] >> B[i];

	vi p1, p2;
	FOR(i,0,M) {
		if (B[i] == 1) p1.push_back(P[i]);
		else p2.push_back(P[i]);
	}

	sort(p1.begin(), p1.end());
	sort(p2.begin(), p2.end());
	
	vi onseat1(N+1,0), onseat2(N+1,0);
	for (int x : p1) onseat1[x]++;
	for (int x : p2) onseat2[x]++;
	
	// # of tickets in common (excluding front seat)
	int most1 = 0, most2 = 0;
	for (int s=2; s<=N; s++) {
		if (onseat1[s] > onseat1[most1]) most1 = s;
		if (onseat2[s] > onseat2[most2]) most2 = s;
	}
	
	// Get answer
	int rides = 0;
	int promos = 0;
	
	int total1 = (int)p1.size();
	int total2 = (int)p2.size();
	
	// Give them front seat rides
	rides += onseat1[1] + onseat2[1];
	
	auto gmc = [&]() {
		int mc = 0;
		for (int s=2; s<=N; s++) {
			if (min(onseat1[s],onseat2[s]) > min(onseat1[mc],onseat2[mc])) mc = s;
		}
		return mc;
	};
	
	// Use common person 2
	for (int i=0; i<onseat1[1]; i++) {
		int mc = gmc();
		if (mc != 0) onseat2[mc]--;
	}
	
	// Use common person 1
	for (int i=0; i<onseat2[1]; i++) {
		int mc = gmc();
		if (mc != 0) onseat1[mc]--;
	}
	
	total1 -= rides;
	total2 -= rides;
	
	if (total1 < 0) total1 = 0;
	if (total2 < 0) total2 = 0;

	// Do promotions
	most1 = 0, most2 = 0;
	for (int s=2; s<=N; s++) {
		if (onseat1[s] > onseat1[most1]) most1 = s;
		if (onseat2[s] > onseat2[most2]) most2 = s;
	}
	
	if (most1 == most2 && onseat1[most1] + onseat2[most2] > max(total1,total2)) {
		promos += (onseat1[most1] + onseat2[most2]) - max(total1,total2);
	}
	
	// Do the rest of the rides
	rides += max(total1, total2);
	
	cout << rides << ' ' << promos << '\n';
}

int main() {
	int T=0; cin >> T;
	for (int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		solve_small();
		cerr << "Solved test case " << t << endl;
	}
}




















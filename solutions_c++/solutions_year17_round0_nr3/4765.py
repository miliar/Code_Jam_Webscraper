#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pii> vii;

#define Pq priority_queue
#define ri(x) scanf("%d", &x)
#define rii(x,y) scanf("%d%d", &x, &y)
#define FOR(i,S,E) for(int i=S; i<E; i++)
#define pb push_back
#define fst first
#define snd second

ll N, K;

struct Stall {
	ll l, r, idx;
	Stall (ll x, ll y, ll z) {
		l = x; r = y; idx = z;
	}
	Stall () {
		l = r = idx = -1;
	}
	ll min() const {return std::min(l,r);}
	ll max() const {return std::max(l,r);}
	bool operator<(const Stall &b) const {
		if (Stall::min() < b.Stall::min()) return true;
		if (min() > b.min()) return false;
		if (max() < b.max()) return true;
		if (max() > b.max()) return false;
		return (idx > b.idx);
	}
	void operator=(const int b) {
		l = idx = b; r = N/2;
	}
	void print() {
		printf("l: %lld\tr: %lld\tidx: %lld\n", l, r, idx);
	}
};
Pq< Stall > pq;

int main () {
	int T; ri(T);
	FOR(t,1,T+1) {
		scanf("%lld%lld", &N, &K);
		pq = priority_queue < Stall > ();
		Stall X;
		if (N%2) {
			X=N/2;
		}
		else {
			X=N/2-1;
		}
		pq.push(X);
		FOR(i,0,K) {
			X = pq.top();
			//X.print();
			pq.pop();
			ll l = X.l, r = X.r;
			if (!l && !r) continue;
			if (X.l%2) {
				Stall Y(l/2, l/2, X.idx - (l/2) - 1);
				pq.push(Y);
				/*
				printf("\t");
				Y.print();
				*/
			}
			else if (l){
				Stall Y((l/2)-1, l/2, X.idx - (l/2) - 1);
				pq.push(Y);
				/*
				printf("\t");
				Y.print();
				*/
			}

			if (X.r%2) {
				Stall Y(r/2, r/2, X.idx + (l/2) + 1);
				pq.push(Y);
				/*
				printf("\t");
				Y.print();
				*/
			}
			else if (r) {
				Stall Y((r/2)-1, r/2, X.idx +(r/2));
				pq.push(Y);
				/*
				printf("\t");
				Y.print();
				*/
			}
		}
		printf("Case #%d: %lld %lld\n", t, X.max(), X.min());
	}
}
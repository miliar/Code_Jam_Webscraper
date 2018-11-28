#include <bits/stdc++.h>

using namespace std;
const int MAXH = 102, MAXA = 40;

//#define debug(...) fprintf(stderr, __VA_ARGS__)
#define debug(...)

int HD, AD, HK, AK, B, D;

struct data {
	int hd, ad, hk, ak;	//ad and ak are not actual powers, it is how many upgrades

	data (int _hd, int _ad, int _hk, int _ak) : hd(_hd), ad(_ad), hk(_hk), ak(_ak) {}

	bool ddead() {
		return hd <= 0;
	}
	bool kdead() {
		return hk <= 0;
	}

	int getpd() {
		return AD + ad * B;
	}

	int getpk() {
		return max(0, AK - ak * D);
	}

	data dattack() {
		data res = *this;
		res.hk = max(0, res.hk - getpd());
		return res;
	}

	data dbuff() {
		data res = *this;
		if (B && getpd() < MAXA) {
			res.ad++;
		}
		return res;
	}

	data dcure() {
		data res = *this;
		res.hd = HD;
		return res;
	}

	data ddebuff() {
		data res = *this;
		if (D && getpk() > 0) {
			res.ak++;
		}
		return res;
	}

	//k attacks
	data kattack() {
		data res = *this;
		if (res.hk > 0) {
			res.hd = max(0, res.hd - getpk());
		}
		return res;
	}

	bool fit() {
		return ad < MAXH && ak < MAXH;
	}

	void print() {
		debug("hd = %d, ad = %d, hk = %d, ak = %d\n", hd, getpd(), hk, getpk());
	}
};

vector<data> vvis;	//THIS IS HOW MUCH YOU HAVE VISITED
int dist[MAXH][MAXH][MAXH][MAXH];

int &getdist (data d) {
	return dist[d.hd][d.ad][d.hk][d.ak];
}

void clrvis() {
	for (data d : vvis) {
		getdist(d) = -1;
	}
	vvis.clear();
}

int go() {
	debug("-------new test case-----------------\n");
	scanf("%d %d %d %d %d %d", &HD, &AD, &HK, &AK, &B, &D);
	vvis.clear();
	queue<data> que;
	que.push(data(HD, 0, HK, 0));
	vvis.push_back(que.front());
	getdist(que.front()) = 0;

	while (!que.empty()) {
		data fro = que.front();
		debug("AT THE FRONT, WITH DIST %d: ", getdist(fro)); fro.print();

		int ndist = getdist(fro) + 1;
		que.pop();
		//do every action
		for (data d : {fro.dattack(), fro.dbuff(), fro.dcure(), fro.ddebuff()}) {
			//are YOU still alive?
			//debug("CONSIDER "); d.print();
			/*
			debug("aite ad is %d\n", d.ad);
			*/

			d = d.kattack();
			if (d.kdead()) {
				clrvis();
				return ndist;
			}

			//debug("after attack, "); d.print();
			assert(d.fit());	//I HOPE
			if (d.fit() && !d.ddead()) {
				int &ref = getdist(d);
				if (ref == -1) {
					//debug("new action: "); d.print();
					ref = ndist;
					que.push(d);
					vvis.push_back(d);
				}
			}
		}
	}

	clrvis();
	return -1;
}

int main() {
	int nq;
	scanf("%d", &nq);

	memset(dist, -1, sizeof(dist));
	for (int cas = 1; cas <= nq; cas++) {
		fprintf(stderr, "Starting case %d\n", cas);
		printf("Case #%d: ", cas);
		int ans = go();
		if (ans == -1) {
			puts("IMPOSSIBLE");
		} else {
			printf("%d\n", ans);
		}
		fprintf(stderr, "Case %d finished\n", cas);
	}
}

#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

int n, k;
pair<int, int> pan[1100];

void read() {
	scanf("%d %d", &n, &k);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &pan[i].first, &pan[i].second);
	}
}

double pi = 2*acos(0);
double lat(pii p) {
	return 2 * pi * (double)p.first * (double)p.second;
}

void solve() {
	sort(pan, pan+n, [](pii a, pii b) {
		return lat(a) > lat(b);
	});

	double best = 0;
	for (int i = 0; i < n; i++) {
		double th = lat(pan[i]) + pi * (double)pan[i].first * (double)pan[i].first;
		int av = k-1;
		for (int j = 0; j < n && av; j++) if (j != i) {
			if (pan[i].first >= pan[j].first) {
				th += lat(pan[j]);
				av--;
			} 
		}
		best = max(th, best);
	}

	printf("%.15f\n", best);
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
		}
	}
}
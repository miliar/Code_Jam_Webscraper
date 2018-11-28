#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

long long n, k;

void read() {
	scanf("%lld %lld", &n, &k);
}

void solve() {
	map<long long, long long> spaces;
	spaces[-n] = 1;

	while (1) {
		long long f = -spaces.begin()->first;
		long long occ = spaces.begin()->second;

		if (occ >= k) {
			printf("%lld %lld\n", f/2, (f-1)/2);
			return;
		}

		spaces[-(f/2)] += occ;
		spaces[-((f-1)/2)] += occ;
		k -= occ;
		spaces.erase(spaces.begin());
	}
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
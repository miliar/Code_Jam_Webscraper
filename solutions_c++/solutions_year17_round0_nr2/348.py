#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

long long n;
int d[20];

void read() {
	scanf("%lld", &n);
}

void solve() {
	int len;
	long long p10 = 10;
	for (len = 1; p10 <= n; len++, p10 *= 10);

	long long p = 0;
	p10 /= 10;

	for (int i = len; i > 0; i--) {
		for (int d = 9; d >= 0; d--) {
			long long t = p;
			long long m10 = p10;

			for (int j = 0; j < i; j++) {
				t += m10 * d;
				m10 /= 10;
			}

			if (t <= n) {
				p += p10 * d;
				p10 /= 10;
				break;
			}
		}
	}

	printf("%lld\n", p);
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
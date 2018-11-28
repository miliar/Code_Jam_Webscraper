#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

int n, k;
char s[110000];

void read() {
	scanf("%s %d", &s, &k);
}

char flip(char c) {
	if (c == '+') return '-';
	return '+';
}

void solve() {
	n = strlen(s);
	int cnt = 0;
	for (int i = 0; i + k - 1 < n; i++) {
		if (s[i] == '-') {
			cnt++;
			for (int j = i; j < i+k; j++) s[j] = flip(s[j]);
		}
	}

	for (int i = 0; i < n; i++) {
		if (s[i] == '-') {
			printf("IMPOSSIBLE\n");
			return;
		}
	}

	printf("%d\n", cnt);
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
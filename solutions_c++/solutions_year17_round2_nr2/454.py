#include <bits/stdc++.h>

#define eb emplace_back
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF 0x3f3f3f3f

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const int N = 100010;

bool solve (int r, int y, int b) {
	int sum = r + y + b;
	if (y > r + b or r > y + b or b > r + y) return false;
	int qtd[3] = {r, y, b};
	char c[3] = {'R', 'Y', 'B'};
	int last = 4;
	int primeiro = -1;
	while (sum--) {
		int maior = -1, idx = -1;
		for (int i = 0; i < 3; i++) {
			if (qtd[i] > maior and i != last) {
				maior = qtd[i];
				idx = i;
			}
			if (i == primeiro and qtd[i] == maior and i != last) {
				maior = qtd[i];
				idx = i;
			}
		}
		if (primeiro == -1) primeiro = idx;
		last = idx;
		qtd[idx]--;
		printf("%c", c[idx]);
	}
	assert(primeiro!=last);
	printf("\n");
	return true;
}
int main (void) {
	int t; scanf("%d", &t);
	while (t--) {
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		static int ca = 1;
		printf("Case #%d: ", ca++);
		if (!solve(r, y, b)) {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}


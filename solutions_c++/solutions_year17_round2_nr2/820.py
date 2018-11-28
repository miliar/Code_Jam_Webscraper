//writted by dnvtmf
#include <bits/stdc++.h>
#define INF 1000000007
#define FI first
#define SE second
#define PB push_back
#define VI vector<int>
#define MP make_pair
#define FOR(x, st, ed) for(auto x = (st); x < (ed); ++x)
#define FORE(x, st, ed) for(auto x = (st); x <= (ed); ++x)
#define CLR(arr, val) memset(arr, val, sizeof(arr))
#define INFO(tag, st, ed, x) printf("%s: ", tag); \
	FOR(_i, st, ed) cout << x[_i] << ' '; puts("");
using namespace std;
typedef long long LL;
typedef pair <int, int> PII;
const int NUM = 100010;
string ans[1100];
int N, R, O, Y, G, B, V;
int sum;
void place_first(char a, char b, int x, int X) {
	int pos = 0;
	for(int i = 0; i < x; ++i, pos += 2) {
		ans[pos] = a;
		if(i == 0) {
			while(X--) {
				ans[pos] += b;
				ans[pos] += a;
			}
		}
	}
}
void place_second(char a, char b, int x, int X) {
	int pos = sum - 1;
	for(int i = 0; i < x; ++i, pos -= 2) {
		if(ans[pos] != "")
			--pos;
		ans[pos] = a;
		if(i == 0) {
			while(X--) {
				ans[pos] += b;
				ans[pos] += a;
			}
		}
	}
}
void place_last(char a, char b, int x, int X) {
	int pos = 0;
	for(int i = 0; i < x; ++i) {
		while(ans[pos] != "")
			++pos;
		ans[pos] = a;
		if(i == 0) {
			while(X--) {
				ans[pos] += b;
				ans[pos] += a;
			}
		}
	}
}
char c1[3], c2[3];
int  x1[3], x2[3], id[3];
bool cmp(int a, int b) {
	return x1[a] > x1[b];
}
bool solve() {
	scanf("%d %d %d %d %d %d %d\n", &N, &R, &O, &Y, &G, &B, &V);
	int b = B, r = R, y = Y;
	if(O) {
		if(B < O)
			return false;
		if(B == O) {
			if(N == B + O) {
				for(int i = 0; i < B; ++i)
					printf("BO");
				puts("");
				return true;
			}
			else
				return false;
		}
		b = B - O;
	}
	if(G) {
		if(R < G)
			return false;
		if(G == R) {
			if(N == G + R) {
				for(int i = 0; i < G; ++i)
					printf("GR");
				puts("");
				return true;
			}
			else
				return false;
		}
		r = R - G;
	}
	if(V) {
		if(Y < V)
			return false;
		if(Y == V) {
			if(N == Y + V) {
				for(int i = 0; i < Y; ++i)
					printf("YV");
				puts("");
				return true;
			}
			else
				return false;
		}
		y = Y - V;
	}
	sum = y + r + b;
	if(y + y > sum || r + r > sum || b + b > sum)
		return false;
	for(int i = 0; i < sum; i++)
		ans[i] = "";
	id[0] = 0;
	c1[0] = 'B';
	c2[0] = 'O';
	x1[0] = b;
	x2[0] = O;
	id[1] = 1;
	c1[1] = 'R';
	c2[1] = 'G';
	x1[1] = r;
	x2[1] = G;
	id[2] = 2;
	c1[2] = 'Y';
	c2[2] = 'V';
	x1[2] = y;
	x2[2] = V;
	sort(id, id + 3, cmp);
	place_first(c1[id[0]], c2[id[0]], x1[id[0]], x2[id[0]]);
	place_second(c1[id[1]], c2[id[1]], x1[id[1]], x2[id[1]]);
	place_last(c1[id[2]], c2[id[2]], x1[id[2]], x2[id[2]]);
	for(int i = 0; i < sum; ++i)
		cout << ans[i];
	cout << endl;
	return true;
}
int main() {
#ifdef ACM_TEST
	freopen("in.txt", "r", stdin);
#endif
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++cas) {
		printf("Case #%d: ", cas);
		if(!solve())
			puts("IMPOSSIBLE");
	}
	return 0;
}

#include<cstdio>
#include<cassert>
#include<cstring>
#include<map>
#include<set>
#include<time.h>
#include<algorithm>
#include<stack>
#include<queue>
#include<utility>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>
#include <limits>

using namespace std;

typedef pair <int, int> ii;
const long long INF = 1e9 + 7;
const long long INF9 = 1e9 + 9;

long long gcd(long long b, long long s){
	return (s != 0) ? gcd(s, b%s) : b;
}

long long pw(long long a, long long b, long long c) {
	if (b == 0) return 1;
	else if (b == 1) return a%c;
	else {
		long long A = pw(a, b / 2, c);
		A = (A*A) % c;
		if (b & 1) A = (A*a) % c;
		return A;
	}

}

const int N = 1002;

typedef pair <int, char> ic;
ic a[3];
string p[N];

vector <string> color[3];

void large() {
	int r = color[0].size(), y = color[1].size(), b = color[2].size();
	a[0] = ic(r, 0);
	a[1] = ic(y, 1);
	a[2] = ic(b, 2);

	sort(a, a + 3);

	bool ok = 1;
	if (a[0].first + a[1].first < a[2].first)
		ok = 0;
	if (a[0].first + a[1].first == 0) 
		ok = 0;
	
	int n = r + y + b;

	if (ok) {
		for (int i = 0; i < n; i += 2) {
			if (a[2].first > 0) {
				--a[2].first;
				p[i] = color[a[2].second][a[2].first];
			}
			else if (a[1].first > 0) {
				--a[1].first;
				p[i] = color[a[1].second][a[1].first];
			}
		}
		for (int i = 1; i < n; i += 2) {
			if (a[1].first > 0) {
				--a[1].first;
				p[i] = color[a[1].second][a[1].first];
			}
			else if (a[0].first > 0) {
				--a[0].first;
				p[i] = color[a[0].second][a[0].first];
			}
		}

		for (int i = 0; i < n; i++)
			printf("%s", p[i].c_str());
		puts("");
	}
	else
		puts("IMPOSSIBLE");
}

void solve() {

	int n;
	scanf("%d", &n);
	int r, o, y, g, b, v;
	scanf("%d %d %d %d %d %d", &r, &o, &y, &g, &b, &v);
	bool ok = 1;
	if (o && !(o + 1 <= b)) ok = 0;
	if (g && !(g + 1 <= r)) ok = 0;
	if (v && !(v + 1 <= y)) ok = 0;
	if ( ok ) {

		color[0].clear();
		color[1].clear();
		color[2].clear();

		string t = "";

		if (o) {
			for (int i = 0; i < o; i++) {
				t += 'B';
				t += 'O';
			}
			t += 'B';
			color[0].push_back(t);
			for (int i = 0; i < b - (o + 1); i++)
				color[0].push_back("B");
		}
		else {
			for (int i = 0; i < b; i++)
				color[0].push_back("B");
		}
		if (g) {
			t = "";

			for (int i = 0; i < g; i++) {
				t += 'R';
				t += 'G';
			}
			t += 'R';
			color[1].push_back(t);
			for (int i = 0; i < r - (g + 1); i++)
				color[1].push_back("R");
		}
		else {
			for (int i = 0; i < r; i++)
				color[1].push_back("R");
		}
		

		if (v) {
			t = "";
			for (int i = 0; i < v; i++) {
				t += 'Y';
				t += 'V';
			}
			t += 'Y';
			color[2].push_back(t);

			for (int i = 0; i < y - (v + 1); i++)
				color[2].push_back("Y");
		}else
			for(int i=0; i<y; i++)
				color[2].push_back("Y");
		
		
		large();
		
	}
	else {
		int n = r + o + y + g + b + v;

		if (n % 2 == 0) {
			if (b + o == n && b == o) {
				for (int i = 0; i < n / 2; i++)
					printf("BO");
			}
			else if (r + g == n && r == g) {
				for (int i = 0; i < n / 2; i++)
					printf("RG");
			}
			else if (y + v == n && y == v) {
				for (int i = 0; i < n / 2; i++)
					printf("YV");
			}
			else {
				printf("IMPOSSIBLE");
			}
			puts("");
		}else
			puts("IMPOSSIBLE");
	}
	
	

}


int main() {
	//freopen("in.txt", "r", stdin);
	//freopen("out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int R = 1; R <= T; R++) {
		printf("Case #%d: ", R);
		solve();
	}

}
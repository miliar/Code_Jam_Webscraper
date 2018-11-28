#include <iostream>
#include <string>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
using namespace std;

#define ll long long
#define mx 100

//int conn[mx+2][mx+2], chk[mx+2];

int main() {
	/*int a,b;
	scanf("%d %d", &a, &b);
	queue<int> q;

	q.push(1);
	while (q.size()) {

	}*/

	freopen("A-large.in", "r", stdin);
	freopen("A-large-output.txt", "w", stdout);

	int t, k;
	string s;

	scanf("%d", &t);
	for (int a = 1; a <= t;a++) {
		cin >> s >> k;
		int cnt = 0;
		int len = s.length();
		for (int i = 0; i <= len-k; i++) {
			if (s[i] == '-') {
				cnt++;
				for (int j = i; j < i + k; j++) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
		}
		bool chk = false;
		for (int i = 0; i < len; i++)
			if (s[i] == '-')
				chk = true;
		printf("Case #%d: ", a);
		if (chk)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", cnt);
	}

}
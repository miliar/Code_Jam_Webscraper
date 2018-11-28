#include <bits/stdc++.h>
using namespace std;

int tc;
char s[] = "ROYGBV";
bool cmp(queue<string> &a, queue<string> &b) {
	return a.size() < b.size();
}

int N, A[300];

int main() {
	scanf("%d", &tc);
	for (int tt=1; tt<=tc; ++tt) {
		printf("Case #%d: ", tt);

		scanf("%d", &N);
		memset(A, 0, sizeof(A));
		queue<string> q[3];

		for (int i=0; i<6; ++i)
			scanf("%d", &A[s[i]]);

		bool ans = true;
		int danger = 0;
		string ss;
		for (int i=0; i<6; i+=2) {
			int opp = A[s[(i+3)%6]];
			if (opp == 0 && A[s[i]] == 0) continue;

			if (A[s[i]] < opp) {
				ans = false;
				break;
			}
			else if (A[s[i]] == opp) {
				++danger;
				for (int j=0; j<opp; ++j) {
					ss += s[(i+3)%6];
					ss += s[i];
				}
			}
			else if (opp != 0) {
				A[s[i]] -= opp+1;
				string t;
				t += s[i];
				for (int j=0; j<opp; ++j) {
					t += s[(i+3)%6];
					t += s[i];
				}
				q[i/2].push(t);
				for (int j=0; j<A[s[i]]; ++j)
					q[i/2].push(string(1, s[i]));
			}
			else if (opp == 0) {
				for (int j=0; j<A[s[i]]; ++j)
					q[i/2].push(string(1, s[i]));
			}
		}

		sort(q, q+3, cmp);
		if (danger == 1 && ss.size() == N) {
			cout << ss << endl;
			continue;
		}
		else if (danger != 0 || q[2].size() > q[0].size() + q[1].size())
			ans = false;

		if (ans) {
			string t;
			int a = q[0].size(), b = q[1].size();
			int x = a+b-q[2].size();
			for (int i=0; i<a-x; ++i) {
				t += q[0].front(); q[0].pop();
				t += q[2].front(); q[2].pop();
			}
			for (int i=0; i<b-x; ++i) {
				t += q[1].front(); q[1].pop();
				t += q[2].front(); q[2].pop();
			}
			for (int i=0; i<x; ++i) {
				t += q[0].front(); q[0].pop();
				t += q[1].front(); q[1].pop();
				t += q[2].front(); q[2].pop();
			}
			cout << t;
				
		}
		else 
			printf("IMPOSSIBLE");
		puts("");



	}


	return 0;
}

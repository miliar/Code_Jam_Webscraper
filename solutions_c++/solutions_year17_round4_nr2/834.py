#include <map>
#include <cmath>
#include <ctime>
#include <queue>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const string filename = "B-small-attempt0";
int Test, N, M, C, P[1111], B[1111];
vector<int> X, Y;
bool G[1111][1111], V[1111];
int Match[1111];

bool find(int i)
{
	for (int j = 0; j < M; j ++)
	if (G[i][j] && !V[j]) {
		V[j] = true;
		if (Match[j] == -1 || find(Match[j])) {
			Match[j] = i;
			return true;
		}
	}
	return false;
}

int solve(vector<int> A, vector<int> B)
{
	memset(G, 0, sizeof(G));
	for (int i = 0; i < A.size(); i ++) {
		for (int j = 0; j < B.size(); j ++)
		if (A[i] != B[j]) {
			G[i][j] = true;
		}
	}
	memset(Match, -1, sizeof(Match));
	M = B.size();
	int cnt = A.size();
	for (int i = 0; i < A.size(); i ++) {
		memset(V, false, sizeof(V));
		if (find(i)) cnt --;
	}
	return cnt;
}

int main(int argv, char* argc[])
{
	freopen((filename+".in").c_str(), "r", stdin);
	freopen((filename+".out").c_str(), "w", stdout);
	scanf("%d", &Test);
	for (int Case = 1; Case <= Test; Case ++) {
		scanf("%d%d%d", &N, &C, &M);
		X.clear();
		Y.clear();
		int CNT_1 = 0;
		for (int i = 0; i < M; i ++) {
			scanf("%d%d", &P[i], &B[i]);
			if (B[i] == 1) X.push_back(P[i]);
				else Y.push_back(P[i]);
			if (P[i] == 1) CNT_1 ++;
		}
		sort(X.begin(), X.end());
		sort(Y.begin(), Y.end());
		int CNT = max(X.size(), Y.size());
		int ret = 0;
		if (X.size() <= Y.size()) ret = solve(X, Y);
			else ret = solve(Y, X);
		if (CNT_1 >= CNT) {
			CNT = CNT_1;
			ret = 0;
		}
		printf("Case #%d: %d %d\n", Case, CNT, ret);
	}
	return 0;
}

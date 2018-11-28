#include<cstdio>
#include<cstring>
#include<queue>
using namespace std;
int A[10];
int D[20000001][4];
int N, P;
int C = 101;
vector<int> get(int x) {
	vector<int> v;
	v.push_back(x / (C * C));
	x %= (C * C);
	v.push_back(x / C);
	x %= C;
	v.push_back(x);
	return v;
}
int get(vector<int> v) {
	int s = 0;
	for(int i = 0, x = C * C; i < v.size(); i++, x /= C)
	{
		s += x * v[i];
	}
	return s;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %d", &N, &P);
		memset(A, 0, sizeof(A));
		for(int i = 1; i <= N; i++)
		{
			int x;
			scanf("%d", &x);
			A[x % P]++;
		}
		int n = P - 1;
		memset(D, 0, sizeof(D));
		vector<int> final;
		for(int i = 0; i < P; i++) final.push_back(A[i]);
		int Final = get(final);
		for(int i = 0; i < Final; i++)
		{
			vector<int> v = get(i);
			bool flag = false;
			for(int j = 0; j < P; j++) {
				if(A[j] < v[j]) flag = true;
			}
			if(flag) continue;
			for(int j = 0; j < P; j++)
			{
				if (A[j] != v[j]) {
					v[j]++;
					int g = get(v);
					for(int k = 0; k < P; k++) {
						int h = (j + k) % P;
						D[g][h] = max(D[g][h], D[i][k] + (k == 0 ? 1 : 0));
					}
					v[j]--;
				}
			}
		}
		int Ans = -1;
		for(int i = 0; i < P; i++) Ans = max(Ans, D[Final][i]);
		printf("Case #%d: %d\n", t, Ans);
	}
}
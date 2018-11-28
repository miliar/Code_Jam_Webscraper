#include<cstdio>
#include<algorithm>
#include<vector>
#include<cmath>
using namespace std;
struct LIST
{
	int idx;
	int s, e;
	LIST(int idx_, int s_, int e_) : idx(idx_), s(s_), e(e_)
	{}
	bool operator < (LIST& rhs) const {
		if(s != rhs.s) return s < rhs.s;
		if(e != rhs.e) return e < rhs.e;
		return idx < rhs.idx;
	}
};
int A[51];
vector<LIST> list[51];
int P[51];
int N, M;
bool intersect()
{
	int S = list[1][P[1]].s;
	int E = list[1][P[1]].e;
	for(int i = 2; i <= N; i++)
	{
		int s = list[i][P[i]].s;
		int e = list[i][P[i]].e;
		S = max(S, s);
		E = min(E, e);
	}
	return S <= E;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%d %d", &N, &M);
		for(int i = 1; i <= N; i++) scanf("%d", &A[i]);
		for(int i = 1; i <= N; i++)
		{
			list[i].clear();
			for(int j = 1; j <= M; j++)
			{
				double x;
				scanf("%lf", &x);
				list[i].push_back(LIST(j, ceil(x / 1.1 / A[i]), floor(x / 0.9 / A[i])));
			}
			sort(list[i].begin(), list[i].end());
			P[i] = 0;
		}
		int Ans = 0;
		while(true)
		{
			bool flag = false;
			for(int i = 1; i <= N; i++) if(P[i] == M) flag = true;
			if(flag) break;
			if(intersect())
			{
				Ans++;
				for(int i = 1; i <= N; i++) P[i]++;
				continue;
			}
			int Min = list[1][P[1]].s, x = 1;
			for(int i = 2; i <= N; i++)
			{
				if(Min > list[i][P[i]].s)
				{
					Min = list[i][P[i]].s;
					x = i;
				}
			}
			P[x]++;
		}
		printf("Case #%d: %d\n", t, Ans);
	}
}
#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long LL;
#define N 1000 + 5
#define K 100

const char pi[50] = "3141592653589793238462643383279502";
int Case, n, k, R[N], H[N], Ord[N];
LL ans, A[N], T[N];

struct Big
{
	LL num[K];
	Big (LL x = 0)
	{
		num[0] = x;
		for (int i = 1; i < K; i ++) num[i] = 0;
	}
	Big (const char *ch)
	{
		for (int i = 0; i < K; i ++) num[i] = 0;
		for (int i = 0; *(ch + i); i ++)
			num[i] = pi[i] - '0';
	}
	Big operator * (Big x)
	{
		Big res = Big(0LL);
		for (int i = 0; i < K; i ++)
			for (int j = 0; i + j < K; j ++)
				res.num[i + j] += num[i] * x.num[j];
		for (int i = K - 1; i; i --)
		{
			res.num[i - 1] += res.num[i] / 10;
			res.num[i] %= 10;
		}
		return res;
	}
	void out(int w)
	{
		printf("%lld.", num[0]);
		for (int i = 1; i <= w; i ++)
			printf("%lld", num[i]);
		puts("");
	}
}Ans, Pi;

bool cmp(int u, int v)
{
	return R[u] < R[v];
}

void Add(LL x)
{
	int t = k - 1;
	for (; t && T[t] < x; t --) ;
	t ++;
	if (t >= k) return ;
	for (int i = k - 1; i > t; i --) T[i] = T[i - 1];
	T[t] = x, T[0] = 0;
	for (int i = 1; i < k; i ++) T[0] += T[i];
}

int main()
{
	Pi = Big(pi);
	scanf("%d", &Case);
	for (int Test = 1; Test <= Case; Test ++)
	{
		scanf("%d%d", &n, &k);
		for (int i = 1; i <= n; i ++)
		{
			scanf("%d%d", R + i, H + i);
			Ord[i] = i, A[i] = 2LL * R[i] * H[i];
		}
		sort(Ord + 1, Ord + n + 1, cmp);
		for (int i = 0; i <= k; i ++) T[i] = 0;
		for (int i = 1; i < k; i ++) Add(A[Ord[i]]);
		ans = 0;
		for (int i = k; i <= n; i ++)
		{
			LL tmp = T[0] + A[Ord[i]] + 1LL * R[Ord[i]] * R[Ord[i]];
			ans = max(ans, tmp);
			Add(A[Ord[i]]);
		}
		printf("Case #%d: ", Test);
		Ans = Big(ans);
		Ans = Ans * Pi;
		Ans.out(10);
	}
	return 0;
}

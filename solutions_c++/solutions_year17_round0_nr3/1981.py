#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

/*
세그먼트 트리 2개를 활용하자. 하나는 max 값을 구하고, 하나는 min 값을 구하게 하자.
i번째 리프 노드의 값은 사람이 없으면 0/INF, 있으면 i로 두자.
이제 새롭게 한 사람을 배정해야 한다고 하자.
모든 비어 있는 자리에 대해서 다음을 수행하자. 이번 자리가 i번째 자리일 때
[1, i-1] 구간의 max tree 값을 구하고, [i+1, n+2] 구간의 min tree의 값을 구하자.
그럼 가장 가까운 왼쪽 / 오른쪽 사람의 위치를 알 수 있다.
이제 policy에 맞는 값을 계속 갱신하면서 가지고 있자. 그 뒤 이번에 뽑힌 값에 대해 seg tree를 업데이트하면 끗

*/
struct twe {
	long long pos, mini, maxi;
};

int threshold = 5;

pair<long long, long long> naive(long long n, long long k)
{
	if (n == k) return{ 0LL, 0LL };
	if (k == 0) puts("k is 0");
	vector<int> arr; twe ans;
	arr.push_back(1); for (int i = 0; i < n; i++)arr.push_back(0);
	arr.push_back(1);
	int cnt = 1;
	while (k--)
	{
		ans.mini = ans.maxi = -1; ans.pos = n+1;
		for (int i = 1; i <= n; i++)
		{
			if (arr[i] == 1) continue;
			int leftnear = 0, rightnear = n + 1;
			for (int j = 0; j < i; j++) if (arr[j] == 1) leftnear = j;
			for (int j = n + 1; j > i; j--)if (arr[j] == 1) rightnear = j;
			int mini = min(i - leftnear - 1, rightnear - i - 1);
			int maxi = max(i - leftnear - 1, rightnear - i - 1);
			if (mini > ans.mini) {
				ans = {i, mini, maxi};
			}
			else if (mini == ans.mini && maxi > ans.maxi) {
				ans = { i, mini, maxi };
			}
			else if (mini == ans.mini && maxi == ans.maxi && i < ans.pos) {
				ans = { i, mini, maxi };
			}
		}
		arr[ans.pos] = 1;
		//printf("%dth : %lld %lld\n", cnt, ans.maxi, ans.mini);
		cnt++;
	}
	return{ans.maxi, ans.mini};
}

pair<long long, long long> getAnswer(long long n, long long k)
{
	if (k < threshold) return naive(n, k);
	printf("getanswer %lld %lld\n", n, k);
	if (n == k) return{ 0LL, 0LL };
	if (k == 1) {
		if (n % 2 == 1)
			return{ (n - 1) / 2, (n - 1) / 2 };
		else
			return{ n / 2, n / 2 - 1 };
	}
	long long lower = 1, upper = 1, nextk;
	while (lower * 2 <= k) lower *= 2;
	while (upper <= k) upper *= 2;
	if (k - lower < lower / 2) // left part
	{
		if (n % 2 == 1)//n is odd
		{
			nextk = k - lower / 2;
			return getAnswer((n - 1) / 2, nextk);
		}
		else//n is even
		{
			nextk = k - lower / 2;
			return getAnswer(n / 2, nextk);
		}
	}
	else
	{
		nextk = k - lower;
		if (n % 2 == 1) return getAnswer((n - 1) /2, nextk);
		else return getAnswer(n / 2, nextk);
	}
}

pair<long long, long long> real(long long n, long long k)
{
	long long lower = 1; int cnt = 1;
	long long big = n / 2;
	long long bigcnt;//total cnt == lower
	while (lower * 2 <= k)//lower == 2^cnt
	{
		lower *= 2;
		cnt++;
		big /= 2;
	}
	//bigcnt * big + (2*lower - bigcnt) * (big - 1) + 2*lower - 1 == n
	//2*lower*big + bigcnt - 1 == n
	//bigcnt == n + 1 - 2 * big*lower
	bigcnt = n + 1 - 2 * big * lower;
	//printf("n %lld k %lld big %lld bigcnt %lld lower %lld\n", n, k, big, bigcnt, lower);

	if (bigcnt <= lower)
	{
		if (k - lower < bigcnt) return{ big, big - 1 };
		else return{ big - 1,big - 1 };
	}
	else
	{
		if (k - lower < bigcnt - lower) return{ big, big };
		else return{ big ,big - 1 };
	}
}

void solve(int casen)
{
	long long n, k; scanf("%lld %lld", &n, &k);
	auto ans = real(n, k);
	printf("Case #%d: %lld %lld\n", casen, ans.first, ans.second);
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
	/*for (long long n = 1; n <= 1000; n++)
	{
		printf("n %lld\n", n);
		for (long long k = 1; k <= n; k++)
		{
			auto a = real(n, k);//naive(n, k);
			auto b = naive(n, k);
			if (a != b)printf("n %lld k %lld (%lld, %lld) , (%lld, %lld)\n", n, k, a.first, a.second, b.first, b.second);
		}
	}*/
}
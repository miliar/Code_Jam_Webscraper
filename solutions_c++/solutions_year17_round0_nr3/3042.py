#include <cstdio>
#include <map>
#define CODE "C-large"
typedef long long lld;
std::map<lld,lld> heap;
std::map<lld,lld>::reverse_iterator maxLen;
lld cnt, K, N, P;
int T;

void fission()
{	// Split all Segments
	P = maxLen->first;
	maxLen = heap.rbegin();
	heap[ maxLen->first      / 2] += maxLen->second;
	heap[(maxLen->first - 1) / 2] += maxLen->second;
	cnt += maxLen->second;
	heap.erase(maxLen->first); // Pop Key
}

int main()
{
	freopen(CODE ".in", "r", stdin);
	freopen(CODE ".out", "w", stdout);
	scanf("%d", &T);
	for(int _ = 1; _ <= T; ++_)
	{
		scanf(" %lld%lld", &N, &K);
		heap.clear();
		heap[N] = 1LL;
		maxLen = heap.rbegin();
		P = maxLen->first;
		cnt = 0LL; // People Count
		while(K > cnt) fission();
		printf("Case #%d: %lld %lld\n", _, P / 2, (P - 1) / 2);
	}
	return 0;
}
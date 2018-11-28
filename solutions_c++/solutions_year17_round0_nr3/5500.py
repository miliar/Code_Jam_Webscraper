#include<cstdio>
#include<cstring>
#include<algorithm>
using std::min;
using std::max;
const int maxn = 1000000;
const int INF = 0x7fffffff;

int n, k, p, B[maxn];

struct foo {
	int l, r;
	int mini() { return min(l, r); }
	int maxi() { return max(l, r); }
}B_t[maxn];

int search()
{
	memset(B_t, 0, sizeof(B_t));
	for(int i = 0; i < n; i++) if(!B[i]) {
		for(int j = i-1; j >= 0; j--) if(!B[j]) B_t[i].l++; else break;
		for(int j = i+1; j < n; j++) if(!B[j]) B_t[i].r++; else break;
	}
	/*
	for(int i = 0; i < n; i++) printf("%d %d, ", B_t[i].l, B_t[i].r);
	putchar('\n');
	*/

	int max_of_mini = 0, maxi = 0, maxi_p;
	for(int i = 0; i < n; i++) if(B_t[i].mini() > max_of_mini && !B[i]) max_of_mini = B_t[i].mini();
	for(int i = 0; i < n; i++) if(B_t[i].mini() == max_of_mini && B_t[i].maxi() > maxi && !B[i]) {
		maxi = B_t[i].maxi();
		maxi_p = i;
	}

	return maxi_p;
}

int main()
{
	int T, kase = 0;
	scanf("%d", &T);

	while(T--) {
		memset(B, 0, sizeof(B));
		memset(B_t, 0, sizeof(B_t));

		scanf("%d%d", &n, &k);
		while(k--) B[p=search()] = 1;

		printf("Case #%d: %d %d\n", ++kase, B_t[p].maxi(), B_t[p].mini());
	}

	return 0;
}

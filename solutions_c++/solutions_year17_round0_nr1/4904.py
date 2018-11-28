#include<cstdio>
#include<cstring>
const int maxn = 1000 + 10;

char S[maxn];
int K, ans;

void flip(int l, int r)
{
	for(int i = l; i < r; i++) {
		if(S[i] == '-') S[i] = '+';
		else S[i] = '-';
	}
}

bool solve()
{
	int hight = strlen(S);
	for(int i = 0; i < hight-K+1; i++) if(S[i] == '-') {
		flip(i, i+K);
		ans++;
	}

	for(int i = 0; i < hight; i++) if(S[i] == '-') return false;
	return true;
}

int main()
{
	int T, kase = 0;
	scanf("%d", &T);

	while(T--) {
		ans = 0;

		scanf("%s%d", S, &K);
		printf("Case #%d: ", ++kase);
		if(solve()) printf("%d\n", ans);
		else printf("IMPOSSIBLE\n");
	}

	return 0;
}

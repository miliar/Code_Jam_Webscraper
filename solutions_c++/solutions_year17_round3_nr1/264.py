#include <algorithm>
#include <cstdio>
#define PI 3.141592653589793238462643383279
using namespace std;

struct pancake{
	long long R, H;
	long long m;
};

bool compare1(pancake x, pancake y){
	return x.R > y.R || x.R == y.R && x.m > y.m;
}

bool compare2(pancake x, pancake y){
	return x.m > y.m || x.m == y.m && x.R > y.R;
}

int T, N, K;
long long ans, cnt;
pancake p[2000];

int main (){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		scanf("%d %d", &N, &K);
		for (int j = 0; j < N; j++){
			scanf("%I64d %I64d", &p[j].R, &p[j].H);
			p[j].m = p[j].R * p[j].H;
		}
		sort(p, p + N, compare1);
		
		ans = 0;
		for (int j = 0; j <= N - K; j++){
			cnt = p[j].R * p[j].R;
			sort(p + j + 1, p + N, compare2);
			for (int k = j; k < j + K; k++)
				cnt += 2 * p[k].R * p[k].H;
			if (ans < cnt)
				ans = cnt;
			sort(p + j + 1, p + N, compare1);
		}
		
		printf("Case #%d: %.9lf\n", i, ans * PI);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}

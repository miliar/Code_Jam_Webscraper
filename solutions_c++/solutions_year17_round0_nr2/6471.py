#include<iostream>
#include<cstdio>
using namespace std;
int f[1000];
int main(){
	freopen("input.in","r", stdin);
	freopen("output.out","w", stdout);
	int test_cases;
	scanf("%d", &test_cases);
	for (int time = 1; time <= test_cases; time++){
		long long n;
		scanf("%lld", &n);
		int m = 0;
		while (n > 0){
			f[++m] = n % 10;
			n /= 10;
		}
		for (int i = 1; i < m; i++)
			if (f[i] < f[i + 1]){
				f[i + 1] = f[i + 1] - 1;
				for (int j = 1; j <= i ; j++)
					f[j] = 9;
			}
		if (f[m] == 0) m--;
		printf("Case #%d: ", time);
		for (int i = m; i >= 1; i--)
			printf("%d", f[i]);
		printf("\n");
	}
}
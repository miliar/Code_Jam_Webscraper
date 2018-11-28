#include<iostream>
#include<cstdio>
using namespace std;
int f[2222];
int test_cases;
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d", &test_cases);
	for (int times = 1; times <= test_cases; times++){
		char ch;
		while (ch != '-' && ch != '+') scanf("%c", &ch);
		int n = 0;
		f[++ n] = (ch == '-' ? 0 : 1);
		while (ch != ' '){
			scanf("%c", &ch);
			f[++ n] = (ch == '-' ? 0 : 1);
		}
		int k;
		scanf("%d", &k);
		int ans = 0;
		for (int i = 1; i <= n; i++)
			if (f[i] == 0){
				if (i + k > n){
					ans = -1;
					break;
				}
				for (int j = 0; j < k; j++)
					f[i + j] = 1 - f[i + j];
				ans++;
			}
		printf("Case #%d: ",times);
		if (ans >= 0) printf("%d\n", ans); else printf("IMPOSSIBLE\n");
	}
}
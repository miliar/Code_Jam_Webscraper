#include <bits/stdc++.h>
#define N 1010
using namespace std; 
int cnt, T, n, m, a[N]; 
char s[N]; 
int main() 
{
	freopen("in.txt", "r", stdin); 
	freopen("out.txt", "w", stdout); 
	
	scanf("%d", &T); 
	for (int Cs = 1; Cs <= T; Cs++) 
	{
		cnt = 0; 
		scanf("%s%d", s + 1, &m); 
		n = strlen(s + 1); 
		for (int i = 1; i <= n; i++) a[i] = (s[i] == '-') ? 0 : 1; 
		for (int i = 1; i <= n-m+1; i++) 
		{
			if (a[i]) continue; 
			cnt++; 
			for (int j = i; j <= i+m-1; j++)
				 a[j] ^= 1; 
		}
		bool q = true; 
		for (int i = n-m+2; i <= n; i++) 
			if (!a[i]) q = false; 
		printf("Case #%d: ", Cs); 
		if (!q) puts("IMPOSSIBLE"); 
		else printf("%d\n", cnt); 
	}
}

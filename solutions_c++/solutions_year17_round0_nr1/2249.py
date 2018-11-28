#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, n, k;
char str[10001];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &test);
	for (int uu = 1; uu <= test; uu++)
	{
		scanf("%s%d", str, &k);
		n = strlen(str);
		int ans = 0;
		for (int i = 0; i <= n - k; i++)
		 	if (str[i] == '-')
		 	{
		 		for (int j = i; j < i + k; j++)
		 			if (str[j] == '-')
		 				str[j] = '+';
		 			else
		 				str[j] = '-';
		 		++ans;
			}
		bool ok = true;
		for (int i = 0; i < n && ok; i++)
			if (str[i] == '-')
				ok = false;
		printf("Case #%d: ", uu);
		if (!ok)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n", ans);
	}
}
		
	

#include<stdio.h>
#include<string.h>
int t,k,flag,ans,len;
char s[1001];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for(int test=1;test<=t;test++){
		flag = ans = 0;
		scanf("%s %d", s, &k);
		len = strlen(s);
		for (int i = 0; s[i]; i++){
			if (s[i] == '-'){
				if (i + k > len)break;
				ans++;
				for (int j = i; j < i + k; j++){
					if (s[j] == '-')s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		for (int i = 0; s[i]; i++){
			if (s[i] == '-'){
				flag = 1; break;
			}
		}
		if (flag)printf("Case #%d: IMPOSSIBLE\n", test);
		else printf("Case #%d: %d\n", test, ans);
	}
	return 0;
}
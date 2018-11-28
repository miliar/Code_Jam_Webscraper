#include <cstdio>
#include <cstdlib>
#include <cstring>

int main()
{
	int t, caseNum = 1, i, j, k, ans, flag;
	char str[1005];
	scanf("%d", &t);
	while(t--){
		scanf("%s%d", str, &k);
		ans = 0;
		for(i = 0;i < strlen(str) - k + 1;i++){
			if(str[i] == '-'){
				ans += 1;
				for(j = 0;j < k;j++)
					if(str[i + j] == '-')
						str[i + j] = '+';
					else
						str[i + j] = '-';
			}
		}
		flag = 0;
		for(i = 0;i < strlen(str);i++){
			if(str[i] == '-'){
				flag = 1;
				break;
			}
		}
		if(flag == 1)
			printf("Case #%d: IMPOSSIBLE\n", caseNum++);
		else
			printf("Case #%d: %d\n", caseNum++, ans);
	}
	return 0;
}

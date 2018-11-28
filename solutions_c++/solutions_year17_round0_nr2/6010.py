#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int check(int value)
{
	int i;
	char v_str[20];
	sprintf(v_str, "%d", value);
	if(strlen(v_str) == 1)
		return 1;
	for(i = 0;i < strlen(v_str) - 1;i++){
		if(int(v_str[i]) > int(v_str[i + 1]))
			break;
	}
	if(i == strlen(v_str) - 1)
		return 1;
	return 0;
}

int main()
{
	int t, caseNum = 1, i, j, n,ans;
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		while(n--){
			if(check(n + 1) == 1){
				ans = n + 1;
				break;
			}
		}
		printf("Case #%d: %d\n", caseNum++, ans);
	}
	return 0;
}

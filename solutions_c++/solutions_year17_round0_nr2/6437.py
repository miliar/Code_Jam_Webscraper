#include <cstdio>
#include <cstring>
#include <algorithm>

char str[30], len, found;
int num[30], ans[30];

void recur(int pos, int last, int less){
	// printf("%d %d %d\n", pos, last, less);
	if (found)
		return ;
	if (pos == len){
		for (int i=0; i<len; i++)
			printf("%d", ans[i]);
		found = 1;
	}
	for (int i=9; i>=last; i--){
		if (less == 0 && i > num[pos])
			continue;
		else{
			ans[pos] = i;
			if (i < num[pos])
				recur(pos+1, i, 1|less);
			else
				recur(pos+1, i, less);
		}
	}
}


int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int n, err;
	scanf("%d", &n);
	for (int x=1; x<=n; x++){
		err = 0 ;
		found = 0;
		printf("Case #%d: ", x);
		scanf(" %s", &str);
		len = strlen(str);
		for (int i=0; i<len; i++){
			num[i] = str[i]-'0';
		}
		for (int i=num[0]; i>=1; i--){
			ans[0] = i;
			recur(1, i, i<num[0]?1:0);
		}
		if (found == 0)
			for (int i=1; i<len; i++)
				printf("9");
		printf("\n");
	}
	return 0;
}
#include <cstdio>
#include <cstring>

char str[1010];
int k, len;

int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int q, cnt, err;
	scanf("%d", &q);
	for (int x=1; x<=q; x++){
		cnt=0, err=0;	
		printf("Case #%d: ", x);
		scanf(" %s %d", &str, &k);
		len = strlen(str);
		for (int i=0; i<len-k+1; i++){
			if (str[i] == '-'){
				cnt++;
				for (int j=0; j<k; j++)
					str[i+j] = ((str[i+j]=='-')?'+':'-');
			}
		}
		for (int i=len-k+1; i<len; i++)
			if (str[i] == '-')
				err = 1;
		if (err == 0)
			printf("%d\n", cnt);
		else
			printf("IMPOSSIBLE\n", cnt);
	}
	return 0;
}
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
typedef long long LL;
using namespace std;
int a[25] , T;
char s[25];
int main()
{
	freopen("B-large (1).in" , "r" , stdin);
	freopen("B-large2.out" , "w" , stdout);
	scanf("%d" , &T);
	int cas = 0;
	while(T--){
		scanf("%s" , s + 1);
		int len = strlen(s + 1);
		for(int i = 1;i <= len;i++){
			a[i] = s[i] - 48;
		}
		for(int i = len;i >= 1;i--){
			if(a[i] < a[i - 1]){
				for(int j = i;j <= len;j++)
					a[j] = 9;
				a[i - 1]--;
			}
		}
		printf("Case #%d: " , ++cas);
		for(int i = 1;i <= len;i++){
			if(a[i] != 0 && i == 1) printf("%d" , a[i]);
			else if(i > 1) printf("%d" , a[i]);
		}
		printf("\n");
	}
	fclose(stdin);
	fclose(stdout);
}

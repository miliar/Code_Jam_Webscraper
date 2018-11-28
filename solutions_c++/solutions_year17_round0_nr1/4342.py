#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
const int MaxN = 1000;
using namespace std;
char s[MaxN + 5];
int n;
int main()
{
	freopen("A-large (2).in" , "r" , stdin);
	freopen("A-large.out" , "w" , stdout);
	scanf("%d" , &n);
	int cas = 0;
	while(n--){
		int x , ans = 0;
		scanf("%s%d" , s + 1 , &x);
		int len = strlen(s + 1);
		for(int i = 1;i <= len - x + 1;i++){
			if(s[i] == '-'){
				ans++;
				for(int j = i;j <= i + x - 1;j++){
					if(s[j] == '+') s[j] = '-';
					else s[j] = '+';
				}
			}
		}
		bool ok = 1;
		for(int i = 1;i <= len;i++) {
			if(s[i] == '-') ok = 0;
		}
		printf("Case #%d: " , ++cas);
		if(!ok) printf("IMPOSSIBLE\n");
		else printf("%d\n" , ans);
	}
}

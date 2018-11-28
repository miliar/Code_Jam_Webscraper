#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<algorithm>
using namespace std;
char s[1005];
int T, k;
int main(){
	//freopen("A-small-attempt2.in.txt","r",stdin);
	//freopen("A-small-attempt2.out","w",stdout);
	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	int Case = 0;
	while(T--){
		scanf("%s %d", s + 1, &k);
		int len = strlen(s + 1);
		int cnt = 0;
		for(int i = 1; i <= len - k + 1; i++){
			if(s[i] == '+') continue;
			cnt++;
			for(int j = 0; j < k; j++){
				if(s[i + j] == '+') s[i + j] = '-';
				else if(s[i + j] == '-') s[i + j] = '+';
			}
		}
		bool flag = true;
		for(int i = len - k + 1; i <= len; i++)
			if(s[i] == '-') flag = false;
		printf("Case #%d: ", ++Case);
		if(!flag) printf("IMPOSSIBLE\n");
		else printf("%d\n", cnt);
	}
	return 0;
}


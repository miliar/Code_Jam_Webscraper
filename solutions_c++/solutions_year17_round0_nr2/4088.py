#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<cstdlib>
using namespace std;
typedef long long LL;
LL n;
int T;
int s[25];
int main(){
	//freopen("B-small-attempt0.in.txt", "r", stdin);
	//freopen("B-small-attempt0.out", "w", stdout);
	freopen("B-large.in.txt", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int Case = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%lld", &n);
		int len = 0;
		bool ok = false;
		while(n){
			s[++len] = n % 10;
			if(s[len] == 0) ok = true;
			n /= 10;
		}
		int pos = 0;
		for(int i = 1; i < len; i++){
			if(s[i] < s[i + 1]){
				pos = i;
				s[i + 1]--;
			}
		}
		printf("Case #%d: ", ++Case);
		if(s[len]) printf("%d", s[len]);
		for(int i = len - 1; i >= 1; i--){
			if(i <= pos) printf("9");
			else printf("%d", s[i]);
		}
		printf("\n");
	}
	return 0;
}

#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 1005;

void chg(char *a){
	if (*a == '+')
		*a = '-';
	else
		*a = '+';
}

int go(char a[],int k){
	int len = strlen(a);
	int ret = 0;
	for (int i = k - 1; i < len; ++i){
		int prev = i - k + 1;
		if (a[prev] == '-'){
			++ret;
			for (int j = prev; j <= i; ++j){
				chg(a + j);
			}
		}
	}
	for (int i = 0; i < len; ++i){
		if (a[i] != '+')
			return -1;
	}
	return ret;
}

int main(){

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	
	
	

	char a[N];
	for(int i=1;i<=t;++i){
		scanf("%s", a);
		int k;
		scanf("%d", &k);
		
		int ret;
		
		if ((ret = go(a,k)) < 0){
			printf("Case #%d: IMPOSSIBLE\n",i);
		}
		else
			printf("Case #%d: %d\n", i,ret);
	}
	return 0;
}
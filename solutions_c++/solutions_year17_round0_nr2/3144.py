#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <string>
#include <map>

using namespace std;


void solve(){
	char a[100];
	scanf("%s", a);
	int len = strlen(a);

	for(int i=len-1;i;i--)
		if(a[i]<a[i-1]){
			for(int j=i;j<len;j++) a[j]='9';
			a[i-1]--;
		}

	printf("%ld\n", atol(a));
}

int main(){
	int cs, lp;
	scanf("%d", &cs);
	for(int lp = 1; lp <=cs; lp++){
		printf("Case #%d: ", lp);
		solve();
	}
	return 0;
}

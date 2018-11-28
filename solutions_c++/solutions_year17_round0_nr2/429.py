#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

void solve(){
	char lho[999];
	int res[999];
	memset(res, 0, sizeof (res));
	scanf("%s",lho);
	int N = strlen(lho);
	int largest = 9;
	bool hajar = false;
	res[0] = lho[0] - '0';
	for (int i=1;i<N;i++){
		res[i] = lho[i] - '0';
		if (hajar){
			res[i] = 9;
		} else
		if (res[i] < res[i-1]){
			int j = i;
			while (j > 0 && res[j] < res[j-1]){
			res[j-1]--;
			res[j] = 9;
			j--;
			}
		
		hajar = 1;
		}
	}
	if (res[0] > 0)
		printf("%d",res[0]);
	for (int i=1;i<N;i++){
		printf("%d",res[i]);
	}
	printf("\n");
}

int main(){
	int T;
	scanf("%d",&T);
	for (int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}
}
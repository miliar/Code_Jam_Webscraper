#include <bits/stdc++.h>
using namespace std;

const int N = 105;

int n, p;
int dp[N][N][N];
int freq[10];

int mod(int x){
	x %= p;
	if(x < 0)	x += p;
	return x;
}

int calc(int indice, int mod1, int mod2, int mod3, int toUse){
	if(indice == n)	return 0;
	if(dp[indice][mod1][mod2] != -1)	return dp[indice][mod1][mod2];
	int profit = 0;
	if(toUse == 0)	profit = 1;
	dp[indice][mod1][mod2] = 0;
	for(int i = 1; i < p; i++){
		if(i == 1 and mod1 > 0){
dp[indice][mod1][mod2] = max(dp[indice][mod1][mod2], profit + calc(indice + 1, mod1 - 1, mod2, mod3, mod(toUse - 1)));
		}
		if(i == 2 and mod2 > 0){
dp[indice][mod1][mod2] = max(dp[indice][mod1][mod2], profit + calc(indice + 1, mod1, mod2 - 1, mod3, mod(toUse - 2)));
		}
		if(i == 3 and mod3 > 0){
dp[indice][mod1][mod2] = max(dp[indice][mod1][mod2], profit + calc(indice + 1, mod1, mod2, mod3 - 1, mod(toUse - 3)));
		}
	}
	return dp[indice][mod1][mod2];
}

void solve(){

	memset(dp, -1, sizeof(dp));

	int tmp;
	scanf("%d %d", &n, &p);

	for(int i = 0; i < p; i++)	freq[i] = 0;

	for(int i = 1; i <= n; i++){
		scanf("%d", &tmp);
		tmp %= p;
		freq[tmp]++;
	}

	cout<<freq[0] + calc(freq[0], freq[1], freq[2], freq[3], 0)<<endl;
}

int main(){
	int t;
	scanf("%d", &t);
	for(int big = 1; big <= t; big++){
		cout<<"Case #"<<big<<": ";
		solve();
	}
}
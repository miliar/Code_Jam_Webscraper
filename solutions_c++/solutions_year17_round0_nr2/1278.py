#include "bits/stdc++.h"
using namespace std;
const int D = 19;
int t;
long long n;
string str;
long long pw[D];
long long dp[D][10][2];
bool calc[D][10][2];
long long solve(int pos , int last , bool pre){
	if(pos >= str.size()){
		return 0;
	}
	if(calc[pos][last][pre]){
		return dp[pos][last][pre];
	}
	long long res = -1;
	int dig = str[pos] - '0';
	int p = str.size() - pos - 1;
	for(int i = last ; i < 10 ; ++i){
		if(!pre && i > dig){
			continue;
		}
		long long tmp = solve(pos + 1 , i , pre | (i < dig));
		if(tmp >= 0){
			res = max(res , tmp + pw[p] * i);
		}
	}
	calc[pos][last][pre] = 1;
	return dp[pos][last][pre] = res;
}
int main(){
	pw[0] = 1;
	for(int i = 1 ; i < D ; ++i){
		pw[i] = 10LL * pw[i - 1];
	}
	scanf("%d" , &t);
	for(int tc = 1 ; tc <= t ; ++tc){
		printf("Case #%d: " , tc);
		scanf("%lld" , &n);
		str = to_string(n);
		memset(calc , 0 , sizeof(calc));
		printf("%lld\n" , solve(0 , 0 , 0));
	}
}
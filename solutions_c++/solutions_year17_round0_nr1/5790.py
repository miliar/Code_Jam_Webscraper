#include <bits/stdc++.h>
#define MOD 1000000007
using namespace std;

const int N = 1e3;
int t, k , n, ans;
string S;

bool ok(){
	for(int i = 0 ; i < n ; ++i)
		if(S[i]=='-')
			return 0;
	return 1;
}
int main(){
	freopen("i.in", "r", stdin);
	freopen("o.out", "w", stdout);
	scanf("%d\n", &t);
	for(int i = 1 ; i <= t ; ++i){
		cin >> S >> k ;
		n = S.length();
		ans = 0 ;
		for(int j = 0 ; j < n-k+1 ; ++j){
			if(S[j] == '-'){
				++ans;
				for(int q = j ; q < j+k ; ++q)
					S[q] = S[q]=='+' ? '-' : '+';
			}
		}
		printf("Case #%d: ", i);
		if(ok())
			printf("%d\n", ans);
		else
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
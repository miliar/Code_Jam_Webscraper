#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <cstdlib>
#define maxn 1009
using namespace std;
char s[maxn];
int m;
bool check(int n){
	for(int i = 0; i < n; i++){
		if(s[i] == '-')
			return 0;
	}
	return 1;
}
int main(){
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/QualificationRound/A.in", "r", stdin);
	freopen("/Users/fengweiming/ProgramContest/GoogleCodeJam2017/QualificationRound/A.out", "w", stdout);
	int tt, cot = 1;
	scanf("%d", &tt);
	while(tt--){
		scanf("%s", s);
		scanf("%d", &m);
		int n = strlen(s);
		int ans = 0;
		for(int i = 0; i < n; i++){
			if(s[i] == '+')
				continue;
			if(i + m - 1 >= n)
				break;
			for(int j = 0; j < m; j++){
				if(s[i + j] == '+')
					s[i + j] = '-';
				else 
					s[i + j] = '+';
			}
			ans++;
		}
		if(check(n))
			printf("Case #%d: %d\n", cot++ ,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", cot++);
	}
	return 0;
}
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <utility>
#include <map>
#include <vector>
#include <climits>
#include <set>
#include <algorithm>
 
using namespace std;

long long N;
int d[20], n;

long long b[20];

long long solve(int prevDig, int ix, bool tight){

	if(ix == n - 1){
		if(tight == 0)
			return 9;
		else{
			if(prevDig > d[ix])
				return LLONG_MIN;
			return d[ix];			
		}
	}
	
	if(tight == 0)
		return b[n - 1 - ix] * 9 + solve(9, ix + 1, 0);

	if(prevDig > d[ix])
		return LLONG_MIN;

	long long ret = LLONG_MIN;

	if(d[ix] > 1 && d[ix] - 1 >= prevDig)
		ret = max(ret, b[n - 1 - ix] * (d[ix] - 1) + solve(9, ix + 1, 0));

	ret = max(ret, b[n - 1 - ix]*d[ix] + solve(d[ix], ix + 1, 1));

	return ret;
}

int main(){
	b[0] = 1;
	for(int i = 1; i <= 18; i++)
		b[i] = b[i - 1] * 10;

	int t;
	scanf("%d", &t);
	for(int p = 1; p <= t; p++){
		char s[20];
		scanf("%s", s);
		n = strlen(s);
		for(int i = 0; i < n; i++)
			d[i] = s[i] - '0';
		
		long long ans = 0;

		for(int i = 1; i < n; i++)
			ans = ans * 10 + 9;

		ans = max(ans, solve(1, 0, 1));

		printf("Case #%d: %lld\n", p, ans);
	}
	return 0;
}
#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;

char opac(char co){
	if(co == '-') return '+';
	return '-';
}

void solve(int test){
	string pan;
	cin>>pan;
	int k;
	cin>>k;
	int sum = 0;
	REP(a,pan.size()-k+1){
		if(pan[a] == '-'){
			REP(b, k) pan[a+b] = opac(pan[a+b]);
			sum++;
		}
	}

	REP(a,k){
		if(pan[pan.size()-a-1] == '-'){
			printf("Case #%i: IMPOSSIBLE\n", test);
			return;
		}
	}

	printf("Case #%i: %i\n", test, sum);
}

int main(){
	int t;
	scanf("%i",&t);
	REP(a,t) solve(a+1);
	return 0;
}

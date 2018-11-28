#include <bits/stdc++.h>
#define MOD 1000000007
using namespace std;

const int N = 1e3;
int t, k , n, ans;
string s;

bool ok(){
	for(int i = 0 ; i < n-1 ; ++i)
		if(s[i] > s[i+1])
			return 0;
	return 1;
}

void neg(int ind){
	if(ind<0)	return ;
	if(s[ind] == '0'){
		s[ind] = '9';
		neg(ind-1);
	}
	else{
		--s[ind];
	}
}

void solve(int ind){
	if(ok() || ind < 0)
		return;
	s[ind] = '9';
	neg(ind-1);
	solve(ind-1);
}

void prnt(){
	int f = 0;
	for(int i = 0 ; i < n ; ++i){
		if(f || s[i]!='0'){
			f = 1;
			printf("%c", s[i]);
		}
	}
	puts("");
}

int main(){
	freopen("i.in", "r", stdin);
	freopen("o.out", "w", stdout);
	scanf("%d\n", &t);
	for(int i = 1 ; i <= t ; ++i){
		cin >> s;
		n = s.length();
		solve(n-1);
		printf("Case #%d: ", i);
		prnt();
	}
	return 0;
}
#include <stdio.h>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
#define ll long long
string a;
ll ans, n;
void go(bool flag, int pre, int dep, ll val){
	if(dep == a.size()){
		ans = max(ans, val);
		return;
	}
	if(flag){
		go(true, 9, dep+1, val*10 + 9);
	}
	else{
		if(pre <= a[dep]){
			go(false, a[dep], dep+1, val*10 + a[dep]);
			if(pre < a[dep]){
				go(true, a[dep]-1, dep+1, val*10 + a[dep]-1);
			}
		}
	}
	return;
}
int main(){
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d",&test);
	for(int tc=1; tc<=test; tc++){
		cin>>a;
		ans = 0;
		n = 0;
		for(int i=0; i<a.size(); i++)a[i] -= '0';
		for(int i=0; i<a.size(); i++)n = n*10 + a[i];
		go(false, 0, 0, 0);
		printf("Case #%d: %lld\n", tc, ans);
	}
	return 0;
}

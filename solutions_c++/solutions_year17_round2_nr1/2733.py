#define _GLIBCXX_DEBUG
#include<iostream>
#include<cstdio>
#include<bits/stdc++.h>//"geometry.cpp"
#include<iomanip>//"cout<<fixed<<setprecision(n)<<sth<<endl;"
#include<queue>
#include<string>
#include<vector>
#include<utility>
#include<set>
#include<map>
#include<algorithm>//"lower_bound(it,it,v)", "next_permutation(a,a+n)"
#include<functional>//"greater<T>" Ex. sort(a,a+n,greater<int>());
#include<cmath>//"abs", "sqrt"
using namespace std;
#define pb push_back
#define fi first
#define sc second
#define mp make_pair
#define is insert
typedef pair<long double,long double> pll;

bool cmp(pll x,pll y){
	return x.sc<y.sc;
}

void solve(){
	int n;
	long double d,ans=10000000000000;
	pll p[1000];
	cin>>d>>n;
	for(int i=0;i<n;++i){
		cin>>p[i].fi>>p[i].sc;
	}
	sort(p,p+n,cmp);
	for(int i=0;i<n;++i){
		long double ans1=min(ans,d*p[i].sc/(d-p[i].fi));
		if(ans1<=p[i].sc){
			break;
		}
		ans=ans1;
	}
	cout<<fixed<<setprecision(6)<<ans<<endl;
}

int main(){
	int Q;
	cin>>Q;
	for(int q=1;q<=Q;++q){
		cout<<"Case #"<<q<<": ";
		solve();
	}
}

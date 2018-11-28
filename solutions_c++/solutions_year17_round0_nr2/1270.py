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
typedef pair<int,int> pii;//Add other types in the same way.

void solve(){
	string s;
	cin>>s;
	while(true){
		bool f=false;
		for(int i=0;i<s.size();++i){
			if(f){
				s[i]='9';
			}else if(i+1!=s.size()&&s[i]>s[i+1]){
				s[i]-=1;
				f=true;
			}
		}
		if(!f){
			break;
		}
	}
	bool f=true;
	for(int i=0;i<s.size();++i){
		if(!f||s[i]!='0'){
			f=false;
			cout<<s[i];
		}
	}
	cout<<endl;
}

int main(){
	int Q;
	cin>>Q;
	for(int q=1;q<=Q;++q){
		cout<<"Case #"<<q<<": ";
		solve();
	}
}

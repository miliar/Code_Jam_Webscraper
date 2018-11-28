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
	long long n,k0,dk=1,m[2][2];
	int c=0;
	cin>>n>>k0;
	long long k=k0;
	if(k0==1){
		cout<<n-1-(n-1)/2<<" "<<(n-1)/2<<endl;
		return;
	}
	m[0][0]=n;
	m[0][1]=n;
	while(k>0){
		for(int i=0;i<2;++i){
			m[(c+1)%2][0]=(m[c%2][i]-1)/2;
			m[(c+1)%2][1]=m[c%2][i]-1-m[(c+1)%2][0];
			if(i==0&&m[(c+1)%2][0]!=m[(c+1)%2][1]){
				break;
			}
		}
		++c;
		k-=dk;
		dk*=2;
	}
	c%=2;
	if(m[c][0]==m[c][1]){
		cout<<m[c][0]<<" "<<m[c][1]<<endl;
	}else{
		if(m[c][0]<m[c][1]){
			swap(m[c][0],m[c][1]);
		}
		k=n-dk+1-m[c][1]*dk;//the number of m[c][0]
		if(k>=dk/2){
			k-=dk/2;
			if(k0-dk/2+1<=k){
				cout<<m[c][0]<<" "<<m[c][0]<<endl;
			}else{
				cout<<m[c][0]<<" "<<m[c][1]<<endl;
			}
		}else{
			if(k0-dk/2+1<=k){
				cout<<m[c][0]<<" "<<m[c][1]<<endl;
			}else{
				cout<<m[c][1]<<" "<<m[c][1]<<endl;
			}
		}
	}
}

int main(){
	int Q;
	cin>>Q;
	for(int q=1;q<=Q;++q){
		cout<<"Case #"<<q<<": ";
		solve();
	}
}

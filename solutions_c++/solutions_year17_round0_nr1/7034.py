#include <bits/stdc++.h>
//#include <math.h>        round-mas cercano, floor-inferior, ceil-superior, trunc-truncar 
#define endl '\n'
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0)
using namespace std;
typedef long long ll ;
typedef vector<int> vi ;
typedef vector<ll> vll ;

vi cant,num;
vector<bool> b;
void f(string s){
	cant.resize(0);
	num.resize(0);
	b.resize(0);
	cant.push_back(0);
	num.push_back(1);
	if(s[0]=='+')b.push_back(1);
	else b.push_back(0);
	for(int i=1;i<s.size();i++){
		if(s[i]!=s[cant[cant.size()-1]]){
			cant.push_back(i);
			num.push_back(1);
			if(s[i]=='+')b.push_back(1);
			else b.push_back(0);
		}else{
			num[cant.size()-1]++;
		}
	}
	return ;
}
int main() {
//	fast_io();	
int t,t1;
cin>>t;
t1=t;
while(t--){
	string s;
	int n;
	cin>>s>>n;
	int c,m,ct=0;;
	vi cant1,num1;
	bool bu=1;
	do{
		ct++;
		cant1.resize(0);
		num1.resize(0);
		//cout<<s<<endl;
		f(s);
		for(int i=0;i<cant.size();i++){
			if(!b[i]){
				cant1.push_back(cant[i]);
				num1.push_back(num[i]);
			}
		}
		if(cant1.size()>0){
			if(cant1[0]+n>s.size()){
			bu=0;
			break;
			}
			for(int i=cant1[0];i<cant1[0]+n;i++){
				if(s[i]=='-')s[i]='+';
				else s[i]='-';
			}
		}
	}while(cant1.size()>0);
	if(bu)cout<<"Case #"<<t1-t<<": "<<ct-1<<endl;
	else cout<<"Case #"<<t1-t<<": IMPOSSIBLE"<<endl;
}
	return 0;
}

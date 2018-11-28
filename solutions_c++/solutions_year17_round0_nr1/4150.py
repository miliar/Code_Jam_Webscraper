#include <bits/stdc++.h>
#define ll long long
#define var ll
#define vi vector<var>
#define pii pair<var,var>
#define pb push_back
#define fi first
#define se second
const int INF = 0x3f3f3f3f;

using namespace std;

string s1,s2; int k, res, res1, res2;

void change(int i, int x){
	if(x==1){
		if(s1[i]=='-') s1[i]='+';
		else s1[i] = '-';
	} else if(x==2){
		if(s2[i]=='-') s2[i]='+';
		else s2[i] = '-';
	}
}
bool check1(){
	for(int i=0; i<s1.size(); i++)
		if(s1[i]=='-'){ return false; }
	return true;
}
bool check2(){
	for(int i=0; i<s2.size(); i++)
		if(s2[i]=='-'){ return false; }
	return true;
}

int main(){
	
	int t, cont=0, aux; cin>>t;
	while(t--){
		cin>>s1>>k; s2 = s1;
		res1 = 0;
		for(int i=0; i<=s1.size()-k; i++){
			if(s1[i]=='-'){
				for(int j=0; j<k; j++){
					change(j+i, 1);
				}
				res1++;
			}
		}
		res2 = 0;
		for(int i=s2.size()-1; i>=k; i--){
			if(s2[i]=='-'){
				for(int j=0; j<k; j++){
					change(i-j, 2);
				}
				res2++;
			}
		}
		if(!check1()) res1=INF;
		if(!check2()) res2=INF; 
		res = min(res1,res2);
		if(res<INF) cout<<"Case #"<<++cont<<": "<<res<<endl;
		else cout<<"Case #"<<++cont<<": "<<"IMPOSSIBLE"<<endl;
	}
	
	return 0;
}











#include <iostream>
#include <algorithm>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <queue>
#include <stack>
using namespace std;

#define ll long long

int t;
ll n;
string comp;
vector<string> ans;

bool compare(string a,string b){
	if(a.size()<b.size()) return true;
	if(a.size()>b.size()) return false;
	return a<b;
}


void generate(string temp,int n,int cur){
	if(temp.size()>n) return;
	if(temp.size()==n){
		ans.push_back(temp);
		return;
	}
	temp.push_back(cur+'0');
	generate(temp,n,cur);
	temp.pop_back();
	for(int j=cur+1;j<=9;j++){
		temp.push_back(j+'0');
		generate(temp,n,j);
		temp.pop_back();
	}
	return;
}

void preprocess(){
	for(int i=1;i<=18;i++){
		string t;
		generate(t,i,1);
	}
	sort(ans.begin(),ans.end(),compare);
}


int main(){
	preprocess();
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	for(int i=1;i<=t;i++){
		cout<<"Case #"<<i<<": ";
		cin>>n;
		comp = to_string(n);
		vector<string>::iterator it = upper_bound(ans.begin(),ans.end(),to_string(n),compare);
		cout<<ans[it-ans.begin()-1]<<endl;
	}
	return 0;
}
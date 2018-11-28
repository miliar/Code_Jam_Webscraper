#include <bits/stdc++.h>
#define ll long long
#define var int
#define vi vector<var>
#define pii pair<var,var>
#define pb push_back
#define fi first
#define se second
const int inf = 0x3f3f3f3f;

using namespace std;

string s;

bool func(){
	for(int i=0; i<s.size()-1; i++){
		if(s[i] > s[i+1]){
			s[i]--;
			for(int j=i+1; j<s.size(); j++) s[j] = '9';
			return true;
		}
	}
	return false;
}

void zeros(){
	for(int i=0; i<s.size(); i++){
		if(s[i]>'0'){
			s = s.substr(i);
			return;
		}
	}
}

int main(){
	
	int t,cont=0; cin>>t;
	while(t--){
		cin>>s;
		while(func());
		zeros();
		cout<<"Case #"<<++cont<<": "<<s<<endl;
	}
	
	return 0;
}











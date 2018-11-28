#include <bits/stdc++.h>

using namespace std;

bool check(int n){
	stringstream ss;
	ss<<n;
	string s;
	ss>>s;
	for(int i=1;i<(int)s.size();i++)
		if(s[i]<s[i-1])
			return 0;
	return 1;
}

int main(){
	int test;
	cin>>test;
	int t=1;
	while(test--){
		cout<<"Case #"<<t<<": ";
		t++;
		int n;
		cin>>n;
		for(int i=n;i>=1;i--){
			if(check(i)){
				cout<<i<<"\n";
				break;
			}
		}
	}
	return 0;
}
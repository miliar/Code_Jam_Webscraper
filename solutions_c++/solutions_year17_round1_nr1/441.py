#include <bits/stdc++.h>
using namespace std;

string s[30];

void solve(){
	int r, c;
	cin>>r>>c;
	for(int i = 0; i < r; i++){
		cin>>s[i];
	}

	for(int i = 0; i < r; i++){
		for(int j = 1; j < c; j++){
			if(s[i][j] == '?'){
				s[i][j] = s[i][j - 1];
			}
		}
		for(int j = c - 2; j >= 0; j--){
			if(s[i][j] == '?'){
				s[i][j] = s[i][j + 1];
			}
		}
	}

	for(int i = 1; i < r; i++){
		for(int j = 0; j < c; j++){
			if(s[i][j] == '?'){
				s[i][j] = s[i - 1][j];
			}
		}
	}

	for(int i = r - 2; i >= 0; i--){
		for(int j = 0; j < c; j++){
			if(s[i][j] == '?'){
				s[i][j] = s[i + 1][j];
			}
		}
	}

	for(int i = 0; i < r; i++){
		for(int j = 0; j < c; j++){
			cout<<s[i][j];
		}
		cout<<endl;
	}
}

int main(){
	int t;
	cin>>t;
	for(int big = 1; big <= t; big++){
		cout<<"Case #"<<big<<": "<<endl;
		solve();
	}
}
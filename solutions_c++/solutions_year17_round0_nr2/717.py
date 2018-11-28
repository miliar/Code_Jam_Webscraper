#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
string str;
int T;
bool cannot(int x, char ch){
	for(int i = x; i < str.length(); i++){
		if(str[i] == ch) continue;
		if(str[i] < ch) return true;
		else return false;
	}
	return false;
}

int main(){
	//freopen("a.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin>>T;
	for(int Case = 1; Case <= T; Case++){
		cin>>str;
		/*
		for(int i = n; i >= 1; i--)
			if(ok(i)) cout<<i<<endl;
		*/
		cout<<"Case #"<<Case<<": ";
		int f = 0;
		for(int i = 0; i < str.length(); i++){
			if(cannot(i+1, str[i])) {
				for(int j = 0; j < i; j++) cout<<(char)str[j];
				if(str[i] != '1') cout<<(char)(str[i]-1);
				for(int j = i+1; j < str.length(); j++) cout<<9;
				cout<<endl;
				f = 1;
				break;
			}
		}
		if(!f) cout<<str<<endl;
	}
}

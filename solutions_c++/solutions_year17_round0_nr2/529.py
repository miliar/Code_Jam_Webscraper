#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

bool check( string &str ){
	for(int i = 1; i < str.size(); i++){
		if(str[i] < str[i-1]) return true;
	}
	return false;
}

int main(){
	ios::sync_with_stdio(false);
	int t;
	string str;
	
	cin >> t;

	for(int w = 1; w <= t; w++){
		cin >> str;

		int n = str.size();

		while( check(str) ){
			n = str.size();
			for(int i = 1; i < n; i++){
				if( str[i] < str[i-1] ){
					str[i-1]--;
					while( i < n ) str[i++] = '9';
					if( str[0] == '0' ){
						str.erase(str.begin());
					}
					break;
				}
			}
		}

		cout << "Case #" << w << ": " << str << '\n';

	}

	return 0;
}
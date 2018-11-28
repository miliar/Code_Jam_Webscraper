#include <bits/stdc++.h>

using namespace std;

int T;
string str;

int ok(){
	if(str.size() == 1) return -1;
	for(int i = 0 ; i+1 < str.size() ; ++i)
		if(str[i] > str[i+1]) return i;
	return -1;
}

string goodStr(){
	if(str[0] == '0') return str.substr(1, -1);
	return str;
}

int main(){
	
	freopen("b.in", "r", stdin);
	freopen("b.res", "w", stdout);
	cin.sync_with_stdio(0);
	
	cin >> T;
	for(int t = 1 ; t <= T ; ++t){
		cin >> str;
		int i;
		while((i = ok()) != -1){
			str[i] -= 1;
			for(int j = i+1 ; j < str.size() ; ++j) str[j] = '9';
		}
		printf("Case #%d: %s\n", t, goodStr().c_str());
	}

	return 0;
}

#include <bits/stdc++.h>

using namespace std;

inline int print(int a, int c){
	cout << "Case #" << c << ": " << a << endl;
	return 0;
}

inline int fun(int xx){
	string str = to_string(xx);
	int x = str[0];
	for(int i = 1; i < str.size(); i++){
		if(x > str[i]) return 0;
		x = str[i];
	}
	return 1;
}

int main(){
	int n, c;
	cin >> n;
	for(int i = 0; i < n; i++){
		cin >> c;
		while(!fun(c)) c--;
		print(c, i + 1);
	}
	return 0;
}
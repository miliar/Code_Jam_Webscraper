#include <iostream>
#include <vector>
#include <string>

using namespace std;

string sol(string& b, int a){
	int n = b.size();
	//cout << "n = "<< n << "a = " << a << endl;
	int ans = 0;
	for(int i = 0; i <= n - a; ++i){
		if(b[i] == '-'){
			ans++;
			for(int j = i; j < i + a; ++j){
				if(b[j] == '+') b[j] = '-';
				else b[j] = '+';
			}
		}
	}
	for(int i = n - a; i < n; ++i){
		if(b[i] == '-') return "IMPOSSIBLE";
	}
	return to_string(ans);
}


int main(){
	int t;
	cin >> t;
	
	string b;
	int a; 
	for(int i = 0; i < t; ++i){
		cin >> b >> a;
		string ans = sol(b, a);
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int foo(string s, int n){
	if (s.size() < n){
		for (int i = 0; i < s.size(); i++)
			if (s[i] == '-') return -1;
		return 0;	
	}
	if (s.size() == n){
		int fill = 0;
		int fill2 = 0;
		for (int i = 0; i < s.size(); i++)
			if (s[i] == '-') fill = 1;
		for (int i = 0; i < s.size(); i++)
			if (s[i] == '+') fill2 = 1;
		if (fill == 0)  return 0;
		if (fill2 == 0)	return 1;
		return -1;
	}
	if (s[s.size()-1] == '+'){
		s.pop_back();
		return foo(s,n);
	}
	if (s[s.size()-1] == '-'){
		for (int i = 0; i<n; i += 1){
			s[s.size()-1-i] = (s[s.size()-1-i] == '+' ? '-' : '+');
		}
		s.pop_back();
		int m = foo(s,n);
		return (m != -1 ? 1+ m : -1) ;
	}
	return -1;
}

int main(void){
	const bool debug = false;
	if (not debug){
		int t = 0;
		cin >> t;
		for (int i = 1; i <= t; i += 1){
			string s;
			cin >> s;
			int n = 0;
			cin >> n;
			int m = foo(s,n);
			cout << "Case #" << i << ": ";
			if (m == -1){
				cout << "IMPOSSIBLE";
			} else {
				cout << m;	
			}
			cout << endl;
		}
	} else {
		
	}
}


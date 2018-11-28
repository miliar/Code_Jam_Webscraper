#include <iostream>
#include <string>
using namespace std;

int t, k, i, c, m;

string flip(string s, int i, int k){
	for(int j = i; j < i+k ; ++j){
		if(s[j] == '-')
			s.replace(j, 1, "+");
		else
			s.replace(j, 1, "-");
	}
	return s;
}

int main() {
	cin >> t;
	m = t;
	while(t--){
		string s;
		c = 0;
		cin >> s >> k;
		for(i = 0; i <= s.length() - k; ++i){
			if(s[i] == '-'){
				s = flip(s, i, k);
				c++;
			}
		}
		if(s.find("-") != string::npos)
			cout << "Case #" << m-t  << ": "<< "IMPOSSIBLE" << endl;
		else 
			cout << "Case #" << m-t  << ": "<< c << endl;
	}
	return 0;
}

//https://hastebin.com/mecohetete.cpp
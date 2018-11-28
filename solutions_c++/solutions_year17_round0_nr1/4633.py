#include <bits/stdc++.h>
#include <unordered_map>
#include <tuple>

using namespace std;

unordered_map<string, int> seen;

void flip(string &s, int st, int k){
	for(int i=0; i < k; ++i){
		if(s[st + i] == '-') s[st + i] = '+';
		else s[st + i] = '-';
	}
}

int numFlips(string& s, int k, bool &g){
	int cost = 0;

	//cout << s << endl;
	int i=0;
	for(; i+k < s.size(); ++i){
		if(s[i] == '-'){
			flip(s, i, k);
			++cost;
			//cout << s << endl;
		}
	}

	if(s[i] == '-'){ 
		flip(s, i, k);
		++cost;
	}
	g = true;
	for(; i<s.size(); ++i){
		g = g && (s[i] == '+');
	}

	return cost;
}

int main(int argc, char const *argv[]) {
	int T;
	string S;
	int K, D;

	cin >> T;	
	for(int daCase = 1; daCase <= T; ++daCase){
		cin >> S;
		cin >> K;

		bool g = true;
		int c = numFlips(S, K, g);

		cout << "Case #" << daCase << ": " ;
		if(g){
			cout << c;
		} else{
		 cout << "IMPOSSIBLE";
		}

		cout << endl;
	}
}
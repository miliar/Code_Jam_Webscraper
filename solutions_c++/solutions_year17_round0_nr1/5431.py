#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>
#include <sstream>
#include <string>
using namespace std;


string solve(string S, int K) {
	//Impossible case
	/*bool imp = true;
	
	for(int i=1; i<S.length(); ++i) {
		imp &= (S[i-1]!=S[i]);
	}
	
	if(imp) {
		return "IMPOSSIBLE";
	}*/
	
	bool fin = false;
	int moves = 0;
	
	while(!fin) {
		int id =  S.find('-');
		if(id==string::npos) {
			fin = true;
			break;
		}
		
		if(id > (S.length()-K)) {
			id = S.length() - K;
		}
		//cout << id << " ";
		
		for(int i=id; i<id+K; i++) {
			S[i] = S[i]=='+' ? '-' : '+';
		}
		//cout << S << endl;
		
		moves++;
		//getchar();
		if(moves >= 50) {
			fin = false;
			return "IMPOSSIBLE";
		}
	}
	//cout << moves << endl;
	stringstream ss;
	ss << moves;
	return ss.str();
}

int main() {
	int T, K;
	string S;
	
	cin >> T;
	
	for(int t=1; t<=T; ++t) {
		cin >> S >> K;
		cout << "Case #" << t << ": " << solve(S,K) << endl;
	}
	return 0;
}
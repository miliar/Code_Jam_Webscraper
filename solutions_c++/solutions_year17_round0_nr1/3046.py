#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cstdlib>
#include <algorithm>
#include <assert.h>
#include <set>

using namespace std;

int number_of_uses(string S, int N) {
	int uses = 0;
	
	for (int i=0; i+N<=S.size(); i++) if (S[i] == '-') {
		for (int j=i; j<i+N; j++) 
			S[j] ^= ('+' ^ '-');

		uses++;
	}
	
	
	for (char c : S) if (c != '+') return -1;
	
	return uses;
}

int main(void) {
	int num_test;
	cin>>num_test;
	
	for (int test=1; test<=num_test; test++) {
		string S;
		int N;
		cin >> S >> N;
		
		int turns = number_of_uses(S, N);
		
		cout<<"Case #"<<test<<": ";
		
		if (turns < 0) cout << "IMPOSSIBLE";
		else cout << turns;

		cout << "\n";
	}
	return 0;
}

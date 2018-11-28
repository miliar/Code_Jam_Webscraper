#include<iostream>
#include<string>
using namespace std;

bool allHappy(string s){
	for (int i = 0; i < s.size(); i++){
		if (s.at(i) =='-') return false;
	}
	return true;
}

string flip(string s, long position, long length){
	string cpy = s;
	for (long i = position; i < (position + length); i++){
		if (cpy.at(i) == '-') cpy.at(i) = '+';
		else cpy.at(i) = '-';
	}
	return cpy;
}

long countMovements(string s, long k){
	long move = 0;
	for (long i = 0; (i + k) <= s.size(); i++){
		if (s.at(i) == '-'){
			s = flip(s, i, k);
			move++;
		}
	}
	if (allHappy(s)) return move;
	return -1;
}

int main(void){
	long T, K, moves;
	string S;

	cin >> T;
	if (1 > T || T > 100) return 0;
	for (long i = 0; i < T; i++){
		cin >> S >> K;
		if (2 > S.size() || S.size() > 1000) continue; //small
		if (2 > K || K > S.size()) continue;

		moves = countMovements(S, K);

		cout << "Case #" << (i+1) << ": ";
		if (moves < 0)
			cout << "IMPOSSIBLE\n";
		else
			cout << moves << "\n";
	}
	return 0;
}

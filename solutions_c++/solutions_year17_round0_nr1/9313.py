//============================================================================
// Name        : ReadFromFile2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <list>
#include <vector>
using namespace std;

void setSAndK();
void flip(int);
bool testSuccess();

static int K = 0;
static vector<char> S;
static int flipNum = 0;

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
	  flipNum = 0;
	  setSAndK();
	  // Test if valid S and K
	  for (int j = 0; j < S.size() - K + 1; j++) {
		  if (S[j] == '-'){
			  flip(j);
			  flipNum++;
		  }
	  }

	  if (testSuccess()) cout << "Case #" << i << ": " << flipNum << endl;
	  if (!testSuccess()) cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
  }

  return 0;
}

bool testSuccess(){
	bool test = true;
	for (int i = 0; i < S.size(); i++) {
		if (S[i] == '-') test = false;
	}
	return test;
}

void flip(int startIndex){
	for (int i = 0; i < K; i++){
		if (S[startIndex] == '+') {
			S[startIndex] = '-';
		}
		else if (S[startIndex] == '-'){
			S[startIndex] = '+';

		}
		startIndex++;
	}
}

void setSAndK(){
	string p_S;
	int i = 0;
	S.clear();

	cin >> p_S;
	vector<char> tempS(p_S.begin(), p_S.end());
	S = tempS;
	cin >> K;

}

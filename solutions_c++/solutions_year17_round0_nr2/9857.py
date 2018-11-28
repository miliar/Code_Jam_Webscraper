//============================================================================
// Name        : ReadFromFile2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void N_to_Vector(long long int);
bool isTidy(long long int);

static vector<int> DIGITS;
static vector<int> N_after_Sort;


int main() {
  int T;
  long long int N;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
	  cin >> N;
	  while (!isTidy(N)){
		  N -= 1;
	  }

	  cout << "Case #" << i << ": " << N << endl;
  }
  return 0;
}

bool isTidy(long long int N){
	N_after_Sort.clear();

	N_to_Vector(N);
	N_after_Sort = DIGITS;
	sort (N_after_Sort.begin(), N_after_Sort.end());
	return DIGITS == N_after_Sort;
}

void N_to_Vector(long long int p_N){
  DIGITS.clear();

  if (0 == p_N) {
	  DIGITS.push_back(0);
  } else {
	while (p_N != 0) {
	  int last = p_N % 10;
	  DIGITS.push_back(last);
	  p_N = (p_N - last) / 10;
	}
	reverse(DIGITS.begin(), DIGITS.end());
  }

}

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <windows.h>


using namespace std;

/*
	This 'smart' function does following 2 jobs:
		1. It checks if a given number is a 'tidy' one or not and return true/false accordingly.
		2. If false, it gives a clue on next potential candidate to be checked for 'tidiness'
*/

bool is_a_tidy_num(long long &N) {
	long long temp;
	short d_unit_position, d_tens_position, no_of_digits_removed = 0;

	temp = N; d_unit_position = temp % 10;
	do {
		temp /= 10;
		no_of_digits_removed++;

		d_tens_position = temp % 10;
		if(d_tens_position > d_unit_position) {
			N = (temp * (long long)pow(10, no_of_digits_removed)) - 1; // move to next lower possible candidate
			return false;
		}
		d_unit_position = d_tens_position;
	} while (temp > 0);
	return true;
}

int main() {
	int T;
	long long N;
	cin>>T;

	for(int i=1; i<=T; i++) {
		cin>>N;
		while(false == is_a_tidy_num(N));
		cout<<"Case #"<<i<<": "<<N<<endl;
	}
	return 0;
}
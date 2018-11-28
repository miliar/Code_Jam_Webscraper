#include <cmath>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <vector>
#include <string>

using namespace std;


int main(){

	int NumberOfTestCases, i, j, k, prev, curr, NumLength;
	scanf("%d", &NumberOfTestCases);
	cin.get();

	for (i = 1; i <= NumberOfTestCases; i++){
		std::string N;
		getline(cin, N);
		NumLength = N.length();
		prev = (int) N[NumLength-1] - '0';

		for (j = NumLength-2; j >= 0; j--){
			curr = N[j] - '0';
			if (prev < curr){
				N[j] = (char) ((curr - 1) + '0');
				curr--;
				for (k = j + 1; k < NumLength; k++)
					N[k] = '9';
			}
			prev = curr;
		}
		N.erase(0, min(N.find_first_not_of('0'), N.size()-1));
		printf("Case #%d: ", i);
		cout << N << '\n';
	}

	

	return 0;
}
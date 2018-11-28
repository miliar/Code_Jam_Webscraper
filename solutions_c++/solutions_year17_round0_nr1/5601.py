// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include<algorithm>
#include<string>
#include<fstream>
#include<vector>

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream input("A-large.in");
	std::ofstream output("A-large.out");
	int t,k;
	std::string s;
	input >> t;
	for (int i = 0; i < t; ++i){
		input >> s >> k;
		int count = 0;
		bool impossible = false;
		for (size_t j = 0; j < s.length(); ++j){
			if (s[j] == '-'){
				if (j + k>s.length()){
					impossible = true;
					break;
				}
				++count;
				for (int m = 0; m < k; ++m){
					s[j + m] = (s[j + m] == '+') ? '-' : '+';
				}
			}
		}
		output << "Case #" << i + 1 << ": ";
		if (impossible){
			output << "IMPOSSIBLE" << std::endl;
		}
		else{
			output << count << std::endl;
		}
	}
	input.close();
	output.close();

	//getchar();
	return 0;
}


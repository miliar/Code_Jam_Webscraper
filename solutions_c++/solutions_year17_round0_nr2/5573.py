// ProblemB.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include<algorithm>
#include<string>
#include<fstream>
#include<vector>

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream input("B-large.in");
	std::ofstream output("B-large.out");
	int t;
	
	std::string s;
	input >> t;
	for (int i = 0; i < t; ++i){
		input >> s;
		
		for (int j = s.length() - 2; j >= 0; --j){
			if (s[j]>s[j + 1]){
				--s[j];
				for (size_t kk = j+1; kk < s.length(); ++kk){
					s[kk] = '9';
				}
			}
		}
		while (s[0] == '0'){
			s = s.substr(1, s.length() - 1);
		}
		output << "Case #" << i + 1 << ": "<<s;
		output << std::endl;
	}
	input.close();
	output.close();

	//getchar();
	return 0;
}

// ProblemC.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include<algorithm>
#include<string>
#include<fstream>
#include<vector>
#include<queue>
#include<list>
#include<functional>

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream input("C-small-1-attempt3.in");
	std::ofstream output("C-small-1-attempt3.out");
	int t;
	int k, n;
	input >> t;
	int* lst = new int[1000001];
	for (int i = 0; i < t; ++i){
		int in1 = 0, in2 = 0;
		input >> n >> k;
		lst[++in2] = n;
		int maxr, minr;
		for (int j = 1; j <= k; ++j){
			int temp = lst[++in1];
			if (temp == 0){
				maxr = 0;
				minr = 0;
				break;
			}
			--temp;

			minr = temp / 2;
			maxr = temp - minr;
			lst[++in2] = maxr;
			for (int tempin = in2 - 1; tempin > in1; --tempin){
				if (lst[tempin] > lst[tempin - 1]){
					std::swap(lst[tempin], lst[tempin - 1]);
				}
				else{
					break;
				}
			}
			lst[++in2] = minr;
			for (int tempin = in2 - 1; tempin > in1; --tempin){
				if (lst[tempin] > lst[tempin - 1]){
					std::swap(lst[tempin], lst[tempin - 1]);
				}
				else{
					break;
				}
			}
		}
		std::cout <<i+1<<" "<< n << " " << k << std::endl;// " " << maxr << " " << minr << std::endl;
		output << "Case #" << i + 1 << ": ";
		output << maxr << " " << minr;
		output << std::endl;
	}
	input.close();
	output.close();

	getchar();
	return 0;
}



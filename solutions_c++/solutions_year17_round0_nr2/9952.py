// codejam_b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <string>

std::string is_accending(__int64 N)
{
	std::string temp;
	bool not_tidy = true;
	if (N < 10)
	{
		return std::to_string(N);
	}
	for (size_t i = N; (i > 0) && not_tidy; i--)
	{
		temp = std::to_string(i);
		not_tidy = false;
		for (size_t j = 0; j < temp.size() - 1; j++)
		{
			if (!(temp.at(j) <= temp.at(j + 1)))
			{
				not_tidy = true;
				break;
			}
		}
	}
	return temp;
}

int main()
{
	//open files
	std::ifstream in;
	std::ofstream out;
	std::string in_filename = "\0";
	std::cin >> in_filename;
	in.open(in_filename);
	out.open("output.txt");
	int T = 0;
	int N = 0;
	in >> T;
	if (in.is_open())
	{
		for (size_t i = 0; i < T; i++)
		{
			in >> N;
			out << "Case #" << i + 1 << ": " <<  is_accending(N) <<std::endl;
		}
		return 0;
	}
	else
	{
		printf("error, input file doesnt exit!");
		return -1;
	} 
}


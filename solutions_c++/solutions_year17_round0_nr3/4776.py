// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <queue>
#include <functional>

using namespace std;


template<typename T> void print_queue(T& q) {
	while (!q.empty()) {
		std::cout << q.top() << " ";
		q.pop();
	}
	std::cout << '\n';
}

void print(uint64_t i, uint64_t max, uint64_t min, ofstream& outputf)
{
	outputf << "Case #" << i << ": " << max << " " << min << std::endl;
	cout << "Case #" << i << ": " << max << " " << min << std::endl;
}
void decimalToBinary(vector<int>* binary, uint64_t decimal)
{

	std::string::reverse_iterator iter;
	uint64_t remainder;
	
	while (decimal > 0)
	{
		remainder = decimal % 2;

		if (remainder == 0)
			binary->push_back(0);
		else if (remainder == 1)
			binary->push_back(1);

		decimal /= 2;
	}
	/*
	for (iter = binary.rbegin(); iter != binary.rend(); iter++)
	{
		newBinary.push_back(*iter);
	}*/
}

uint64_t solverbad(uint64_t r, uint64_t p)
{
	if (p == 1)
	{
		return r;
	}
	uint64_t vagasSzam = floor(log2(p));
	r -= vagasSzam;
	uint64_t db = pow(2, vagasSzam);
	uint64_t a, b;
	if (r % db == 0)
	{
		a = b = r / db;
	}
	else
	{
		b = (r - r%db) / db;
		a = b + 1;
	}
	uint64_t x;
	if (a == b)
	{
		x = db/2;
	}
	else
	{
		x = (r - db*b) / (a - b);
	}
	p -= pow(2, vagasSzam) - 1;
	if (x > p)
	{
		return a;
	}
	else
	{
		return b;
	}
	return vagasSzam;
}

pair< uint64_t, uint64_t> solver(uint64_t r, uint64_t p)
{

	vector<uint64_t> q;
	vector<uint64_t> nextQ;
	nextQ.push_back(r);
	int i = 0;
	while (i < p - 1)
	{
		q.insert(q.end(), nextQ.begin(), nextQ.end());
		std::sort(q.begin(), q.end());
		nextQ.clear();
		while (!q.empty() && i < p-1)
		{
			uint64_t max = q.at(q.size()-1);
			q.pop_back();
			if (max % 2 == 1)
			{
				max = (max - 1) / 2;
				nextQ.push_back(max);
				nextQ.push_back(max);
			}
			else
			{
				max = max / 2;
				nextQ.push_back(max);
				nextQ.push_back(--max);
			}
			i++;
		}
	}
	uint64_t min;
	if (q.empty())
	{
		std::sort(nextQ.begin(), nextQ.end());
		min = nextQ.at(nextQ.size() - 1);
	}
	else
	{
		std::sort(q.begin(), q.end());
		min = q.at(q.size() - 1);
	}
	if (min % 2 == 0)
	{
		return{ min / 2, min / 2 - 1 };
	}
	else
	{
		uint64_t a = (min - 1) / 2;
		return{ a, a };
	}
}
int main() {
	string line;
	string name = "C-small-2-attempt1";
	ifstream myfile(name + ".in");
	ofstream outputf(name + ".out");
	uint64_t i = 0;
	if (myfile.is_open() && outputf.is_open())
	{
		getline(myfile, line);
		while (getline(myfile, line))
		{
			i++;
			istringstream lineStream(line);
			string s;
			getline(lineStream, s, ' ');
			uint64_t roomNumber = std::strtoull(s.c_str(), NULL, 0);
			getline(lineStream, s, ' ');
			uint64_t people = std::strtoull(s.c_str(), NULL, 0);
			pair<uint64_t, uint64_t> p = solver(roomNumber,people);
			print(i, p.first, p.second, outputf);
		}
		myfile.close();
	}

	else cout << "Unable to open file";

	return 0;
}




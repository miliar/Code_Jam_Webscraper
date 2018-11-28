#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

bool isTidy(long long num)
{
	std::stringstream ss;
	ss << num;
	std::string str;
	ss >> str;

	for (int i = 0; i < str.size() - 1; ++i)
	{
		if (str[i] > str[i + 1])
			return false;
	}

	return true;
}

long long calc(long long n)
{

	while (n > 0)
	{
		if (isTidy(n))
			return n;
		n--;
	}

	return 0;
}

void main()
{
	std::ifstream in("input.txt");
	std::ofstream out("out.txt");

	std::string line;
	std::getline(in, line);

	int numTestCases = 0;
	std::stringstream ss;
	ss << line;
	ss >> numTestCases;

	std::cout << "Number of testcases: " << numTestCases << "\n";

	for (int i = 0; i < numTestCases; ++i)
	{
		int testCaseNum = i + 1;

		

		std::getline(in, line);
		ss.clear();

		long long n;
		ss << line;
		ss >> n;

		std::cout << "Solving testcase #" << testCaseNum << ", n=" << n << "\n";

		//std::cout << numStalls << " " << numPeople << "\n";std::string line;

		long long lastTidyNumber = calc(n);

		std::cout << "Case #" << testCaseNum << ": " << lastTidyNumber << "\n";
		out << "Case #" << testCaseNum << ": " << lastTidyNumber << "\n";


	}

	out.close();

	std::cout << "Done!";

	getchar();
}
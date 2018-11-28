#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
using std::cin;
using std::cout;

#include <fstream>
using std::ifstream;
using std::ofstream;

#include <vector>
using std::vector;

#include <string>
using std::string;

void problemB();

int main()
{
	problemB();

	return 0;
}

void problemB()
{
	ifstream infile("file.in");
	int num_tests = 0;
	vector<long long> ns;

	if (infile.is_open())
	{
		string buffer;
		infile >> num_tests;
		for (int i = 0; i < num_tests; i++)
		{
			infile >> buffer;
			ns.push_back(atoll(buffer.c_str()));
		}
		infile.close();
	}

	ofstream outfile("file.out");

	if (outfile.is_open())
	{
		for (int i = 0; i < num_tests; i++)
		{
			int last_tidy = 0;

			for (long long j = ns[i]; j >= 0; j--)
			{
				char * num = new char[32];
				char * start = num;
				sprintf(num, "%lld", j);
				int length = strlen(num);
				cout << num << "\n";

				int max = 0;
				int count = 0;
				bool tidy = true;

				while (*num != 0)
				{
					count++;
					if ((*num - 48) >= max)
						max = *num - 48;
					else
					{
						tidy = false;
						*num = 0;
					}
					num++;
				}

				if (tidy)
				{
					last_tidy = j;
					j = -1;
				}
				num = start;
				delete[] num;
			}

			outfile << "Case #" << i+ 1 << ": " << last_tidy << "\n";
		}

		outfile.close();
	}
}
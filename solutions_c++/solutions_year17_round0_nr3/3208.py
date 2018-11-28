// CPP file
// Created in Microsoft VS2017 Community  

#include <algorithm>
#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>


using namespace std;


int get_power(long long number)
{
	int ret = 0;
	while (number > 0)
	{
		number >>= 1;
		++ret;
	}

	return ret;
}

int main()
{
	int T = 0; // test cases
	vector<long long> Ns;
	vector<long long> Ks;
	vector<pair<long long, long long>> results;

	string sFileName = "C-large";

	//--------------------- begin - reading from file ---------------------
	FILE *stream;

	if (fopen_s(&stream, (sFileName + ".in").c_str(), "r"))
	{
		cout << "File does not exist" << endl;
	}
	else
	{
		fscanf_s(stream, "%d", &T); // "%ld"   "%f"   "%c"

		for (int idx = 0; idx < T; ++idx)
		{
			// reading data for each test case
			long long temp_n = 0;
			fscanf_s(stream, "%lld", &temp_n);
			Ns.push_back(temp_n);
			long long temp_k = 0;
			fscanf_s(stream, "%lld", &temp_k);
			Ks.push_back(temp_k);
		}

		// closing file
		fclose(stream);
	}
	//--------------------- end - reading from file -----------------------


	//--------------------- begin - algorithm ---------------------
	for (int idx = 0; idx < T; ++idx)
	{
		if (Ns[idx] == Ks[idx])
		{
			results.push_back(make_pair(0,0));
		}
		else
		{
			int power = get_power(Ks[idx]);
			long long two_power = 1LL << power;
			long long res = (Ns[idx] - Ks[idx]) / two_power;

			long long maximum = res;
			long long minimum = res;

			// if >= 0.5 add +1 to maximum
			long long mod_res = (Ns[idx] - Ks[idx]) % two_power;

			if (mod_res * 2 >= two_power)
			{
				++maximum;
			}

			results.push_back(make_pair(maximum,minimum));
		}
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (int idx = 0; idx < T; ++idx)
	{
		out << "Case #" << idx + 1 << ": " << results[idx].first << " " << results[idx].second << endl;
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}

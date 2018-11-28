#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
using namespace std;

long long max(long long k, long long n)
{
	if (k == 1)
		return n >> 1;
	else
	{
		long long kLog2 = (long long)floor(log2(k));
		return ((1i64 << kLog2) + n - k) >> (1 + kLog2);
	}
}

long long min(long long k, long long n)
{
	return max(k, n - (1i64 << (long long)floor(log2(k))));
}

int main(int argc, char** argv)
{
	if (argc < 2)
	{
		cout << "Not enough arguments" << endl;
		return EXIT_FAILURE;
	}
	ifstream file(argv[1]);
	if (!file.is_open())
	{
		cout << "Error: could not read file: " << argv[1] << endl;
		return EXIT_FAILURE;
	}

	int T;
	file >> T;

	string fileName = "output.txt";
	ofstream output(fileName, ios::out | ios::trunc);
	if (!output.is_open())
	{
		cout << "Error: could not write file: " << fileName.c_str() << endl;
		return EXIT_FAILURE;
	}
	for (int i = 0; i < T; i++)
	{
		long long N, K;
		file >> N >> K;
		output << "Case #" << i + 1 << ": " << max(K, N) << " " << min(K, N) << endl;
	}
	output.close();
	file.close();
	cout << "Done\n";
	return EXIT_SUCCESS;
}
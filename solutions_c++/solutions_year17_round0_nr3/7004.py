#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct infos
{
	long long int N;
	long long int K;
};

int T;

vector<infos> v;
vector<long long int> csoportok;

void beOlvas()
{
	ifstream inputFile("input.in");
	inputFile >> T;

	for(int i = 0; i < T; i++)
	{
		v.push_back(infos());

		inputFile >> v[i].N;
		inputFile >> v[i].K;
	}
}

inline void megHataroz(long long int &lS, long long int &rS, long long int stalls, long long int people)
{
	do
	{
		csoportok.push_back(stalls / 2);
		csoportok.push_back((stalls - 1) / 2);

		if(people > 1)
		{
			auto minmax = minmax_element(csoportok.begin(), csoportok.end());
			
			stalls = csoportok[minmax.second - csoportok.begin()];
			csoportok.erase(minmax.second);
		}

		people -= 1;

	}while(people > 0);

	rS = csoportok[csoportok.size() - 2];
	lS = csoportok[csoportok.size() - 1];
}

void kiIr()
{
	ofstream outputFile;
	outputFile.open("output.out");

	long long int lS;
	long long int rS;

	for(int i = 0; i < T; i++)
	{
		if(v[i].N == v[i].K)
		{
			outputFile << "Case #" << i + 1 << ": " << 0 << " " << 0 << endl;
		}
		else if(v[i].K == 1)
		{
			outputFile << "Case #" << i + 1 << ": " << v[i].N / 2 << " " << (v[i].N - 1) / 2 << endl;
		}
		else
		{
			csoportok.clear();
			megHataroz(lS, rS, v[i].N, v[i].K);

			outputFile << "Case #" << i + 1 << ": " << max(rS, lS) << " " << min(rS, lS) << endl;
		}
	}
}

int main(int argc, char const *argv[])
{
	beOlvas();
	kiIr();

	return 0;
}
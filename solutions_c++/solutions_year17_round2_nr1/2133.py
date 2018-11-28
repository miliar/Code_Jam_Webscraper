
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdint.h>
#include <algorithm>
#include <iomanip>

using namespace std;


class Loader
{
public:
	Loader()
	{

	}


	static vector<vector<uint64_t>> load(string path)
	{
		ifstream file;
		file.open(path);
		int numberOfEntries;
		vector<vector<uint64_t>> ret;

		file >> numberOfEntries;
		
		for (int i = 0; i < numberOfEntries; i++)
		{
			int destination, noHorses;
			file >> destination;
			file >> noHorses;

			vector<uint64_t> set;
			set.push_back(destination);

			for (int j = 0; j < noHorses; j++)
			{
				uint64_t tmpPos, tmpVel;
				file >> tmpPos;
				file >> tmpVel;
				set.push_back(tmpPos);
				set.push_back(tmpVel);
			}

			ret.push_back(set);
		}
		return ret;
	}
};



int main(int argc, char **args)
{
	char buf[100];
	vector<vector<uint64_t>> sets = Loader::load("F:\\Downloads\\A-large.in");

	ofstream outFile;
	outFile.open("F:\\out.txt");

	for (int i = 0; i < sets.size(); i++)
	{
		outFile << "Case #" << i + 1 << ": ";
		vector<uint64_t> active = sets.at(i);

		long double largestTimeOfArrival = -1;
		for (int j = 1; j < active.size(); j += 2)
		{
			long double delta = active.at(0) - active.at(j);
			long double time = delta / active.at(j + 1);

			if (largestTimeOfArrival < time)
				largestTimeOfArrival = time;
			
		}

		outFile << setprecision(6) << fixed << (long double)active.at(0)/largestTimeOfArrival << endl;
	}

	cout << "DONE";
	cin >> buf;
	outFile.close();
    return 0;
}

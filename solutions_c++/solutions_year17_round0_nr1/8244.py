
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdint.h>
#include <algorithm>

using namespace std;

class Set
{
public: 
	string panCakes;
	int size;
};

class Loader
{
public:
	Loader()
	{

	}

	static vector<Set> load(string path)
	{
		ifstream file;
		file.open(path);
		int numberOfEntries;
		vector<Set> ret;

		file >> numberOfEntries;
		
		for (int i = 0; i < numberOfEntries; i++)
		{
			Set tmpSet;
			file >> tmpSet.panCakes;
			file >> tmpSet.size;
		

			ret.push_back(tmpSet);
		}
		return ret;
	}
};

string flipAt(string toFlip, int index, int size)
{

	for (int i = index; i < index + size; i++)
	{
		toFlip[i] = (toFlip[i] == '-' ? '+' : '-');
	}

	return toFlip;
}

bool isHappy(string pancakes)
{
	for (int i = 0; i < pancakes.size(); i++)
	{
		if (pancakes[i] != '+')
		{
			return false;
		}
	}
	return true;
}

int main(int argc, char **args)
{
	char buf[100];
	vector<Set> sets = Loader::load("F:\\Downloads\\A-large.in");
	ofstream outFile;
	outFile.open("F:\\out.txt");

	for (int i = 0; i < sets.size(); i++)
	{
		outFile << "Case #" << i + 1 << ": ";
		Set active = sets[i];
		int flips = 0;
		for (int j = 0; j < active.panCakes.size() - active.size + 1; j++)
		{
			if (active.panCakes[j] == '-')
			{
				active.panCakes = flipAt(active.panCakes, j, active.size);
				flips++;
			}
		}
		if (isHappy(active.panCakes))
			outFile << flips << endl;
		else
			outFile << "IMPOSSIBLE" << endl;
	}
	outFile.close();
    return 0;
}



#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdint.h>
#include <algorithm>
#include <iomanip>

using namespace std;

enum Colors{N, R, O, Y, G, B, V};
string colorChars = "NROYGBV";

class Loader
{
public:
	Loader()
	{

	}


	static vector<vector<int>> load(string path)
	{
		ifstream file;
		file.open(path);
		int numberOfEntries;
		vector<vector<int>> ret;

		file >> numberOfEntries;
		
		for (int i = 0; i < numberOfEntries; i++)
		{
			int noUnicorns;

			file >> noUnicorns;

			vector<int> set;
			set.push_back(noUnicorns);

			for (int j = 0; j < 6; j++)
			{
				uint64_t col;
				file >> col;
				set.push_back(col);
			}

			ret.push_back(set);
		}
		return ret;
	}
};

int getIndexOfHeighest(vector<int> s)
{
	int tmp = -1;
	int highest;

	for (int i = 1; i < 7; i++)
	{
		if (s[i] > tmp)
		{
			tmp = s[i];
			highest = i;
		}
	}
	return highest;
}


int main(int argc, char **args)
{
	char buf[100];
	vector<vector<int>> sets = Loader::load("F:\\Downloads\\B-small-attempt0.in");

	ofstream outFile;
	outFile.open("F:\\out.txt");

	for (int i = 0; i < sets.size(); i++)
	{
		outFile << "Case #" << i + 1 << ": ";
		vector<int> active = sets.at(i);
		
		string out;

		//enum Colors{N, R, O, Y, G, B, V};
		//string colorChars = "0NROYGBV";

		if (active.at(O) > active.at(B) * 2 || active.at(V) > active.at(Y) * 2 || active.at(G) > active.at(R) * 2)
		{
			outFile << "IMPOSSIBLE" << endl;
			continue;
		}
		else if (active.at(R) > active.at(N) - active.at(R) || active.at(B) > active.at(N) - active.at(B) || active.at(Y) > active.at(N) - active.at(Y))
		{
			outFile << "IMPOSSIBLE" << endl;
			continue;
		}
		else
		{
			int circleSize = active.at(getIndexOfHeighest(active));
			for (int k = 0; k < circleSize; k++)
			{
				out.push_back(colorChars[getIndexOfHeighest(active)]);
				
			}
			active[getIndexOfHeighest(active)] = 0;

			int posInCircle = 0;
			int lap = 2;

			for (int k = 0; k < active.at(getIndexOfHeighest(active)); k++)
			{
				out.insert(out.begin() + posInCircle*2, colorChars[getIndexOfHeighest(active)]);
				posInCircle++; 
				if (posInCircle == circleSize)
				{
					posInCircle = 0;
					lap++;
				}
			}
			active[getIndexOfHeighest(active)] = 0;

			for (int k = 0; k < active.at(getIndexOfHeighest(active)); k++)
			{
				out.insert(out.begin() + posInCircle*lap, colorChars[getIndexOfHeighest(active)]);
				posInCircle++;
				if (posInCircle == circleSize)
				{
					posInCircle = 0;
					lap++;
				}
			}
		}
		outFile << out << endl;
	}

	cout << "DONE";
	cin >> buf;
	outFile.close();
    return 0;
}

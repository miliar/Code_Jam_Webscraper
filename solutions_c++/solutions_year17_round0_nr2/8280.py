
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdint.h>

using namespace std;


class Loader
{
public:
	Loader()
	{

	}

	static vector<uint64_t> load(string path)
	{
		ifstream file;
		file.open(path);
		int numberOfEntries;
		vector<uint64_t> ret;

		file >> numberOfEntries;
		
		for (int i = 0; i < numberOfEntries; i++)
		{
			uint64_t tmp;
			file >> tmp;
			ret.push_back(tmp);
		}
		return ret;
	}
};

bool isTidy(uint64_t number)
{
	string toCheck = std::to_string(number);
	
	for (int i = 0; i < toCheck.size() - 1; i++)
	{
		if (toCheck.at(i) > toCheck.at(i+1))
		{
			return false;
		}
	}
	return true;
}

string constructBiggestTidy(uint64_t number)
{
	string chk = std::to_string(number);
	string ret("");
	


	for (int i = 0; i < chk.size() - 1; i++)
	{
		if (chk[i] > chk[i + 1])
		{
			chk[i] -= 1;
			for (int k = i + 1; k < chk.size(); k++)
			{
				chk[k] = '9';
			}
		}
	}
	return chk;
}

int main(int argc, char **args)
{
	char buf[100];
	vector<uint64_t> sets = Loader::load("F:\\Downloads\\B-small-attempt1.in");
	ofstream outFile;
	outFile.open("F:\\out.txt");

	for (int i = 0; i < sets.size(); i++)
	{
		outFile << "Case #" << i + 1 << ": ";
		outFile << stol(constructBiggestTidy(sets.at(i))) << endl;
	}
	outFile.close();
	cout << "\nComputation Done\n";
    return 0;
}


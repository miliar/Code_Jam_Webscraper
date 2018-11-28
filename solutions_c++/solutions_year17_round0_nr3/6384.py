
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include <stdint.h>
#include <algorithm>

using namespace std;


class Loader
{
public:
	Loader()
	{

	}


	static vector<pair<uint64_t, uint64_t>> load(string path)
	{
		ifstream file;
		file.open(path);
		int numberOfEntries;
		vector<pair<uint64_t, uint64_t>> ret;

		file >> numberOfEntries;
		
		for (int i = 0; i < numberOfEntries; i++)
		{
			pair<uint64_t, uint64_t> tmpSet;
			file >> tmpSet.first;
			file >> tmpSet.second;
			ret.push_back(tmpSet);
		}
		return ret;
	}
};


class Level
{
public:
	pair<uint64_t, uint64_t> noOfElements;
	pair<uint64_t, uint64_t> smaller;
	pair<uint64_t, uint64_t> bigger;
};

pair<uint64_t, uint64_t> computeFirstOf(uint64_t number)
{
	pair<uint64_t, uint64_t> ret;
	number--;
	ret.first = number / 2;
	ret.second = number / 2 + number % 2;
	return ret;
}

pair<uint64_t, uint64_t> computeSmallerAtLevel(int level, uint64_t number)
{
	pair<uint64_t, uint64_t> last = computeFirstOf(number);
	for (int i = 0; i < level; i++)
	{
		last = computeFirstOf( last.first < last.second ? last.first : last.second);
	}
	return last;
}

pair<uint64_t, uint64_t> computeBiggerAtLevel(int level, uint64_t number)
{
	pair<uint64_t, uint64_t> last = computeFirstOf(number);
	for (int i = 0; i < level; i++)
	{
		last = computeFirstOf(last.first > last.second ? last.first : last.second);
	}
	return last;
}

uint64_t computeSmallerAmountAtLevel(int level, uint64_t number)
{
	pair<uint64_t, uint64_t> last = computeFirstOf(number);

	uint64_t tmp = number - powl(2, level) + 1;

	
	if (tmp <= powl(2, level))
	{
		tmp = tmp % (int64_t)powl(2, level);
	}
	else
	{
		tmp = (int64_t)powl(2, level) - tmp % (int64_t)powl(2, level);
	}
	

	return tmp;
}

uint64_t globalIndexToLevelIndex(uint64_t index)
{
	int elementDepth = log2(index);
	int local = index - powl(2, elementDepth) + 1;
	return local;
}

int main(int argc, char **args)
{
	char buf[100];
	vector<pair<uint64_t, uint64_t>> sets = Loader::load("F:\\Downloads\\C-small-2-attempt0.in");

	ofstream outFile;
	outFile.open("F:\\out.txt");

	for (int i = 0; i < sets.size(); i++)
	{
		outFile << "Case #" << i + 1 << ": ";
		pair<uint64_t, uint64_t> active = sets.at(i);
		int maxDepth = log2(active.first);
		int elementDepth = log2(active.second);

		if (maxDepth == elementDepth)
		{
			outFile << 0 << " " << 0 << endl;
			continue;
		}
		
		int smallerAmount = computeSmallerAmountAtLevel(elementDepth, active.first);
		int localElementIndex = globalIndexToLevelIndex(active.second);
		uint64_t elementsAtLevel = pow(2, elementDepth);
		uint64_t biggerAmount = elementsAtLevel - smallerAmount;


		cout << "sm: " << smallerAmount << " bm: " << biggerAmount << " gei: " << active.second << " lei: " << localElementIndex << " max: " << maxDepth << " elD: " << elementDepth << endl;



		pair<uint64_t, uint64_t> ret = biggerAmount >= localElementIndex ? computeBiggerAtLevel(elementDepth, active.first) : computeSmallerAtLevel(elementDepth, active.first);
		
		cout << ret.second << " " << ret.first << endl;
		outFile << ret.second << " " << ret.first << endl;

	}
	cin >> buf;
	outFile.close();
    return 0;
}

/*
uint64_t mult = 1;
uint64_t absolutes = 0;
int tmpMult = 0;
bool lastSame = false;

for (int i = 0; i < level; i++)
{
if (last.first == last.second)
{
mult *= 2 + tmpMult;
lastSame = true;
}
else
lastSame = false;


pair<uint64_t, uint64_t> tmp = computeFirstOf(last.second);
last = computeFirstOf(last.first);

if (!lastSame && tmp.first == last.first)
mult *= 2;
}*/
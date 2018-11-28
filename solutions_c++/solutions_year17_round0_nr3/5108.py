#include <iostream>
#include <string>
#include <cassert>
#include <queue>
#include <vector>
using namespace std;

#define min(a, b) ((a < b) ? a : b)

void processTestCasePan(int caseNr);
void processTestCaseTidy(int caseNr);
void processTestCaseBath(int caseNr);
void processTestCaseBathFast(int caseNr);

void main()
{
	int n = 0;

	cin >> n;

		for (int i = 0; i < n; i++)
	{
		//processTestCasePan(i);
		//processTestCaseTidy(i+1);
		//processTestCaseBath(i + 1);
		processTestCaseBathFast(i + 1);
	}

	//cin >> kkt;
}

void processTestCasePan(int caseNr)
{
	string input = "";
	getline(cin, input);

	int pos = input.find_last_of(' ');

	if (pos == 0)
	{
		cout << "Case #" << caseNr << ": 0" << endl;
		return;
	}

	int panSize = pos;
	int k = stoi(input.substr(pos + 1));
	char c = 'X';
	int leftMin = 0;
	int leftPlus = 0;
	int rightMin = 0;
	int rightPlus = 0;

	int flips = 0;

	for (int i = 0; i < panSize; i++)
	{
		c = input[i];
		if (c == '+')
		{
			leftPlus++;
			continue;
		}

		if (c == '-')
		{
			// pancake problem!
		}
	}

	cout << "Case #" << caseNr << ": " << flips << endl;
}

void processTestCaseTidy(int caseNr)
{
	string input = "";
	//getline(cin, input);
	cin >> input;
	int actualSize = input.size();
	int ninesFromHere = -1;

	if (actualSize <= 1)
	{
		cout << "Case #" << caseNr << ": " << input << endl;
		return;
	}

	bool minusOne = false;
	char now = input[actualSize - 1];
	for (int i = actualSize - 2; i >= 0; i--)
	{
		char next = input[i];

		if (minusOne)
		{
			if (next == '0')
			{
				ninesFromHere = i;
				now = '9';
				continue;
			}
			else
			{
				minusOne = false;
				next--;
				input[i]--;
			}
		}

		if (next > now)
		{
			if (ninesFromHere != -1)
			{
				ninesFromHere = min(i + 1, ninesFromHere);
			}
			else
			{
				ninesFromHere = i + 1;
			}

			if (next == '0')
			{
				ninesFromHere = i;
				minusOne = true;
				now = '9';
				continue;
			}
			else
			{
				next--;
				input[i]--;
			}
		}

		now = next;
	}

	if (ninesFromHere != -1)
	{
		for (int i = ninesFromHere; i < actualSize; i++)
		{
			input[i] = '9';
		}
	}

	int firstNonZero = 0;
	for (; firstNonZero < actualSize; firstNonZero++)
	{
		if (input[firstNonZero] != '0')
		{
			break;
		}
	}

	cout << "Case #" << caseNr << ": " << input.substr(firstNonZero) << endl;
}

struct SubdivInfo
{
	unsigned long long size;
	unsigned long long count;

	SubdivInfo(unsigned long long osize, unsigned long long ocount) : size(osize), count(ocount) {}
};

class SubdivCompare
{
public:
	bool operator() (SubdivInfo a, SubdivInfo b)
	{
		return a.size < b.size;
	}
};

int getLargestSubdiv(vector<SubdivInfo>& from)
{
	int maxIndex = 0;
	unsigned long long maxSize = from[0].size;
	for (int i = 1; i < from.size(); i++)
	{
		if (from[i].size > maxSize)
		{
			maxIndex = i;
			maxSize = from[i].size;
		}
	}

	return maxIndex;
}

void updateOrAddSubdivInfo(vector<SubdivInfo>& from, SubdivInfo& newInfo)
{
	bool found = false;
	for (int i = 0; i < from.size(); i++)
	{
		SubdivInfo& now = from[i];
		if (now.size == newInfo.size)
		{
			now.count += newInfo.count;
			found = true;
			break;
		}
	}

	if (!found)
	{
		from.push_back(newInfo);
	}
}

void processTestCaseBath(int caseNr)
{
	unsigned long long n, k;
	cin >> n;
	cin >> k;

	vector<SubdivInfo> subdivs;
	subdivs.reserve(5);
	subdivs.push_back(SubdivInfo(n, 1));

	unsigned long long minLsRs, maxLsRs;

	for (unsigned long long i = 0; i < k; i++)
	{
		//assert(subdivs.size() < 5);
		int largestSubdivId = getLargestSubdiv(subdivs);
		SubdivInfo& largest = subdivs[largestSubdivId];
		unsigned long long largestSize = largest.size;

		if (largest.count == 1)
		{
			subdivs.erase(subdivs.begin() + largestSubdivId);
		}
		else
		{
			// multiple largest means that regardless of the type, leftmost will loose an item and get split
			largest.count--;
		}

		if (largestSize % 2 == 1) // odds split in the middle, Ls == Rs == newSize
		{
			unsigned long long newSize = (largestSize - 1) / 2;
			if (newSize > 0)
			{
				updateOrAddSubdivInfo(subdivs, SubdivInfo(newSize, 2));
			}

			minLsRs = newSize;
			maxLsRs = newSize;
		}
		else // evens will get the leftest, Ls = newSizeL, Rs = newSizeR
		{
			unsigned long long newSizeL = (largestSize / 2) - 1;
			unsigned long long newSizeR = largestSize / 2;
			if (newSizeL > 0)
			{
				updateOrAddSubdivInfo(subdivs, SubdivInfo(newSizeL, 1));
			}
			updateOrAddSubdivInfo(subdivs, SubdivInfo(newSizeR, 1));

			minLsRs = newSizeL;
			maxLsRs = newSizeR;
		}
	}

	cout << "Case #" << caseNr << ": " << maxLsRs << ' ' << minLsRs << endl;
}

void processTestCaseBathFast(int caseNr)
{
	unsigned long long n, k;
	cin >> n;
	cin >> k;

	vector<SubdivInfo> subdivs;
	subdivs.reserve(5);
	subdivs.push_back(SubdivInfo(n, 1));

	unsigned long long minLsRs, maxLsRs;

	for (unsigned long long i = 0; i < k;)
	{
		//assert(subdivs.size() < 5);
		int largestSubdivId = getLargestSubdiv(subdivs);
		SubdivInfo largest = subdivs[largestSubdivId];
		unsigned long long largestSize = largest.size;

		subdivs.erase(subdivs.begin() + largestSubdivId);
		i += largest.count;

		if (largestSize % 2 == 1) // odds split in the middle, Ls == Rs == newSize
		{
			unsigned long long newSize = (largestSize - 1) / 2;
			if (newSize > 0)
			{
				updateOrAddSubdivInfo(subdivs, SubdivInfo(newSize, 2*largest.count));
			}

			minLsRs = newSize;
			maxLsRs = newSize;
		}
		else // evens will get the leftest, Ls = newSizeL, Rs = newSizeR
		{
			unsigned long long newSizeL = (largestSize / 2) - 1;
			unsigned long long newSizeR = largestSize / 2;
			if (newSizeL > 0)
			{
				updateOrAddSubdivInfo(subdivs, SubdivInfo(newSizeL, 1 * largest.count));
			}
			updateOrAddSubdivInfo(subdivs, SubdivInfo(newSizeR, 1 * largest.count));

			minLsRs = newSizeL;
			maxLsRs = newSizeR;
		}
	}

	cout << "Case #" << caseNr << ": " << maxLsRs << ' ' << minLsRs << endl;
}
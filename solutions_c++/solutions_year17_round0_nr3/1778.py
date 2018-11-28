#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<algorithm>
#include<sstream>
#include<cstdlib>
#include<cstdio>
#include<climits>

using namespace std;

int main()
{
	int count;
	cin >> count;
	for(int i=1; i<=count; i++)
	{
		long long stalls, people;
		cin >> stalls >> people;

		stalls += 2;
		long long partitionSize = stalls - 2;
		long long numPart = 1;
		long long numPartPlus = 0;
		long long removeFactor = 1;

		//When we split, take total number of partPlus first, then Part.
		//1000 becomes 999/2 -> partSize 499, 1 part, 1 partPlus
		//999 becomes 998/2 -> partSize 499, 2 part, 0 partPlus

		while(people > removeFactor)
		{
			people -= removeFactor;
			long long newPart = 0;
			long long newPartPlus = 0;
			if(partitionSize & 0x1)
			{
				partitionSize--;
				partitionSize /= 2;
				newPart += (2 * numPart);
				newPart += numPartPlus;
				newPartPlus += numPartPlus;
			}
			else
			{
				partitionSize--;
				partitionSize /= 2;
				newPart += numPart;
				newPartPlus += numPart;
				newPartPlus += 2 * numPartPlus;
			}
			removeFactor *= 2;
			numPart = newPart;
			numPartPlus = newPartPlus;
		}
		//Solve for remaining people within the partitions.
		long long bestMax = 0, bestVal = 0;
//		cerr << "Final partition size: " << partitionSize << endl;
//		cerr << "People: " << people << " plus: " << numPartPlus << " normal: " << numPart << endl;
		if(people <= numPartPlus)
		{
			//Partition is 1 greater.
			long long choice = (partitionSize + 2) / 2;
			bestMax = max(choice-1, partitionSize + 1 - choice);
			bestVal = min(choice-1, partitionSize + 1 - choice);
		}
		else
		{
			long long choice = (partitionSize + 1) / 2;
			bestMax = max(choice-1, partitionSize - choice);
			bestVal = min(choice-1, partitionSize - choice);

		}
		cout << "Case #" << i << ": ";
		cout << bestMax << " " << bestVal;
		cout << endl;

	}

	return 0;
}

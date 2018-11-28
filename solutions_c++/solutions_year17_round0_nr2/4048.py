#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	int testCase;
	char num[20];
	int lastNum[20];
	int samecheck;
	int smallcheck;
	int startNum;
	ifstream inFile("B-small-attempt1.in");
	ofstream outFile("output.txt");
	inFile >> testCase;
	for (int i = 1; i <= testCase; i++)
	{
		samecheck = -1;
		smallcheck = -1;
		inFile >> num;
		for (int i = 0; num[i] != '\0'; i++)
			lastNum[i] = num[i] - '0';
		for (int i = 0; num[i + 1] != '\0'; i++)
		{
			if ((lastNum[i] == lastNum[i + 1]) && (samecheck == -1))
				samecheck = i;
			else if (lastNum[i] > lastNum[i + 1])
			{
				smallcheck = i;
				break;
			}
		}
		if (smallcheck != -1)
		{
			if (samecheck != -1)
			{
				lastNum[samecheck]--;
				for (int i = samecheck + 1; num[i] != '\0'; i++)
					lastNum[i] = 9;
			}
			else
			{
				lastNum[smallcheck]--;
				for (int i = smallcheck + 1; num[i] != '\0'; i++)
					lastNum[i] = 9;
			}
		}
		for (int i = 0; num[i] != '\0'; i++)
			if (lastNum[i] != 0)
			{
				startNum = i;
				if (i != 0)
					num[i - 1] = '\0';
				break;
			}
		outFile << "Case #"<<i<<": ";
		for (; num[startNum] != '\0'; startNum++)
		{
			outFile << lastNum[startNum];
			num[startNum] = '\0';
		}
		outFile << "\n";
	}
	return 0;
}
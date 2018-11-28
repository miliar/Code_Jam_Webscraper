#include <iostream>  
#include <fstream>
#include<vector>
using namespace std;

vector<int> pan;

void change(int start, int length);

void main()
{
	long long int t, m, i, count, length =0;

	char temp[100];

	ifstream inFile("A-large.in");
	ofstream outFile("test.txt");

	inFile.getline(temp, 100);
	t = atoi(temp);
	
	for (m = 1; m <= t; ++m)
	{
		char ch;
		count = 0;

		while (inFile.get(ch))
		{
			if (ch == '\n')
				break;
			else if (ch == '+')
			{
				pan.push_back(1);
			}
			else if (ch == '-')
			{
				pan.push_back(0);
			}
			else if(ch != ' ')
			{
				length = length * 10 + (ch - '0');
			}
		}

		for(i = 0; i < pan.size(); i++)
		{
			if (pan[i] == 0 && i > pan.size()-length)
			{
				//cout << "Case #" << m << ": IMPOSSIBLE" << endl;
				outFile << "Case #" << m << ": IMPOSSIBLE" << endl;
				goto outside;
			}
			if (pan[i] == 0)
			{
				change(i, length);
				count++;
			}
		}
		//cout << "Case #" << m << ": " << count <<endl;
		outFile << "Case #" << m << ": " << count << endl;
		outside:
		pan.clear();
		length = 0;
	}
}

void change(int start, int length)
{
	for (int i = start; i < length+start; i++)
	{
		if (pan[i] == 0)
			pan[i] = 1;
		else if(pan[i] == 1)
			pan[i] = 0;
	}
}
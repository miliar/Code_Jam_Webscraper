#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
	int testCase;
	ifstream input("A-large.in");
	ofstream output("answer.txt");
	string cake;
	int cutting;
	int count;
	input >> testCase;
	for (int t = 1; t <= testCase; t++)
	{
		input >> cake;
		input >> cutting;
		count = 0;
		for (int i = 0; i + cutting <= cake.length(); i++)
		{
			if (cake.at(i) == '-')
			{
				for (int j = 0; j < cutting; j++)
				{
					if (cake.at(i + j) == '+')
						cake.at(i + j) = '-';
					else
						cake.at(i + j) = '+';
				}
				count++;
			}
		}
		for (int checkNum = cake.length() - cutting + 1; checkNum < cake.length(); checkNum++)
		{
			if (cake.at(checkNum) == '-')
			{
				count = -1;
				break;
			}
		}
		if (count == -1)
			output << "Case #" << t << ": IMPOSSIBLE\n";
		else
			output << "Case #" << t << ": "<<count<<"\n";
		cake.clear();
	}
	return 0;
}
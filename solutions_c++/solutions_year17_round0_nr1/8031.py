#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

int Flip(string, int);

int main()
{
	ifstream inputFile("input.txt");
	ofstream outputFile("output.txt");
	string line;
	int T;
	int K;

	inputFile >> T;
	for(int i = 0; i < T; i++)
	{
		inputFile >> line >> K;

		int result = Flip(line, K);

		if(result == -1)
		{
			outputFile << "Case #" << i+1 << ": IMPOSSIBLE" << endl;	
		}
		else
		{
			outputFile << "Case #" << i+1 << ": " << result << endl;
		}
	}

	return 0;
}

int Flip(string aCakes, int aK)
{
	 int result = 0;
	 for(int i = 0; i < aCakes.length(); i++)
	 {
		 //뒤집을 케이크가 k보다 작음
		 if(aCakes.length() - i < aK)
		 {
			 int allHappy = 1;
			 for(int j = i; j < aCakes.length(); j++)
			 {
				 if(aCakes[j] == '-')
				 {
					 allHappy = 0;
					 break;
				 }
			 }

			 if(allHappy == 1)
				 return result;
			 else
				return -1;
		 }


		 if(aCakes[i] == '-')
		 {
			 for(int j = i; j < i+aK; j++)
			 {
				 if(aCakes[j] == '-')
				 {
					 aCakes[j] = '+';
				 }
				 else if(aCakes[j] == '+')
				 {
					aCakes[j] = '-';
				 }
			 }
			 result ++;
		 }
	 }
}
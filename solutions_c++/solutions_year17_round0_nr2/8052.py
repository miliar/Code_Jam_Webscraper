#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

int Tidy(int aN);

int main()
{
	ifstream inputFile("input.txt");
	ofstream outputFile("output.txt");
	
	int T;
	long long N;
	int K;

	inputFile >> T;
	for(int i = 0; i < T; i++)
	{
		inputFile >> N;

		int result = Tidy(N);

		outputFile << "Case #" << i+1 << ": " << result << endl;
		
	}

	return 0;
}

int Tidy(int aN)
{
	for ( int i = aN; i >= 0 ; i--)
	{
		if(i < 10) //1�ڸ�
		{
			return i;
		}
		else if(i < 100) //2�ڸ�
		{
			if(i/10 <= i%10)
				return i;
		}
		else if(i < 1000) //3�ڸ�
		{
			if(i/100 <= (i%100)/10 && (i%100)/10 <= i%10)
				return i;
		}
		else			   //4�ڸ�
		{
			//only 1000
		}
	}

	return -1;
}

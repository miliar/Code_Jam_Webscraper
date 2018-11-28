#include<iostream>
#include<fstream>
#include<string>
#include<iterator>
using namespace std;

int main()
{
	string line;
	ifstream inFile("C-small-2-attempt0.in");
	ofstream outFile("output_c_small_2.out");
	int testCases;
	if (inFile.is_open())
	{
		getline(inFile, line);
		testCases = stoi(line);
		unsigned long long N, K;
		for (int i = 0; i < testCases; i++){
			inFile >> N >> K;

			int level, multipleOfTwo = 1, reservedNumOfSlots = 0, remainingNumOfSlots, orderInLevel, result;
			while (multipleOfTwo <= K){
				reservedNumOfSlots += multipleOfTwo;
				multipleOfTwo *= 2;
			}
			level = multipleOfTwo / 2;
			reservedNumOfSlots -= level;
			remainingNumOfSlots = N - reservedNumOfSlots;
			orderInLevel = K - reservedNumOfSlots;

			if (orderInLevel <= remainingNumOfSlots%level)
				result = (remainingNumOfSlots / level) + 1;
			else
				result = remainingNumOfSlots / level;

			int min, max;
			if (result % 2 > 0)
				min = max = result / 2;
			else{
				max = result / 2;
				min = max - 1;
			}
			if (outFile.is_open())
			{
				outFile << "Case #" << i + 1 << ": " << max << " " << min << '\n';
				continue;
			}
		}
		outFile.close();
		inFile.close();
	}
	return 0;
}


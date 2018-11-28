#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;

bool isTidyNumber(string number){
	bool isTidy = true;
	for (int i = 0; i < number.size() - 1; i++)
		if (number[i] - '0' > number[i + 1] - '0'){
			isTidy = false;
			break;
		}
	return isTidy;
}
string removeLeadingZeros(string number)
{
	number.erase(0, min(number.find_first_not_of('0'), number.size() - 1));
	return number;
}
string getLargestTidyNumber(string number){
	int stopIndex;

	while (true){
		for (int k = 0; k < number.size() - 1; k++){
			if (number[k] - '0' <= number[k + 1] - '0')
				continue;
			else{
				int currDigit = number[k] - '0';
				stopIndex = k;
				if (currDigit == 0){
					currDigit = number[k - 1] - '0';
					stopIndex = k - 1;
				}

				currDigit--;
				number[stopIndex] = currDigit + '0';
				break;
			}
		}
		for (int k = stopIndex + 1; k < number.size(); k++)
			number[k] = '9';
		if (isTidyNumber(number))
			break;
	}
	return number;
}
int main()
{
	string line;
	ifstream inFile("B-large.in");
	ofstream outFile("output_large.out");
	int testCases;
	if (inFile.is_open())
	{
		getline(inFile, line);
		testCases = stoi(line);
		string number;
		for (int i = 0; i < testCases; i++){
			getline(inFile, number);
			number = removeLeadingZeros(number);
			if (isTidyNumber(number))
				if (outFile.is_open()){
					outFile << "Case #" << i + 1 << ": " << number << '\n';
					continue;
				}
			number = getLargestTidyNumber(number);
			
			number = removeLeadingZeros(number);
				if (outFile.is_open())
					outFile << "Case #" << i + 1 << ": " << number << '\n';
			
		}
		outFile.close();
		inFile.close();
	}
	return 0;
}


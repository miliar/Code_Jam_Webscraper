#include <string>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

int flipper(int k, int pos, string &lineStr)
{
	int sum = k + pos;
	for (int count = pos; count<sum;count++)
	{
		if (lineStr[count] == '-')
			lineStr[count] = '+';
		else
			lineStr[count] = '-';
	}
	return 0;
}

int main()
{
	vector<int> numbers(1000,0);
	int flips;
	string entireLine, subLine;
	string pancakes;
	int nPancakes;
	int t, k, pos;
	cin >> t;
	cin.ignore();
	int countCase = 1;
	while(t--)
	{
		flips = 0;
		entireLine = "";
		subLine = "";
		getline(cin, pancakes);
		istringstream inputStringStream(pancakes);
		inputStringStream >> entireLine;
		subLine = entireLine;
		inputStringStream >> entireLine;
		k = stoi(entireLine);
		nPancakes = subLine.length();
		int totalCount = nPancakes + 1 - k;
		for (pos = 0; pos<totalCount; pos++){
			if (subLine[pos] == '-'){
				flipper(k, pos, subLine);
				flips++;
			}
		}
		int pos = totalCount;
		bool downside = false;
		if (subLine[pos] == '-')
			downside = true;
		pos++;
		while (pos <= nPancakes && !downside) {
			if (subLine[pos] == '-')
				downside = true;
			pos++;
		}
		if (downside)
			cout<<"Case #"<<countCase<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #" << countCase << ": " << flips << endl;
		countCase++;
	}
	return 0;
}
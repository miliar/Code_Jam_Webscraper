#include <iostream>
#include <string>

using namespace std;

bool isFaceUp(string const &line)
{
	return (line.find('-') == string::npos);
}

string flipString(string const &line, int flipPos, int flipLength)
{
	string newLine = line;
	if (flipPos + flipLength > line.length())
	{
		flipPos += line.length() - flipPos - flipLength;
	}

	for (int i = flipPos; i < flipPos + flipLength; i++)
	{
		if (newLine[i] == '-') {
			newLine[i] = '+';
		} 
		else
		{
			newLine[i] = '-';
		}
	}
	return newLine;
}

int main()
{
	int T;
	cin >> T;
	for (auto i = 0; i < T; i++)
	{
		int K;
		string S;

		cin >> S;
		cin >> K;
		
		if (isFaceUp(S)) 
		{
			cout << "Case #" << i + 1 << ": 0" << endl;
			continue;;
		}

		string ModifiedS = S, LastS2 = "a";
		int flipCount = 0, possible = 1;
		while (!isFaceUp(ModifiedS))
		{
			string LastS = ModifiedS;
			ModifiedS = flipString(ModifiedS, ModifiedS.find('-'), K);
			flipCount++;
			if (LastS == ModifiedS || LastS2 == ModifiedS)
			{
				cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
				possible = 0;
				break;
			}
			LastS2 = LastS;
		}
		if (possible) cout << "Case #" << i + 1 << ": " << flipCount << endl;
	}

	return 0;
}

// CodeJam1.cpp : 定义控制台应用程序的入口点。
//


#include <iostream>
#include <string>
#include <fstream>

using namespace std;

bool PancakeFlipper(string s, int k, int& cnt)
{
	bool ret = false;
	char HappySide = '+';
	char BlankSide = '-';
	string testAllHappy;

	testAllHappy.assign(s.length(), HappySide);

	if (s.length() == 0)
	{
		ret = true;
	}
	else if (s == testAllHappy)
	{
		ret = true;
	}
	else if (s.length() == k)
	{
		string testHappy, testBlank;
		testHappy.assign(k, HappySide);
		testBlank.assign(k, BlankSide);

		if (s.compare(testHappy) == 0)
		{
			ret = true;
		}
		else if (s.compare(testBlank) == 0)
		{
			cnt += 1;
			ret = true;
		}
		else
		{
			ret = false;
		}
	}
	else if (s.length() < k)
	{
		ret = false;
	}
	else
	{
		string testByte;
		size_t pos;

		pos = s.find(BlankSide);

		if (pos + k > s.length())
			ret = false;
		else
		{
			for (int i = 0; i < k; i++)
			{
				if (s[pos + i] == HappySide)
					s[pos + i] = BlankSide;
				else
					s[pos + i] = HappySide;
			}

			cnt += 1;
		}

		pos = s.find(BlankSide);

		if (pos != string::npos)
			ret = PancakeFlipper(s.substr(pos), k, cnt);
		else
			ret = true;

	}

	return ret;
}

int main()
{
	ifstream infile("A-large.in");
	ofstream outfile;

	int caseIndex = 0;
	string line, testString;
	bool first = true;

	outfile.open("A-large.txt");
	while (getline(infile, line))
	{
		if (first)
		{
			first = false;
			continue;
		}

		++caseIndex;
		int cnt = 0;
		size_t pos = line.find(' ');

		bool ret = PancakeFlipper(line.substr(0, pos), stoi(line.substr(pos + 1, line.length() - pos - 1)), cnt);

		char* buffer = new char[32];
		sprintf(buffer, "Case #%d: ", caseIndex);
		char otherDesc[16];

		if (ret == false)
		{
			strcpy(otherDesc, "IMPOSSIBLE \n");
			strcat(buffer, otherDesc);
		}
		else
		{
			if (cnt == 0)
				sprintf(otherDesc, "0 \n");
			else
				sprintf(otherDesc, "%d \n", cnt);

			strcat(buffer, otherDesc);
		
		}
			
		outfile << buffer;

		delete[] buffer;
	}
	outfile.close();
}




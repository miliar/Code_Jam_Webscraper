#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <fstream>
#include <ctype.h>

#define MIN(x,y) ((x)<(y))?(x):(y)
#define MAX(x,y) ((x)>(y))?(x):(y)

#define rep(i,b) for(int i = 0; i < (b); i++)
#define fo(i,a,b) for(int i = (a); i < (b); i++)
#define fos(i,a,b) for(int i = (a); i < (int)(b).size(); i++)


#include <sstream>
#include <conio.h>

using namespace std;

unsigned _int64 calc()
{
	return 0;
}

int main( int argc, char* argv[] )
{
	std::fstream in;
	in.open("B-large.in", std::fstream::in);

	string line;
	getline(in, line);
	int T = atoi(line.c_str());

	std::fstream out;
	out.open("B-lage.out", std::fstream::out);

	fo(i, 0, T)
	{
		string input;
		getline(in, input);

		vector<char> number;

		for (auto symbol : input)
		{
			number.push_back(symbol - '0');
		}

		string result;

		if (number.size() > 1)
		{
			int i = 1;
			while (i < number.size())
			{
				if (number[i] >= number[i - 1])
				{
					i++;
				}
				else
				{
					i--;
					number[i] --;

					for (int j = i + 1; j < number.size(); j++)
					{
						number[j] = 9;
					}

					if (i == 0)
					{
						break;
					}
				}
			}
		}

		bool skip = true;

		for (auto symbol : number)
		{
			if (symbol == 0 && skip)
			{
				continue;
			}

			skip = false;

			char digit = '0' + symbol;

			result += digit;
		}
	
		out << "Case #" << i + 1 << ": " << result << std::endl;
	}

	in.close();

	getch();

	return 0;
}

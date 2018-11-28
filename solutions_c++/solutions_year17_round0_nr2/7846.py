#include <string>
#include <math.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <list>
#include <utility>
#include <queue>

using namespace std;
typedef long long int lli;

#define pb push_back

vector < vector<int> >grid;


int main(int argc, char* argv[])
{
	string directory = "d:\\Google Drive\\versenyek";


	if (argc > 1)
	{
		freopen((directory + "\\be.txt").c_str(), "rt", stdin);
		freopen((directory + "\\ki.txt").c_str(), "wt", stdout);
	}

	int N,TT,t,D;

	cin >> TT;
	t = TT;

	
	while (TT--)
	{
		string input;
		cin >> input;
		string result = input;

		int current,biggest=0,problematic= input.size(),lastOkay=input.size();

		for (size_t i = 0; i < input.length(); i++)
		{
			current = input[i] - '0';
			if (current < biggest)
			{
				problematic = i;
				
				for (size_t j = 0; j < i; j++)
				{
					if ((input[j] - '0') == biggest)
					{
						lastOkay = j;
						break;
					}
				}
				break;
			}
			biggest = max(biggest, current);

		}

		if (lastOkay == 0 && ((input[0] - '0') == 1)) ///11110
		{
			result.clear();
			for (size_t i = 0; i < input.size()-1; i++)
				result += '9';
		}
		else //335770 -> 335669     122220 -> 111119  330 -> 299
		{
			result = input;
			
			result[lastOkay] = biggest - 1 + '0';
			for (size_t i = lastOkay+1; i < input.size(); i++)
			{
				result[i] = '9';
			}
		}
		
		cout << "Case #" << t - TT << ": " <<result << endl;

	}


	return 0;

}

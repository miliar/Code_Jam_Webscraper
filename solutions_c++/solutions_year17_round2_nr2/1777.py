#include <iostream>
#include <vector>
#include <string>

using namespace std;
int main() 
{
	std::cin.sync_with_stdio(false);
	int T;
	cin >> T;
	for (int c = 0; c<T; ++c)
	{
		cout << "Case #" << c+1 << ": ";
		vector<int> col(6);
		int n;
		cin >> n;
		for (int i=0; i<6; ++i)
			cin >> col[i];
		string result;
		while (col[3] > 0)
		{
			if (col[0] > 0)
			{
				result += "RG";
				--col[3];
				--col[0];
				n -= 2;
			}
			else
			{
				result = "IMPOSSIBLE";
				col = vector<int>(6,0);
			}	
		}
		if (result.size() > 0 && result.back() == 'G')
		{
			if (n>0)
			{
				result += "R";
				--col[0];
				--n;
			}
		}
		while (col[1] > 0)
		{
			if (col[4] > 0)
			{
				result += "BO";
				--col[1];
				--col[4];
				n -= 2;
			}
			else
			{
				result = "IMPOSSIBLE";
				col = vector<int>(6,0);
			}	
		}
		if (result.size() > 0 && result.back() == 'O')
		{
			if (n>0)
			{
				result += "B";
				--col[0];
				--n;
			}
		}
		while (col[5] > 0)
		{
			if (col[2] > 0)
			{
				result += "YV";
				--col[5];
				--col[2];
				n -= 2;
			}
			else
			{
				result = "IMPOSSIBLE";
				col = vector<int>(6,0);
			}	
		}
		if (result.size() > 0 && result.back() == 'V')
		{
			if (n>0)
			{
			result += "Y";
			--col[2];
			--n;
			}
		}
		if (result.size() == 0)
		{
			if (col[0] > 0)
			{
				result = "R";
				--col[0];
				--n;
			}
			else if (col[2] > 0)
			{
				result = "Y";
				--col[2];
				--n;
			}
			else 
			{
				result = "B";
				--col[4];
				--n;
			}
		}
		char prev, first;
		prev = result.back();
		first = result[0];

		while (!(col[0] == col[2] && col[0] == col[4]))
		{

		if (prev == 'R')
			{
				if (col[2] > col[4])
				{
					result += 'Y';
					--col[2];
					--n;
					prev = 'Y';
				}
				else
				{
					result += 'B';
					--col[4];
					--n;
					prev = 'B';
				}			
			}
			else if (prev == 'Y')
			{
				if (col[0] > col[4])
				{
					result += 'R';
					--col[0];
					--n;
					prev = 'R';
				}
				else
				{
					result += 'B';
					--col[4];
					--n;
					prev = 'B';
				}
			}
			else
			{
				if (col[2] > col[0])
				{
					result += 'Y';
					--col[2];
					--n;
					prev = 'Y';
				}
				else
				{
					result += 'R';
					--col[0];
					--n;
					prev = 'R';
				}
				
			}			
		}
		string rep;
		if (prev == 'R')
		{
			if (first == 'R')
				rep = "BRY";
			if (first == 'Y')
				rep = "YRB";
			if (first == 'B')
				rep = "BRY";
		}
		if (prev == 'Y')
		{
			if (first == 'R')
				rep = "BRY";
			if (first == 'Y')
				rep = "RYB";
			if (first == 'B')
				rep = "BRY";
		}
		if (prev == 'B')
		{
			if (first == 'R')
				rep = "RBY";
			if (first == 'Y')
				rep = "RYB";
			if (first == 'B')
				rep = "RBY";
		}		
		while (col[0] > 0)
		{
			result += rep;
			--col[0];
		}
		for (auto i:col)
		{
			if (i<0)
				result = "IMPOSSIBLE";
		}
		prev = result.back();
		for (auto a:result)
		{
			if (a == prev)
			{
				result = "IMPOSSIBLE";
				break;
			}
			prev = a;
		}
		if (n<0)
			result = "IMPOSSIBLE";
		cout << result  << endl;
		
		
	}

}

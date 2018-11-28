#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>
typedef long long int ll;
using namespace std;

int main (void)
{
	int t, limit, curr;
	string s;
	vector <int> n, result;

	bool ifWork;

	cin >> t;
	for (int i=1; i<=t; i++)
	{
		cin >> s;
		limit = 0;//TO BE MODIFIED

		for (int j=0; j<s.size(); j++)
		{
			n.push_back((int) (s[j]-'0'));
		}

		//vector translation works, no debug required above

		for (int j=0; j<n.size(); j++)
		{
			curr = n[j];

			ifWork = true;
			for (int k=j+1; k<n.size(); k++) //make sure this works
			{
				if (n[k] > curr) break; //has to all work, already set as working
				else if (n[k] < curr)
				{
					ifWork = false;
					break;
				}
			}

			if(ifWork) result.push_back(curr); //needs to continue
			else //curr doesn't work
			{
				if (curr == 1) {} //should only happen in first digit (left)
				else result.push_back(curr-1);

				for (int k=j+1; k<n.size(); k++) //make rest of the digits 9
				{
					result.push_back(9);
				}

				break;
			}
		}

		//print result
		printf("Case #%d: ", i);
		for (int j=0; j<result.size(); j++)
		{
			cout << result[j];
		}
		cout << endl;

		n.clear();
		result.clear();
	}
}
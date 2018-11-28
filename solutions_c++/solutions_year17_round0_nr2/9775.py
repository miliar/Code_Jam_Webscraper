#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <sstream>
#include <iomanip>
#include <cassert>

using namespace std;

#define wait system("pause");
const long double pi = 2 * acos(0.);

int main()
{

	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long k;
	cin >> k;
	long long numa = 1;
	for (int i = 0; i < k; i++)
	{
		long long n;
		cin >> n;
		vector <int> st;
		while (n)
		{
			st.push_back(n % 10);
			n /= 10;
		}
		reverse(st.begin(), st.end());
		vector <int> ans;
		int j = 0;
		for ( ;j < st.size()-1; j++)
		{
			if (st[j] <= st[j + 1])
			{
				ans.push_back(st[j]);
			}		
			else
			{
				st[j]--;
				for (int k = j + 1; k < st.size(); k++)
				{
					st[k] = 9;
				}
				ans.clear();
				j=-1;
			}
		}
		cout << "Case #" << numa<<": ";
		numa++;
		ans.push_back(st[j]);
		if (st[0] != 0)
			cout << st[0];
		for (int j = 1; j < ans.size(); j++)
			cout << ans[j];
		cout << endl;
	}
	
}


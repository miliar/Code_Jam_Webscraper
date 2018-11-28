#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <utility>
#include <iomanip> 
#include <queue>

using namespace std;

#define pb push_back

#define N 100100

typedef long long ll;

string s;
int t, n;

bool check()	{
	bool correct = true;
	for (int i = 0; i < n-1; i++)
		if (s[i] > s[i+1])
		{
			correct = false;
			s[i]--;
			for (int j = i+1; j < n; j++)
				s[j] = '9';
		}
		
	//cerr << s << ' ' << correct << endl;
	return correct;
}

int main() {

	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);

	cin >> t;
	for (int testcase = 1; testcase <= t; testcase++)
	{
		cin >> s;
		n = s.length();
		
		while (!check());
		
		cout << "Case #" << testcase << ": ";
		int i = 0;
		while (s[i] == '0')
			i++;
			
		for (; i < n; i++)
			cout << s[i];
		cout << endl;
	}

	return 0;
}
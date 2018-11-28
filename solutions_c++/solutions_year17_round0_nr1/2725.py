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
int t, k;

void flip(int l, int r)	{
	for (int i = l; i < r; i++)
		s[i] = (s[i] == '+' ? '-' : '+');
}

int main() {

	freopen("A-large.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(false);

	cin >> t;
	int testcase = 0;
	while (t--)	{
		cin >> s >> k;
		int n = s.length();
		int cnt = 0;
		for (int i = 0; i <= n-k; i++)
			if (s[i] == '-')
			{	
				flip(i,i+k);
				cnt++;
			}	
			
		bool solved = true;
		for (int i = n-k+1; i < n; i++)
			if (s[i] == '-')
				solved = false;
				
		testcase++;
		cout << "Case #" << testcase << ": ";
		if (solved)
			cout << cnt << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}

	return 0;
}
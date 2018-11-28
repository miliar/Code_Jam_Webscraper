#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("a.out");

char flip(char x)
{
	if(x == '+') x = '-';
	else x = '+';
	return x;
}

int slv(string s, int k)
{
	int n = s.length();
	int ans = 0;
	for(int i = 0; i + k - 1 < n; i++)
	{
		if(s[i] == '-')
		{
			for(int j = i; j < i + k; j++)
			s[j] = flip(s[j]);
			ans++;
		}
	}
	for(int i = 0; i < n; i++)
	if(s[i] == '-')
	return -1;
	return ans;
	
}

int main()
{
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; i++)
	{
		string s;
		int k;
		cin >> s >> k;
		int ans = slv(s, k);
		if(ans == -1)
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << ans << endl;
	}
	
	
	
	return 0;
}


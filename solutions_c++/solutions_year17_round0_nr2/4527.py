	//     . .. ... .... ..... be name khoda ..... .... ... .. .     \\

#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cassert>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;

inline int in() { int x; scanf("%d", &x); return x; }
const int N = 2002;

int main()
{
	int _t = in();
	for(int _i = 1; _i <= _t; _i++)
	{
		printf("Case #%d: ", _i);
		string s;
		cin >> s;
		int n = s.size();
		int koj = n;
		for(int i = n - 1; i; i--)
			if(s[i - 1] > s[i])
				koj = i - 1;
		if(koj < n)
		{
			while(koj > 0 && s[koj] == s[koj - 1])
				koj--;
			s[koj]--;
			for(int i = koj + 1; i < n; i++)
				s[i] = '9';
		}
		string ans;
		for(int i = 0; i < n; i++)
			if(s[i] > '0' || ans.size())
				ans += s[i];
		cout << ans << endl;
	}
}

# define _CRT_SECURE_NO_WARNINGS 
#include <iostream> 
#include <algorithm> 
#include <cstring> 
#include <cmath> 
#include <stdio.h> 
#include <vector> 
#include <cstdlib> 
#include <string> 
#include <map> 
#include <ctime> 
#include <list> 
#include <stack> 
#include <set> 
#include <memory.h> 
#include <deque> 
#include <queue> 
#include <cctype> 
#include <iomanip> 
#include <bitset> 
#include <sstream> 
#include <unordered_map> 
#include <fstream>

# define pi acos(-1.) 
# define e exp(1.) 

using namespace std;
using ld = long double;
using ll = long long;

const double EPS = 1e-6;
const int N = 100010;

int n, k;
bool Check(string& s)
{
	for (int i = 0; i < s.size(); ++i)
	{
		if (s[i] == '-')
		{
			return false;
		}
	}
	return true;
}

void UpdateString(string& s, int in)
{
	for (int i = 0; i < k; ++i)
	{
		if (s[in+i] == '+')
		{
			s[in+i] = '-';
		}
		else
		{
			s[in+i] = '+';
		}
	}
}
int main()
{
	fstream out("C:\\Users\\volok\\Desktop\\out.txt");
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i)
	{
		vector<int>intervals;
		string ans = "Case #" + to_string(i) + ": ";
		string s;
		cin >> s;
		scanf("%d", &k);
		int minn = 0;
		n = s.size();

		for (int i = 0; i <= n - k&&!Check(s); ++i)
		{
			if (s[i] == '-')
			{
				UpdateString(s, i);
				++minn;
			}
		}

		ans += (!Check(s)? "IMPOSSIBLE" : (to_string(minn)));
		out << ans << endl;
	}
}
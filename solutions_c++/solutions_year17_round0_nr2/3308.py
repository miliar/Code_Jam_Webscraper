#pragma comment(linker, "/STACK:256000000")
 
#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <utility>
#include <algorithm>
#include <random>
#include <unordered_map>
#include <unordered_set>
#include <complex>
using namespace std;
 
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;
typedef complex < double > base;
const int INF = (int)(1e9);
const int64 LINF = (int64)(1e18);
const double EPS = 1e-13;
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)(0))++)
const int MAXN = 100100;
const int BUBEN = 600000;
int n, k;
string s;
string solve(string s)
{
	int las = 0, flag = 0;
	
	for(int i = 1; i < s.size(); ++i)
	{
		if (s[i] < s[i - 1])
		{
			flag = 1;
			break;
		}
		if (s[i] > s[i - 1])
			las = i;
	}
	if (!flag)
	{
		return s;
	}
	
	string ans = "";
	for(int i = 0; i < las; ++i)
		ans += s[i];
	if (s[las] != '1')
		ans += s[las] - 1;
	for(int i = las + 1; i < s.size(); ++i)
		ans += '9';
	
		
	
	return ans;

}

int main()
{
	cin.tie(0); ios_base::sync_with_stdio(false);
#ifdef _MY_DEBUG
    freopen("input.txt", "rt", stdin); freopen("output.txt", "wt", stdout);
#else
#endif
    srand(88);
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i)
	{
		int k;
		string s;
		cin >> s;
		string t = solve(s);
		cout << "Case #" << i + 1 << ": " << t << '\n'; 
		//printf("Case #%d: %d\n", i + 1, t);
		
	}
    return 0;
}
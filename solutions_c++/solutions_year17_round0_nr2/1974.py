#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:500000000") 
#include <functional>
#include <algorithm>
#include <iostream> 
#include <string.h> 
#include <stdlib.h>
#include <complex>
#include <sstream> 
#include <fstream>
#include <numeric>
#include <ctype.h> 
#include <stdio.h> 
#include <bitset>
#include <vector> 
#include <string> 
#include <math.h> 
#include <time.h> 
#include <queue> 
#include <stack> 
#include <list>
#include <map> 
#include <set> 
#define Int long long 
#define INF 0x3F3F3F3F 
#define eps 1e-9
using namespace std;

#define N 21

char str[N];

//bool isAcs(string s)
//{
//	for (int i = 1; i < (int)s.size(); i++)
//		if (s[i] < s[i - 1])
//			return false;
//	return true;
//}
//
//string brute(string s)
//{
//	int n = atoi(s.c_str());
//	while (!isAcs(to_string(n)))
//		n--;
//	return to_string(n);
//}

string solve(string s)
{
	if (s.size() == 1)
		return s;
	for(char d = s[0]; d >= '0'; d--)
	{
		if (string(s.size(), d) <= s)
		{
			string res;
			if (d == s[0])
				res = solve(s.substr(1));
			else
				res = string((int)s.size() - 1, '9');
			if (d > '0')
				res = d + res;
			return res;
		}
	}
	return string((int)s.size() - 1, '9');
}

int main()
{
	//for(int i = 1; i < 10000; i++)
	//{
	//	if (solve(to_string(i)) != brute(to_string(i)))
	//	{
	//		cout << "BAD " << i << endl;
	//		return 1;
	//	}
	//}
	//return 0;

	int tests;
	scanf("%d", &tests);
	for(int test = 1; test <= tests; test++)
	{
		scanf("%s", str);
		printf("Case #%d: %s\n", test, solve(str).c_str());
	}
}
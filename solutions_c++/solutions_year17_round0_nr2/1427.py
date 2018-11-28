// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#ifdef _MSC_VER
#include "stdafx.h"
#endif
#include <cassert>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string>
// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#ifdef _MSC_VER
#include "stdafx.h"
#endif
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
typedef long long ll;
using namespace std;
int precomputed[2010];

#ifdef WIN32
int __stdcall WinMain(int hThisInstance, int hPrevInstance, int lpszArgument, int nCmdShow)
#else
int main()
#endif
{
	int T; cin >> T;
	for (int casen = 0; casen < T; casen++) {
		cout << "Case #" << casen+1 << ": ";
	string s; cin >> s;
	int pos = 0;
	while (pos < s.length() - 1 && s[pos] <= s[pos + 1])pos++;
	if (pos == s.length() - 1) { cout << s << endl; continue;}
	int pos2 = pos;
	while (pos2 > 0 && s[pos2-1] == s[pos])pos2--;
	if(s[pos2]>'1')s[pos2]--;
	else s[pos2] = ' ';pos2++;
	for (; pos2 < s.length(); pos2++)s[pos2] = '9';
	
	cout << s<<endl;




	}

}
/*

*/

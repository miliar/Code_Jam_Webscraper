// FcodejamA.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<string>
using namespace std;
int a[1050];
string s;
int main()
{
	int i, j, k, n, m, p, t,q;
	cin >> t;
	q = 0;
	while (t--) {
		q++;
		cin >> s >> k;
		n = s.size();
		for (i = 0; i < n; i++)
			if (s[i] == '-')
				a[i] = 0;
			else
				a[i] = 1;
		p= 0;
	   for(i=0;i<n-k+1;i++)
		   if (a[i] == 0)
		   {
			   for (j = 0; j < k; j++)
				   a[i + j] = 1 - a[i + j];
			     p++;
		   }
	   m = 0;
	   for (i = 0; i < n; i++)
		   if (a[i] == 0)
		   {
			   m = 1;
			   break;
		   }
	   if (m == 0) {
		   cout << "Case #" << q << ": " << p << endl;
	   }
	   else
		   cout << "Case #" << q << ": " << "IMPOSSIBLE" << endl;
	}
}


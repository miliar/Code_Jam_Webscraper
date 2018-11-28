// FcodejamB.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<algorithm>
using namespace std;
long long s[100];
long long a[10000000];
long long len;
void pp(int k,long long x) {
	long long u, i;
	len++;
	a[len] = x;
	if (k == 17)
		return;
	for (i = s[k]; i <= 9; i++)
	{
		u = x * 10 + i;
		s[k + 1] = i;
		pp(k + 1, u);
	}
}
int main()
{
	long long i, j, k, n, m, p,t;
	s[0] = 0;
	pp(0,0);
	sort(a+1, a + len+1);
	cin >> t;
	k = 0;
	while (t--) {
		k++;
		cin >> n;
		j = lower_bound(a + 1, a + 1 + len, n) - a;
		cout << "Case #" << k << ": ";
		if (j != len + 1) {
			if (a[j] == n)
				cout << n << endl;
			else
				cout << a[j - 1] << endl;
		}
		else
			cout << a[len] << endl;
	}
    return 0;
}


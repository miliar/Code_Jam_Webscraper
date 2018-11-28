#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

void print(char c1, char c2, int &n1, int &n2)
{
	for (int i = 0; i < n2; ++i)
		printf("%c%c", c1,c2);
	n2 = 0;
	if (n1 == 0) return;
	printf("%c",c1);
	--n1;
}

void solve()
{
	int N,R, O, Y, G, B, V;
	cin >> N>>R >> O >> Y >> G >> B >> V;
	int restb = B-O, restr = R-G, resty = Y-V;
	if (N-B-O==0)
	{
		if (restb == 0 || N==1)
			print('B','O',restb,O);
		else
			cout << "IMPOSSIBLE";
		cout << endl;
		return;
	}
	if (N-R-G==0)
	{
		if (restr == 0 || N==1)
			print('R','G',restr,G);
		else
			cout << "IMPOSSIBLE";
		cout << endl;
		return;
	}
	if (N-Y-V==0)
	{
		if (resty == 0 || N == 1)
			print('Y','V',resty,V);
		else
			cout << "IMPOSSIBLE";
		cout << endl;
		return;
	}
	if ((restb < 1 && O>0) || (restr < 1 && G>0) || (resty < 1 && V>0))
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	int maxi = restb, cases = 0;//0-b;1-r;2-y
	if (maxi < restr){maxi=restr;cases=1;}
	if (maxi < resty){maxi=resty;cases=2;}
	if (maxi*2 > restb+restr+resty)
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	switch (cases)
	{
		case 0:
		while (restb > 0)
		{
			print('B','O',restb,O);
			//cout << restb << " " << restr << " " << resty << endl;
			if (restr+resty>restb+1)
			{
				print('R','G',restr,G);
				print('Y','V',resty,V);
			} else
			if (restr>0)
				print('R','G',restr,G);
			else
				print('Y','V',resty,V);
		}
		break;
		case 1:
		while (restr > 0)
		{
			print('R','G',restr,G);
			if (restb+resty>restr+1)
			{
				print('B','O',restb,O);
				print('Y','V',resty,V);
			} else
			if (restb>0)
				print('B','O',restb,O);
			else
				print('Y','V',resty,V);
		}
		break;
		case 2:
		while (resty > 0)
		{
			print('Y','V',resty,V);
			if (restr+restb>resty+1)
			{
				print('R','G',restr,G);
				print('B','O',restb,O);
			} else
			if (restr>0)
				print('R','G',restr,G);
			else
				print('B','O',restb,O);
		}
		break;
	}
	while (restb+restr+resty>0)
	{
		if (restb>0)print('B','O',restb,O);
		if (restr>0)print('R','G',restr,G);
		if (resty>0)print('Y','V',resty,V);
	}
	cout << endl;
}

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int min(int a, int b, int c)
{
	if (a <= b && a <= c)
		return a;
	if (b <= c)
		return b;
	return c;
}

int max(int a, int b, int c)
{
	if (a >= b && a >= c)
		return a;
	if (b >= c)
		return b;
	return c;
}

int main()
{
	int T, N;
	int R, O, Y, G, B, V;
	int a = 0; int len = 0;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{	
		len = 0;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		cout << "Case #" << t << ": ";
		if (R + B + Y - max(R, B, Y) < max(R, B, Y))
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		int z = min(R, Y, B);
		R -= z;
		Y -= z;
		B -= z;
		if (!R)
		{
			if (Y >= B)
			{
				for (int i = 0; i < Y - B; i++) {
					cout << "YBYR"; len += 4;
				}
				for (int i = 0; i < z - (Y - B); i++) {
					cout << "YBR"; len += 3;
				}
				for (int i = 0; i < B; i++) {
					cout << "YB"; len += 2;
				}
			}
			else
			{
				for (int i = 0; i < B - Y; i++) {
					cout << "BYBR"; len += 4;
				}
				for (int i = 0; i < z - (B - Y); i++) {
					cout << "BYR"; len += 3;
				}
				for (int i = 0; i < Y; i++) {
					cout << "BY"; len += 2;
				}
					
			}
		} else
		if (!Y)
		{
			if (R >= B)
			{
				for (int i = 0; i < R - B; i++) {
					cout << "RBRY"; len += 4;
				}
				for (int i = 0; i < z - (R - B); i++) {
					cout << "RBY"; len += 3;
				}
				for (int i = 0; i < B; i++) {
					cout << "RB"; len += 2;
				}
			}
			else
			{
				for (int i = 0; i < B - R; i++) {
					cout << "BRBY"; len += 4;
				}
				for (int i = 0; i < z - (B - R); i++) {
					cout << "BRY"; len += 3;
				}
				for (int i = 0; i < R; i++) {
					cout << "BR"; len += 2;
				}
			}
		} else
		if (!B)
		{
			if (R >= Y)
			{
				for (int i = 0; i < R - Y; i++) {
					cout << "RYRB"; len += 4;
				}
				for (int i = 0; i < z - (R - Y); i++) {
					cout << "RYB"; len += 3;
				}
				for (int i = 0; i < Y; i++) {
					cout << "RY"; len += 2;
				}
			}
			else
			{
				for (int i = 0; i < Y - R; i++) {
					cout << "YRYB"; len += 4;
				}
				for (int i = 0; i < z - (Y - R); i++) {
					cout << "YRB"; len += 3;
				}
				for (int i = 0; i < R; i++) {
					cout << "YR"; len += 2;
				}
			}
		}	
		cout << endl;
		if (len != N)
			cout << "ALARM" << t << endl;
	}
	return 0;
}
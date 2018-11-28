#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <sstream>
#include <iomanip>
#include <cassert>

using namespace std;

#define sqr(x) ((x)*(x))

typedef long long ll;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	int arr[3];

	for (int t = 1; t <= T; t++)
	{

		cout << "Case #";
		cout << t << ": ";
		int N;
		int R, O, Y, G, B, V;

		cin >> N >> R >> O >> Y >> G >> B >> V;
		char sym[3] = { 'R', 'Y', 'B' };
		arr[0] = R; arr[1] = Y; arr[2] = B;
		string s;
		for (int i = 0; i < N; i++)
		{
			int max_ind = -1;
			int max_val = 0;
			for (int j = 0; j < 3; j++)
				if (max_val < arr[j] && (s.length() == 0 || s[s.length() - 1] != sym[j]))
				{
					max_ind = j;
					max_val = arr[j];
				}
			if (max_ind == -1)
				s += '#';
			else
			{
				s += sym[max_ind];
				arr[max_ind]--;
				if (s.length() == 1)
				{
					swap(arr[max_ind], arr[0]);
					swap(sym[max_ind], sym[0]);
				}
			}
		}
		bool fl = false;
		for (int i = 0; i < s.length(); i++)
			if (s[i] == '#')
				fl = true;
		if (fl || s[0] == s[s.length() - 1])
			cout << "IMPOSSIBLE";
		else
		{
			cout << s;
		}
		cout << endl;
	}

}

	/*int T;
	cin >> T;
	int arr[3];
	char sym[3] = { 'R', 'Y', 'B' };
	for (int t = 1; t <= T; t++)
	{
	
		cout << "Case #";
		cout << t << ": ";
		int N;
		int R, O, Y, G, B, V;
		
		cin >> N >> R >> O >> Y >> G >> B >> V;
		arr[0] = R; arr[1] = Y; arr[2] = B;
		dp[0][0][0][0][0] = 1;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				for (int q = 0; q < N; q++)
					for (int p = 0; p < 3; p++)
						for (int f_sym = 0; f_sym < 3; f_sym++)
						{
							if (dp[i % 2][j][q][p] != 0)
							{
								for (int go = 0; go < 3; go++)
								{
									if (go == 0 && i == 0 || p != go)
									{
										if (i == 0)
											dp[(i + 1) % 2][j][q][go][go] = dp[i % 2][j][q][p][f_sym];
										else
											dp[(i + 1) % 2][j][q][go][f_sym] = dp[i % 2][j][q][p][f_sym];
						
									}
									if (go == 1 && i == 0 || p != go)
									{
										if (i == 0)
											dp[(i + 1) % 2][j + 1][q][go][go] = dp[i % 2][j][q][p][f_sym];
										else
											dp[(i + 1) % 2][j + 1][q][go][f_sym] = dp[i % 2][j][q][p][f_sym];
									}
									if (go == 2 && i == 0 || p != go)
									{
										if (i == 0)
											dp[(i + 1) % 2][j][q + 1][go][go] = dp[i % 2][j][q][p][f_sym];
										else
											dp[(i + 1) % 2][j][q + 1][go][f_sym] = dp[i % 2][j][q][p][f_sym];
									}
								}
							}
						}
		bool fl = false;
		for (int p = 0; p < 3; p++)
			for (int f_sym = 0; f_sym < 3; f_sym++)
			{
				if (f_sym != p)
					if (dp[N % 2][arr[1]][arr[2]][p][f_sym] == 1)
						fl = true;
			}
		cout << fl;
		cout << endl;
	}
	*/
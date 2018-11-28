#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

#define DEBUG	0

int T, K;
string S;

void flip(int index)
{
	for (int i = index; i < index + K; i++)
	{
		if (S[i] == '+')
			S[i] = '-';
		else
			S[i] = '+';
	}
}

void solve()
{
	bool isHappy = true;
	int count = 0;

	for (int i = 0; i <= S.length() - K; i++)
	{
		if (S[i] == '-')
		{
			flip(i);
			count++;
		}
			
	}
	for (int i = S.length() - K + 1; i < S.length(); i++)
	{
		if (S[i] == '-')
			isHappy = false;
	}

	if (isHappy)
		cout << count;
	else
		cout << "IMPOSSIBLE";
}


int main()
{
	if (DEBUG) freopen("A-large.in", "r", stdin);
	if (DEBUG) freopen("A-large.out", "w", stdout);
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> S >> K;
		//if (DEBUG) cout << "S = " << S << " Slength=" << S.length() << " K = " << K << endl;
		cout << "Case #" << t + 1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}

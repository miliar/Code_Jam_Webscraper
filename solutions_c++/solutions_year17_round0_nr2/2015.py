#include <iostream>
#include <string>

#define ll long long
using namespace std;

string S;
int pr[10] = { 9, 0, 1, 2, 3, 4, 5, 6, 7, 8 };

inline void init()
{
	cin >> S;
}

inline bool check_max(int pos)
{
	for (int i = pos + 1; i < S.size(); i++)
		if (S[i] != '9')
			return 0;

	return 1;
}

inline bool check_min(int pos)
{
	for (int i = pos + 1; i < S.size(); i++)
	{
		if (S[i] > S[pos])
			return 1;
		else if (S[i] < S[pos])
			return 0;
	}

	return 1;
}

void f(int pos)
{
	int i;

	if (check_max(pos))
		return;

	if (!check_min(pos))
	{
		S[pos] = pr[S[pos] - '0'] + '0';
		for (i = pos + 1; i < S.size(); i++)
			S[i] = '9';
		return;
	}

	f(pos + 1);
}

inline void print()
{
	cout << stoll(S) << "\n";
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);

	int T, i;

	cin >> T;

	for (i = 1; i <= T; i++)
	{
		init();
		cout << "Case #" << i << ": ";
		f(0);
		print();
	}

	return 0;
}
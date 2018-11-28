#include <iostream>
#include <cstring>

using namespace std;

#define NOSOL 9999

bool is_happy[1000];
char s[1001];
int l, k;


int bf(int st, int d)
{
	bool all_happy = true;
	for (int i = 0; i < l; ++i)
		if (!is_happy[i])
			all_happy = false;

	if (all_happy)
		return d;

	if (st >= l)
		return NOSOL;

	int min_step = NOSOL;
	for (int i = st; i <= l - k; ++i)
	{
		// not toggle
		int step = bf(st + 1, d);
		if (step < min_step)
			min_step = step;

		// toggle
		// do
		for (int j = 0; j < k; j++)
			is_happy[i + j] = !is_happy[i + j];
		step = bf(st+1, d+1);
		if (step < min_step)
			min_step = step;
		// undo
		for (int j = 0; j < k; j++)
			is_happy[i + j] = !is_happy[i + j];
	}
	return min_step;
}

int main()
{
	int n_case;
	cin >> n_case;
	for (int i = 1; i <= n_case; ++i)
	{
		cin >> s >> k;
		l = strlen(s);

		for (int j = 0; j < l; ++j)
		{
			is_happy[j] = s[j] == '+';
		}
		
		int ans = bf(0, 0);
		cout << "Case #" << i << ": ";
		if (ans == NOSOL)
			cout << "IMPOSSIBLE";
		else
			cout << ans;

		cout << endl;
	}
	return 0;
}

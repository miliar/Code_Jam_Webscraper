#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

struct Action
{
	int Start, End, color, id;
};

bool cmp(Action a1, Action a2)
{
	if (a1.Start != a2.Start)
		return a1.Start < a2.Start;
	return a1.id < a2.id;
}

const int Max = 222;
int n, k1, k2;
Action a[Max];
multiset <int> gap1, gap2;

void solve(int num)
{
	cin >> k1 >> k2;
	for (int i = 1; i <= k1; i++)
	{
		cin >> a[i].Start >> a[i].End;
		a[i].color = 1;
		a[i].id = i;
	}
	for (int i = 1; i <= k2; i++)
	{
		cin >> a[i + k1].Start >> a[i + k1].End;
		a[i + k1].color = 2;
		a[i + k1].id = i + k1;
	}
	n = k1 + k2;
	sort(a + 1, a + n + 1, cmp);
	a[n + 1] = a[1];
	a[n + 1].Start += 1440;
	a[n + 1].End += 1440;
	int answer = 0;
	int Time1 = 0;
	int Time2 = 0;
	for (int i = 1; i <= n; i++)
	{
		if (a[i].color != a[i + 1].color)
			answer++;
		else
		{
			if (a[i].color == 1)
			{
				gap1.insert(a[i + 1].Start - a[i].End);
				Time1 += a[i + 1].Start - a[i].End;
			}
			else
			{
				gap2.insert(a[i + 1].Start - a[i].End);
				Time2 += a[i + 1].Start - a[i].End;
			}
		}
		if (a[i].color == 1)
			Time1 += a[i].End - a[i].Start;
		else
			Time2 += a[i].End - a[i].Start;
	}
	cout << "Case #" << num << ": ";
	if (Time1 <= 720 && Time2 <= 720)
	{
		cout << answer << endl;
		return;
	}
	if (Time1 > 720)
	{
		while (true)
		{
			multiset <int>::iterator it = gap1.end();
			it--;
			int num = (*it);
			gap1.erase(it);
			Time1 -= num;
			answer += 2;
			if (Time1 <= 720)
				break;
		}
	}
	else
	{
		while (true)
		{
			multiset <int>::iterator it = gap2.end();
			it--;
			int num = (*it);
			gap2.erase(it);
			Time2 -= num;
			answer += 2;
			if (Time2 <= 720)
				break;
		}
	}
	cout << answer << endl;
	return;
}

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}
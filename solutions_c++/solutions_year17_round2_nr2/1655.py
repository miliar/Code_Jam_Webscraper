#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cstring>
#include <cmath>
#include <stack>
#include <iomanip>
#define int long long
#define CONTAINS(v,n) (find((v).begin(), (v).end(), (n)) != (v).end())
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define ARY_SORT(a, size) sort((a), (a)+(size))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
using namespace std;

enum
{
	R, O, Y, G, B, V,
};

int ans[1000];
int num[6];
int first;
bool is_end;
int N;

bool is_valid(int n)
{
	num[first]++; //bonus

	for (int i = 0; i < 6; i++)
	{
		if (num[i] < 0)
		{
			num[first]--;
			return false;
		}
	}

	int bonus[6] = { 0 };
	bonus[first] = 1;
	if (num[R] - bonus[R] > num[Y] + num[B] + num[G]) { num[first]--; return false; }
	if (num[Y] - bonus[Y] > num[R] + num[B] + num[V]) { num[first]--; return false; }
	if (num[B] - bonus[B] > num[Y] + num[R] + num[O]) { num[first]--; return false; }
	if (num[O] - bonus[O] > num[B]) { num[first]--; return false; }
	if (num[G] - bonus[G] > num[R]) { num[first]--; return false; }
	if (num[V] - bonus[V] > num[Y]) { num[first]--; return false; }

	if (n > 0)
	{
		switch (ans[n - 1])
		{
		case R: if (!(ans[n] == Y || ans[n] == B || ans[n] == G)) { num[first]--; return false; } break;
		case Y: if (!(ans[n] == R || ans[n] == B || ans[n] == V)) { num[first]--; return false; } break;
		case B: if (!(ans[n] == Y || ans[n] == R || ans[n] == O)) { num[first]--; return false; } break;
		case O: if (!(ans[n] == B)) { num[first]--; return false; } break;
		case G: if (!(ans[n] == R)) { num[first]--; return false; } break;
		case V: if (!(ans[n] == Y)) { num[first]--; return false; } break;
		}
	}

	num[first]--;

	if (num[first] < 0) return false;

	return true;
}

void func(int n)
{
	if (n == N)
	{
		switch (ans[n - 1])
		{
		case R: if (!(ans[0] == Y || ans[0] == B || ans[0] == G)) { return; } break;
		case Y: if (!(ans[0] == R || ans[0] == B || ans[0] == V)) { return; } break;
		case B: if (!(ans[0] == Y || ans[0] == R || ans[0] == O)) { return; } break;
		case O: if (!(ans[0] == B)) { return; } break;
		case G: if (!(ans[0] == R)) { return; } break;
		case V: if (!(ans[0] == Y)) { return; } break;
		}
		is_end = true;
		return;
	}

	for (int i = 0; i < 6; i++)
	{
		ans[n] = i;
		num[i]--;
		if (n == 0)
		{
			first = ans[0];
		}
		if (is_valid(n))
		{
			func(n + 1);
			if (is_end) break;
		}
		num[i]++;
	}
}

signed main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> N;
		cin >> num[R] >> num[O] >> num[Y] >> num[G] >> num[B] >> num[V];

		is_end = false;
		func(0);

		cout << "Case #" << (t + 1) << ": ";
		if (is_end)
		{
			for (int i = 0; i < N; i++)
			{
				switch (ans[i])
				{
				case R: cout << "R"; break;
				case B: cout << "B"; break;
				case Y: cout << "Y"; break;
				case O: cout << "O"; break;
				case G: cout << "G"; break;
				case V: cout << "V"; break;
				}
			}
			cout << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
}

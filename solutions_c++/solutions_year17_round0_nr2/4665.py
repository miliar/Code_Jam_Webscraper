#pragma warning(disable : 4996) //_CRT_SECURE_NO_WARNINGS
#include <queue>
#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <set>
#include <deque>
#include <sstream>
#define sync ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ss second
#define ff first
#define ll long long
#define mp make_pair
#define endl "\n"
#define pb push_back
#define ld long double
#define M_PI 3.14159265358979323846
#define puss vector
const ld EPS = 0.9;
const ll INF = 1000000007;
using namespace std;


bool check(vector<int> n)
{
	for (int i = 0; i < n.size()-1; i++)
	{
		if (n[i + 1] < n[i])
			return false;
	}
	return true;
}

void show(vector<int> a)
{
	bool ch = false;
	for (int i = 0; i < a.size(); i++)
		if (a[i] == 0 && ch == false)
		{
			ch = true;
		}
		else
		cout << a[i];
	cout << endl;
}

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int h = 0; h < t; h++)
	{
		ll k;
		cin >> k;
		cout << "Case #" << h + 1 << ": ";

		vector<int> n;
		while (k)
		{
			n.pb(k % 10);
			k /= 10;
		}
		reverse(n.begin(), n.end());

		if (check(n))
		{
			show(n);
			continue;
		}
		for (int pos = n.size() - 1; pos >= 0; pos--)
		{
			if (n[pos] > 0)
			{
				n[pos]--;
				for (int i = pos+1; i < n.size(); i++)
					n[i] = 9;
				if (check(n))
				{
					show(n);
					break;
				}
			}
		}
	}
}
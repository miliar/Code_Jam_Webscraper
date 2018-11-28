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


int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int h = 0; h < t; h++)
	{
		int n,k;
		string s;
		cin >> s >> k;
		n = s.size();
		char a[1005];
		for (int i = 0; i < n; i++)
			if (s[i] == '+')
				a[i] = true;
			else
				a[i] = false;
		int res = 0;
		for (int i = 0; i <= n - k; i++)
		{
			
			if (a[i]==false)
			{
				/*
				for (int i = 0; i < n; i++)
				{
					cout << a[i] << ' ';
				}
				cout << endl;
				*/
				for (int j = i; j < i + k; j++)
					a[j] = (a[j]==true?false:true);
				res++;
			}
		}
		bool ch = true;
		cout << "CASE #" << h + 1 << ": ";
		for (int i=0;i<n;i++)
			if (a[i]==false)
			{
				cout << "IMPOSSIBLE" << endl;
				ch = false;
				break;
			}
		if (ch)
			cout << res << endl;
	}
}
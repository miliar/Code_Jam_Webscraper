#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	long long n;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n;
		deque<int> deq;
		while (n)
		{
			deq.push_front(n % 10);
			n /= 10;
		}
		for (int j = 0; j < deq.size()-1; j++)
		{
			if (deq[j] > deq[j + 1])
			{
				while (j != 0 && deq[j - 1] == deq[j]) j--;
				deq[j]--;
				for (int k = j + 1; k < deq.size(); k++) deq[k] = 9;
				break;
			}
		}
		long long ans = 0;
		for (auto &x : deq) ans = ans * 10 + x;
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
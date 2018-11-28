#pragma comment(linker, "/STACK:100000000")
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <stdio.h>
#include <set>
#include <queue>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <list>
#include <functional>
#include <unordered_set>
#include <unordered_map>
using namespace std;
int main()
{
	//freopen("C-large.in", "r", stdin); freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		long long n, k;
		cin >> n >> k;
		map <long long, long long> x;
		x.insert(make_pair(n, 1));
		long long power = 0;
		while (k > power) {
			auto current = x.end();
			current--;
			power += current->second;
			if (current->first % 2 == 0) {
				auto p = x.find(current->first / 2);
				if (p != x.end())
					p->second += current->second;
				else x.insert(make_pair(current->first / 2, current->second));
				p = x.find(current->first / 2 - 1);
				if (p != x.end())
					p->second += current->second;
				else x.insert(make_pair(current->first / 2 - 1, current->second));
			}
			else {
				auto p = x.find(current->first / 2);
				if (p != x.end())
					p->second += current->second*2;
				else x.insert(make_pair(current->first / 2, current->second*2));
			}
			if (power >= k)
				break;
			auto p = x.end();
			p--;
			x.erase(p);
		}
		auto current = x.end();
		current--;
		if (current->first % 2 == 0)
			cout << current->first / 2 << ' ' << current->first / 2-1;
		else cout << current->first / 2 << ' ' << current->first / 2;
		cout << "\n";
	}
	return 0;
}
#define _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include <string>
#include <cstdio>
#include <set>
#include <deque>
#include <vector>
using namespace std;


string solve(long long i) {
	string s = to_string(i);
	int index = -1;
	for (int i = 1; i < s.length(); i++) {
		if (index == -1 && s[i] < s[i - 1])
		{
			s[i - 1]--;
			index = i - 1;
		}

		if (index != -1)
			s[i] = '9';
	}

	if (index != -1)
		for (int i = index; i > 0; i--)
			if (s[i] < s[i - 1])
			{
				s[i - 1]--;
				s[i] = '9';
			}

	// deleting leading zeros
	index = 0;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == '0')
			index++;
		else
			break;

	}

	return s.substr(index);

}


int main()
{

	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, index = 0;
	long long n, ans;


	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> n;
		cout << "Case #" << i << ": " << solve(n)<<endl;


	}

	return 0;
}


#include <iostream>
#include <algorithm>
#include <vector>
#include <list>
#include <queue>
#include <string>
#include <stack>
#include <set>
#include <assert.h>


using namespace std;

FILE *fp;

#define READ                  freopen_s(&fp,"input.txt", "r", stdin);
#define WRITE                 freopen_s(&fp,"output.txt", "w", stdout);

uint64_t solve(uint64_t n)
{
	if (n < 10) return n;
	string s = to_string(n);
	size_t len = s.length();

	for (size_t c = len - 1; c > 0; c--)
	{
		if (s[c] < s[c - 1] || s[c] == '0')
		{
			for (size_t i = c; i < len; i++) s[i] = '9';
			s[c - 1]--;
		}
	}
	n = std::stoull(s);
	return n;
}


int main(int argc, char* argv[])
{
	READ;
	WRITE;

	int t; cin >> t;
	for (int i = 1; i <=t;++i)
	{
		uint64_t n; cin >> n;
		cout << "Case #" <<i << ": "<< solve(n) << endl;
	}

	return 0;
}
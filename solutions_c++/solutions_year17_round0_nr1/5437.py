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


string solve(string s, size_t k)
{
	int r = 0;
	if (count(s.begin(), s.end(), '-') == 0) return to_string(r);

	size_t len = s.length();
	for (size_t i = 0; i < len; i++)
	{
		if (s[i] == '-')
		{
			if (i + k > len)
				return "IMPOSSIBLE";
			for (size_t j=0; j < k; j++)
				s[i+j] = (s[i+j] == '-') ? '+' : '-';

			r++;
		}

	}

	return to_string(r);	
}

int main(int argc, char* argv[])
{
READ;
WRITE;

int t; cin >> t;
for (int i = 1; i <=t;++i)
{
	string s; cin >> s; size_t k; cin >> k;
	cout << "Case #" <<i << ": "<< solve(s,k).c_str() << endl;
}

return 0;
}
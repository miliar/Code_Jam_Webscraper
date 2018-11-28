#include <iostream>
#include <string>
#include <sstream>

using namespace std;

static long long toggle_count = 0;

bool check_done(string s, int slen)
{
	for (int i = 0; i < slen; i++)
		if (s[i] == '-')
			return false;
	return true;
}

void reverse(string& s, int index, int k, int n)
{
	if (index + k > n)
		return;
	for (int i = index; i < index + k; i++) {
		if (s[i] == '+') s[i] = '-';
		else if (s[i] == '-') s[i] = '+';
	}
	toggle_count++;
}

int main()
{
	string s;
	int T;
	long long k, n;
	cin >> T;

	for (int i = 0; i < T; i++) {
		cin >> s >> k;
		n = s.size();

		for (int j = 0; j < n; j++) {
			if(check_done(s, n))
				goto OUTPUT;
			if (s[j] == '-')
				reverse(s, j, k, n);
		}
OUTPUT:
		if(check_done(s, n))
			cout << "Case #" << i + 1 << ": " << toggle_count << endl;
		else
			cout << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
		toggle_count = 0;
	}
	return 0;
}

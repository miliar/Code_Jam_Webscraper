#include <iostream>
#include <vector>

using namespace std;

void flip(string &s, int i, int k);

void flip(string &s, int i, int k)
{
	while(k>0){
		s[i] = (s[i] == '+') ? '-' : '+';
		--k;
		++i;
	}
}

int main()
{
	int n;
	long long k, ans;
	string s;
	cin >> n;
	for (int i = 0; i < n; ++i){
		cin >> k;
		s = to_string(k);
		int l = (int)s.size(), j = 1;
		// cout << s << endl;

		bool change = false;
		while (j < l){
			if (s[j-1] <= s[j]){
				j++;
				continue;
			}
			int m = j;
			while (m < l){
				s[m] = '9';
				m++;
				change = true;
			}
			if (change) j--;
			break;
		}
		if (j < l){
			while (j > 0){
				if (s[j] > s[j-1]){
					s[j]--;
					change = false;
				}
				else{
					s[j] = '9';
					change = true;
				}
				j--;
			}
			if (change || s[j] > s[j+1])
				s[j]--;
		}

		ans = stoll(s);

		// if (ans == -1)
		// 	cout << "Case #" << i+1 << ": IMPOSSIBLE" << endl;
		// else
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}

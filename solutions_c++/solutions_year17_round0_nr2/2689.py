#include <iostream>
#include <cstdio>

using namespace std;

int t;
string s;
int n;

void print(string s) 
{
	int k = 0;
	int n = s.size();
	
	while (k < n && s[k] == '0')
		k++;
	if (k == n) {
		cout << 0;
		return;
	}
	
	for (int i = k; i < n; i++)
		cout << s[i];
}

bool can(string s, int k) 
{
	bool fl = true;
	int n = s.size();
	
	for (int i = k + 1; i < n; i++) {
		if (s[i] > s[k])
			break;
		if (s[i] < s[k]) {
			fl = false;
			break;
		}
	}
	
	return fl;
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	
	cin >> t;
	
	for (int l = 0; l < t; l++) {
		cin >> s;
		n = s.size();
		string ans = s;
		
		for (int i = 0; i < n; i++) {
			if (!can(ans, i)) {
				ans[i] -= 1;
				for (int j = i + 1; j < n; j++)
					ans[j] = '9';
				break;
			}
		}
		
		cout << "Case #" << l + 1 << ": ";
		print(ans);
		cout << endl;		
	}
	
	
	return 0;
}

#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>

using namespace std;



int check(string &s, int pan, int len)
{
	int ans = 0;
	for (int i = len; i >= pan-1; --i){
		if (s[i] == '-'){
			ans++;
			
			for (int j = 0; j < pan; ++j){
				if (s[i - j] == '-')
					s[i - j] = '+';
				else
					s[i - j] = '-';
			}
		}
	}
	for (int j = 0; j < s.length() - 1; ++j)
	{
		if (s[j] != '+')
			return -1;
	}
	//cout << s << endl;
	return ans;
}

int main()
{
#ifdef _DEBUG
	freopen("c:/a.in", "r", stdin);
	freopen("c:/a.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++){
		string s;
		int pan_size;
		cin >> s;
		scanf("%d", &pan_size);
		int a = check(s, pan_size, s.length() - 1);
		if (a == -1)
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		else
			cout << "Case #" << i << ": " << a << endl;
	}
}
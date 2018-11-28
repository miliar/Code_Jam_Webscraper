#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
#include<bitset>
#include<vector>
#include<deque>
#include<queue>
#include<map>
#include<set>
#include<stack>
#include<cmath>
#include<iomanip>
#include <functional>
using namespace std;
typedef long long ll;
const int mod = 1000000007;
const int INF = 1 << 28;
const double EPS = 1e-10;
//cout << fixed << std::setprecision(9)
//memset(a, 0, sizeof(a));
//--------------------------

int t;
string s;

bool check(string s)
{
	if (s.size() < 2) return true;
	int n = s.size();
	for (int i = 0;i < n - 1;i++) {
		if (s[i] > s[i + 1]) return false;
	}
	return true;
}

void Count(string s)
{
	int n = s.size();

	while (!check(s)) {
		int k = n - 1;
		while (s[k - 1] <= s[k]) k--;
		s[k - 1]--;
		while (k < n) {
			s[k] = '9';
			k++;
		}
	}
	
	int i = 0;
	while (s[i] == '0') i++;
	while (i < n) {
		cout << s[i];
		i++;
	}
	cout << endl;

	return;
}


int main()
{
	cin >> t;

	for (int i = 0;i < t;i++) {
		cin >> s;
		cout << "Case #" << i + 1 << ": ";
		Count(s);
	}
	return 0;
}

int countSmall(int n)
{
	if (n < 10) return n;
	if (n == 1000) return 999;

	while (n > 9) {
		int a, b, c;
		a = n / 100;
		b = (n / 10) % 10;;
		c = n % 10;
		if (a <= b && b <= c) {
			return n;
		}
		n--;
	}
	return n;
}


//int t,k;
//string s;
//
//void parse(string s, int k)
//{
//	int ans = 0;
//	int n = s.size();
//
//	for (int i = 0;i < n - k;i++) {
//		if (s[i] == '-') {
//			for (int j = i;j < i + k;j++) {
//				if (s[j] == '-') s[j] = '+';
//				else s[j] = '-';
//			}
//			ans++;
//		}
//	}
//
//	int subcount = 0;
//	for (int i = n - k;i < n;i++) {
//		if (s[i] == '-') subcount++;
//	}
//
//	if (subcount == 0) {
//		cout << ans << endl;
//		return;
//	}
//
//	if (subcount < k) {
//		cout << "IMPOSSIBLE" << endl;
//		return;
//	}
//	else {
//		cout << ans+1 << endl;
//	}
//}








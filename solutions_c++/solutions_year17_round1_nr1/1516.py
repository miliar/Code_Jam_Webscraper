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

char grid[30][30];
int r, c;
void Solve(void)
{
	if (r == 1 && c == 1) {
		cout << grid[0][0] << endl;
		return;
	}

	if (r == 1) {
		//go right
		for (int j = 1;j < c;j++)
			for (int i = 0;i < r;i++) {
				if (grid[i][j] == '?') grid[i][j] = grid[i][j - 1];
			}

		//go left
		for (int j = c - 2;j >= 0;j--)
			for (int i = 0;i < r;i++) {
				if (grid[i][j] == '?') grid[i][j] = grid[i][j + 1];
			}

		for (int k = 0;k < r;k++) {
			for (int j = 0;j < c;j++)
				cout << grid[k][j];
			cout << endl;
		}
		return;
	}

	if (c == 1) {
		//down
		for (int i = 1;i < r;i++)
			for (int j = 0;j < c;j++) {
				if (grid[i][j] == '?') grid[i][j] = grid[i - 1][j];
			}

		//up
		for (int i = r - 2;i >= 0;i--)
			for (int j = 0;j < c;j++) {
				if (grid[i][j] == '?') grid[i][j] = grid[i + 1][j];
			}
		for (int k = 0;k < r;k++) {
			for (int j = 0;j < c;j++)
				cout << grid[k][j];
			cout << endl;
		}
		return;
	}


	//down
	for (int i = 1;i < r;i++)
		for (int j = 0;j < c;j++) {
			if (grid[i][j] == '?') grid[i][j] = grid[i - 1][j];
		}

	//up
	for (int i = r - 2;i >= 0;i--)
		for (int j = 0;j < c;j++) {
			if (grid[i][j] == '?') grid[i][j] = grid[i + 1][j];
		}

	//go right
	for (int j = 1;j < c;j++)
		for (int i = 0;i < r;i++) {
			if (grid[i][j] == '?') grid[i][j] = grid[i][j - 1];
		}

	//go left
	for (int j = c - 2;j >= 0;j--)
		for (int i = 0;i < r;i++) {
			if (grid[i][j] == '?') grid[i][j] = grid[i][j + 1];
		}

	for (int k = 0;k < r;k++) {
		for (int j = 0;j < c;j++)
			cout << grid[k][j];
		cout << endl;
	}
}

 int main()
{
	cin >> t;

	for (int i = 0;i < t;i++) {
		cin >> r >> c;
		for (int k = 0;k < r;k++)
			for (int j = 0;j < c;j++)
				cin >> grid[k][j];

		cout << "Case #" << i + 1 << ":" << endl;
		
		Solve();
	}
	return 0;
}



//int t;
//int k, n;
//int stalls[2000];
//
//void Solve(int n, int k)
//{
//	memset(stalls, 0, sizeof(stalls));
//	stalls[0] = stalls[n + 1] = 1;
//
//	int left, right, place;
//
//	//simulate k people
//	for (int i = 0;i < k;i++) {
//		place = 0;
//		int minDis = -1;
//		int BigWide = -1;
//
//		for (int j = 1;j <= n;j++) {
//			if (stalls[j]) continue;
//			left = 1;
//			right = 1;
//			while (!stalls[j - left]) left++;
//			while (!stalls[j + right]) right++;
//			left--;
//			right--;
//
//			if (minDis < std::min(left, right)) {
//				place = j;
//				minDis = std::min(left, right);
//				BigWide = std::max(left, right);
//			}
//			else if (minDis == std::min(left, right)) {
//				if (BigWide < std::max(left, right)) {
//					place = j;
//					BigWide = std::max(left, right);
//				}
//			}
//		}
//
//		stalls[place] = true;
//	}
//
//	left = 1;
//	right = 1;
//	while (!stalls[place - left]) left++;
//	while (!stalls[place + right]) right++;
//	left--;
//	right--;
//
//	cout << std::max(left,right) << " " << std::min(left,right) << endl;
//}
//
//int main()
//{
//	cin >> t;
//
//	for (int i = 0;i < t;i++) {
//		cin >> n >> k;
//		cout << "Case #" << i + 1 << ": ";
//		Solve(n, k);
//	}
//	return 0;
//}

//bool check(string s)
//{
//	if (s.size() < 2) return true;
//	int n = s.size();
//	for (int i = 0;i < n - 1;i++) {
//		if (s[i] > s[i + 1]) return false;
//	}
//	return true;
//}
//
//void Count(string s)
//{
//	int n = s.size();
//
//	while (!check(s)) {
//		int k = n - 1;
//		while (s[k - 1] <= s[k]) k--;
//		s[k - 1]--;
//		while (k < n) {
//			s[k] = '9';
//			k++;
//		}
//	}
//
//	int i = 0;
//	while (s[i] == '0') i++;
//	while (i < n) {
//		cout << s[i];
//		i++;
//	}
//	cout << endl;
//
//	return;
//}
//
//
//
//int countSmall(int n)
//{
//	if (n < 10) return n;
//	if (n == 1000) return 999;
//
//	while (n > 9) {
//		int a, b, c;
//		a = n / 100;
//		b = (n / 10) % 10;;
//		c = n % 10;
//		if (a <= b && b <= c) {
//			return n;
//		}
//		n--;
//	}
//	return n;
//}
//

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








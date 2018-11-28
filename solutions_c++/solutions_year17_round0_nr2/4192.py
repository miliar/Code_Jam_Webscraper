#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int n, t, j;
vector<string>v;
bool c(string k, string j) { return k.length() < j.length() || (k.length() == j.length() && k < j); }
void f(string x) {
	v.push_back(x);
	int m = x.length();
	if (m == 18)return;
	for (char i = x[m - 1]; i <= '9'; ++i)f(x + i);
}
void js() {
	for (string i = "1"; i <= "9";i[0]++)f(i);
	sort(v.begin(), v.end(), c);
}
string s;
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	js();
	cin >> t;
	while (j++ < t) {
		cin >> s;
		cout << "Case #" << j << ": " << *(upper_bound(v.begin(), v.end(), s, c)-1) << endl;
	}
}
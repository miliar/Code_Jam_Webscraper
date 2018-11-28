#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
FILE *fi = freopen("B-large.in", "r", stdin);
FILE *fo = freopen("outBL.txt", "w", stdout);
int test;
string str;
char change(char ch)
{
	--ch;
	return ch;
}
int main() {
	int lev = 0;
	scanf("%d", &test); while (test--) {
		++lev;
		cin >> str;
		for (int i = str.size() - 2; i >= 0; i--) {
			if (str[i] > str[i + 1]) {
				str[i] = change(str[i]);
				for (int j = i + 1; j < str.size(); j++)str[j] = '9';
			}
		}
		while (str[0] == '0')str.erase(str.begin());
		printf("Case #%d: ", lev);
		cout << str << endl;
	}
	exit(0);
}
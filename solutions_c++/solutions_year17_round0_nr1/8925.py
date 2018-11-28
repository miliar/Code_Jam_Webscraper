/*
	1. 
*/
#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int test = 1;test <= t;++test) {
		string txt;
		cin >> txt;
		int len = txt.length() ;
		int size;
		cin >> size;
		int cnt = 0;
		bool imp = 0;
		for (int i = 0;i < len;++i) {
			if (txt[i] == '-') {
				cnt++;
				for (int j = i;j < i + size;++j) {
					if (j == len) {
						imp = 1; break;
					}
					if (txt[j] == '-') txt[j] = '+';
					else txt[j] = '-';
				}
			}
			if (imp) break;
		}
		printf("Case #%d: ", test);
		if (imp) printf("IMPOSSIBLE");
		else printf("%d", cnt);
		printf("\n");
	}
}
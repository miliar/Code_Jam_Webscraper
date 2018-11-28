#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <map>
#include <string>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <bitset>
using namespace std;

typedef long long LL;
#define pb push_back

bool f(string &s){
	for(int i = 1; i < s.length(); ++i){
		if(s[i] < s[i-1]){
			int fl = i-1;
			while(s[fl] == '0') --fl;
			s[fl] -= 1;
			for(int j = i; j < s.length(); ++j) s[j] = '9';
			return 1;
		}
	}
	return 0;
}

int main () {
	int T;
	scanf("%d", &T);
	for(int tt = 1; tt <= T; ++tt){
		string s;
		cin >> s;
		while(f(s)){}
		printf("Case #%d: ", tt);
		for(int i = 0; i < s.length(); ++i){
			if(!i && s[i] == '0') continue;
			putchar(s[i]);
		}
		puts("");
	}
}
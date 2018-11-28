#include <algorithm>
#include <vector>
#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
using namespace std;

int main() {
	freopen("text.txt", "w", stdout);
	int tc; scanf("%d", &tc);
	for(int t=1;t<=tc;t++){
		int k; 
		string s1; cin >> s1;
		scanf("%d", &k);

		int cnt = 0;
		for (int i = k-1; i < s1.size(); i++) {
			int first = i - k + 1;
			if (s1[first] == '+') continue;
			cnt++;
			for (int j = first; j <= i; j++) {
				if (s1[j] == '+') s1[j] = '-';
				else s1[j] = '+';
			}
		}
		bool flag = false;
		for (int i = s1.size() - k; i < s1.size(); i++) {
			if (s1[i] == '-') {
				flag = true;
				break;
			}
		}
		if (flag) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n", t,cnt);
	}
}
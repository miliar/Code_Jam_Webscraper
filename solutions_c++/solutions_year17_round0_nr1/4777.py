#include <bits/stdc++.h>
using namespace std;

string s;
int k, n;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);;
	int test;
	scanf("%d\n", &test);
	for(int dem = 1; dem <= test; dem++) {
		getline(cin, s, ' ');
		scanf("%d\n", &k);
		n = s.length();
		int cnt = 0;
		for(int i=0; i+k<=n; i++)
			if (s[i] == '-') {
				++cnt;
				for(int j=0; j<k; j++)
					if (s[i+j] == '+')
						s[i+j] = '-';
					else 
						s[i+j] = '+';
			}
		for(int i=0; i<n; i++) 
			if (s[i] == '-') 
				cnt = -1;
		if (cnt == -1) 
			printf("Case #%d: IMPOSSIBLE\n", dem);
		else 
			printf("Case #%d: %d\n", dem, cnt);
	}
	fclose(stdin);
	fclose(stdout);
}
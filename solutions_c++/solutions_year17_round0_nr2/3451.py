#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;
#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)
typedef long long ll;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;

char s[1111];
int main()
{
	int tt, n, change, last;
	char mx;
	scanf("%d",  &tt);
	for (int t = 0; t < tt; t++) {
		scanf(" %s", s);
		n = strlen(s);
		mx = s[0];
		change = 0;
		last = 0;
		for (int i = 1; i < n; i++) {
			if (s[i] > mx) {
				mx = s[i];
				last = i;
			}
			else if (s[i] < mx) {
				change = 1;
				break;
			}
		}
		if (!change) printf("Case #%d: %s\n", t+1, s);
		else {
			printf("Case #%d: ", t+1);
			if (mx == '1') {
				for (int i = 0; i < n-1; i++) 
					printf("9");
			}
			else {
				s[last]--;
				for (int i = last+1; i < n; i++) s[i] = '9';
				for (int i = 0; i < n; i++) printf("%c", s[i]);
			}
			printf("\n");
		}
	}	

	return 0;
}
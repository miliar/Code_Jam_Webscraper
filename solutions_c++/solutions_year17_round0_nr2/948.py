/*cf handle: visitR*/

#include <bits/stdc++.h>
using namespace std;

#define pi acos(-1)
#define inf (1 << 30)
#define linf (1llu << 60)

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int,int> pii;
typedef vector<pii> vp;
typedef pair<double, double> pdd;
typedef pair<int, double> pid;

int main() {
	int T;
	scanf("%d", &T);
	char str[22];
	for (int t=1; t<=T; ++t) {
		scanf("%s", str);
		int len = strlen(str);
		int pos = len-1;
		int i = 1;
		while (i < len) {
			if (str[i] < str[i-1]) {
				str[i-1]--;
				pos = i-1;
				break;
			}
			++i;
		}
		i = pos - 1;
		while (i >= 0) {
			if (str[i] > str[i+1]) {
				str[i]--;
				pos = i;
			}
			--i;
		}
		printf("Case #%d: ", t);
		for (int i=0; i<=pos; ++i) {
			if (str[i] != '0')
				printf("%c", str[i]);
		}
		for (int i=pos+1; i<len; ++i)
			printf("9");
		printf("\n");
	}
	return 0;
}
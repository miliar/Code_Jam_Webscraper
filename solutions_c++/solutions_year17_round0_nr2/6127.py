#include <bits/stdc++.h>

#define maxn 100000008
#define pp push_back
#define pf push_front
#define mp make_pair
#define fs first
#define sc second

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main(int argc, char *argv[])
{
	/* freopen("in.txt", "r", stdin); */
	/* freopen("out", "w", stdout); */
	
	int t;
	scanf("%d", &t);
	for (int tc = 1; tc <= t; ++tc) {
		string s;
		cin >> s;
		int len = s.length();
		int i;
		for (i = 0; i < len - 1; ++i) {
			if(s[i] > s[i+1]){
				s[i] = (char)s[i] - 1;
				for (int j = i + 1; j < len; ++j) {
					s[j] = '9';
				}
				break;
			}
		}

		for (; i > 0; --i) {
			if(s[i-1] > s[i]){
				s[i] = '9';
				s[i-1] = (char)s[i-1] - 1;
			}
		}
		while(s[i] == '0'){
			s.erase(s.begin());
		}
		printf("Case #%d: ", tc);
		cout << s << endl;

		fprintf(stderr, "test %d solved\n", tc);
	}
	return 0;
}

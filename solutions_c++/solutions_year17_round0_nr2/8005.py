#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <functional>
#include <iterator>
#include <map>
#include <numeric>
#include <cstring>
#include <string>
#include <sstream>
#include <set>
#include <stack>
#include <queue>
#include <cctype>
#include <math.h>
#include <cstdlib>

using namespace std;

#define I64 long long int
#define INF 0x7f7f7f7f

#define PII pair <int, int>
#define PLL pair <I64, I64>
#define PDD pair <double, double>
#define PSI pair <string, int>
#define PIS pair <int, string>
#define PSS pair <string, string>

#define MII map <int, int>
#define MLL map <I64, I64>
#define MDD map <double, double>
#define MSI map <string, int>
#define MIS map <int, string>
#define MSS map <string, string>

#define VI vector <int>
#define VS vector <string>
#define QI queue <int>
#define QS queue <string>
#define SI stack <int>
#define SS stack <string>

#define pb push_back
#define pob pop_back
#define mp make_pair

#define IT iterator
#define ff first
#define ss second

#define SET(a, b) memset( a, b, sizeof (a) )
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define IAMHERE cout << "YES\n";
#define DEBUG(a, b) cout << a << ": " << b << "\n";

#define SIZE 1000
#define MAX 2000
#define EPS 1e-9
#define PI (2*acos(0.0))

int digit[] = {9, 0, 1, 2, 3, 4, 5, 6, 7, 8};

void makeTidy(string &s)
{
	for (int i = 1; i < s.size(); i++) {
		if (s[i - 1] > s[i]) {
			s[i - 1] = digit[s[i - 1] - 48] + 48;
			for (int j = i; j < s.size(); j++) {
				s[j] = '9';
			}
		}
	}
}

bool isTidy(const string &s)
{
	for (int i = 1; i < s.size(); i++) {
		if (s[i - 1] > s[i]) return false;
	}
	return true;
}

int main()
{
    READ("B-large.in");
    WRITE("out.txt");
    int Case=1;
    int n, m, k;
    string s;
    char dump[2];

    int tc; scanf("%d", &tc);
    gets(dump);

    while (tc--) {
    	getline(cin, s);

    	while (!isTidy(s)) {
    		makeTidy(s);
    	}

    	while (s[0] == '0') s.erase(s.begin());
    	printf("Case #%d: %s\n", Case++, s.c_str());
    }
    return 0;
}

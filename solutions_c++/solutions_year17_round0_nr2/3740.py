#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

#define debug 1

#define cerr if(debug) cerr

#define For(i, a, b) for(int i = a; i < b; i++)
#define sz(a) ((int)a.size())
#define mp make_pair
#define pb push_back
#define all(a) a.begin(), a.end()

typedef pair<int, int> pii;
typedef long long lint;

const int inf = 0x7fffffff;
const int Size = 1000 * 1000 + 1;
char buffer[Size];


void init() {

}

void clear(int i) {

}

int solution(int nTest) {
	scanf("%s", buffer);
	string s = buffer;
	int firstOc = 0;
	For (i, 1, sz(s)) {
		if (s[i - 1] < s[i]) {
			firstOc = i;
		} else if (s[i - 1] > s[i]) {
			s[firstOc] = s[firstOc] - 1;
			For (j, firstOc + 1, sz(s)) {
				s[j] = '9';
			}
			break;
		}
	}
	lint res = atoll(s.c_str());
	printf("%lld\n", res);

	return 0;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int i = 0, n = 999999;
	scanf("%d", &n);
	init();
	For(i, 0, n) {
		printf("Case #%d: ", i + 1);
		clear(i);
		solution(i);
	}

	return 0;
}
	

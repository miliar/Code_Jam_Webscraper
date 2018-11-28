#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
const int INF = 987654321;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n - 1)&n) + 1 : 0; }
#define PI 3.141592
int n;

char buffer[20];
vector<int> v;

void decrease() {
	int depth = v.size() -1;
	while (1) {
		if (v[depth] == 0) {
			v[depth] = 9;
			depth--;
		}
		else {
			v[depth]--;
			break;
		}
	}
}

int main() {
	string infile = "B-large.in";
	string outfile = "out.txt";

	freopen(infile.c_str(), "r", stdin);
	freopen(outfile.c_str(), "w", stdout);
	int tt;

	scanf("%d", &tt);
	for (int tc = 1; tc <= tt; tc++) {
		scanf("%s", buffer);
		int len = strlen(buffer);
		v.clear();
		for(int i=0;i < len;i++) {
			v.push_back(buffer[i] - '0');
		}
		int num_of_nine = 0;
		
		while (1) {
			int pos = -1;
			for (int i = 0; i < v.size() - 1; i++) {
				if (v[i] > v[i + 1]) {
					pos = i;
					break;
				}
			}
			if (pos == -1)
				break;
			int num = v.size() - pos - 1;
			while (num--) {
				v.pop_back();
				num_of_nine++;
			}
			decrease();
		}
		printf("Case #%d: ", tc);
		for (int i = 0; i < v.size(); i++) {
			if( i != 0 || v[i] != 0)
			printf("%d", v[i]);
		}
		F0(i, num_of_nine)
			printf("9");
		printf("\n");
	}
}
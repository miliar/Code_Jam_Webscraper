#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
const int INF = 1000000000;
int N;
int idx[105];
int solve(string str, int k) {
  int flips = 0;
  for (int i = 0; i < SIZE(str); i++) {
    if (str[i] == '-') {
      flips++;
      if (i + k > SIZE(str)) {
        return  -1;
      }
      for (int j = 0; j < k; j++) {
        if (str[i + j] == '-') {
          str[i + j] = '+';
        } else {
          str[i + j] = '-';
        }
      }
    }
  }
  
  return flips;
}

int main() {
	//freopen("a.in", "r", stdin); 
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	//freopen("A-small-attempt3.in", "r", stdin); freopen("A-small-attempt3.out", "w", stdout);
	
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	
	int nT;
	cin>>nT;
	for (int t=1; t<=nT; t++) {
    string str;
    int k;
		cin>>str>>k;

		printf("Case #%d: ", t);
    int ret = solve(str, k);
    if (ret == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << ret << endl;
    }
	}
	return 0;
}

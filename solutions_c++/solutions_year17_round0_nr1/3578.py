#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>
#include <set>
#include <cmath>
#include <utility>
#include <queue>
#include <deque>

#define rep(i,a,n) for(int i=a;i<=n;i++)
#define REP(i,a,n) for(int i=a;i<n;i++)
#define mp make_pair
#define pb push_back
#define SZ(x) ((int) (x).size())


using namespace std;

typedef  long long  LL;
typedef  vector<int> VI;
typedef  pair<int,int> PII;

int main(){
	ios::sync_with_stdio(false);
	int n;
	cin>>n;
	rep(pp, 1, n) {
		printf("Case #%d: ", pp);
		string s;
		int ans = 0, k;
		cin >> s;
		cin >> k;
		int len = s.length();
		bool flag = true;
		vector<int> seq;
		REP(i, 0, len) {
			if(s[i] =='+')
				seq.pb(1);
			else
				seq.pb(0);
		}		
		REP(i, 0, len) {
			if(seq[i] == 1)
				continue;
			if( i+k > len) {
				flag = false;
				break;
			}
			ans++;
			REP(j, i, i+k) {
				seq[j] ^= 1;
			}
		}
		if (flag) {
			printf("%d\n", ans);
		} else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}
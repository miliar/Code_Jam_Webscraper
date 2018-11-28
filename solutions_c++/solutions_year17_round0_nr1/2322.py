#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		int bad = 0;
		for (int i = 0; i < s.size(); i++) if (s[i] == '-') {
			ans++;
			for (int j = 0; j < k; j++) {
				if (i + j >= s.size()) bad = 1; else {
					if (s[i + j] == '-') s[i + j] = '+'; else s[i + j] = '-';
				}
			}
		}
		cout << "Case #" << tt << ": ";
		if (bad) cout << "IMPOSSIBLE"; else cout << ans;
		cout << endl;

	}
	return 0;
}
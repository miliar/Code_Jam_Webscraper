#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <bitset>
#include <climits>
#define REP(i,n) for (int i=0;i<(n);i++)
#define FOR(i,a,b) for (int i=(a);i<(b);i++)
#define RREP(i,n) for (int i=(n)-1;i>=0;i--)
#define RFOR(i,a,b) for (int i=(a)-1;i>=(b);i--)
#define ll long long
#define ull unsigned long long
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
const int INF = 1e9;
const int MOD = 1e9 + 7;

using namespace std;



int main(){
  cin.tie(0);
  ios::sync_with_stdio(false);
	int t;cin>>t;
	int ans[20];
	FOR(c,1,t+1){
	string s;
	cin>>s;
	fill_n(ans,20,0);
	RFOR(i,s.size(),0){
		if(i==(int)s.size()-1)ans[i] = s[i]-'0';
		else{
			if(s[i]-'0' > ans[i+1]){
				ans[i] = s[i]-'0'-1;
				FOR(j,i+1,s.size()){
					ans[j] = 9;
				}
			}else{
				ans[i] = s[i]-'0';
			}
		}
	}
	bool outhead = false;
	cout << "Case #" << c <<": ";
	REP(i,s.size()){
		if(!outhead && ans[i])outhead = true;
		if(outhead)cout << ans[i];
	}
	cout << endl;
	}
  return 0;
}

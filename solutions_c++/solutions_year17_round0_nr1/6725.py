#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <cassert>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
typedef pair<int,P> P1;
typedef pair<P,P> P2;
#define pu push
#define pb push_back
#define mp make_pair
#define eps 1e-7
#define INF 1000000000
#define fi first
#define sc second
#define rep(i,x) for(int i=0;i<x;i++)
#define SORT(x) sort(x.begin(),x.end())
#define ERASE(x) x.erase(unique(x.begin(),x.end()),x.end())
#define POSL(x,v) (lower_bound(x.begin(),x.end(),v)-x.begin())
#define POSU(x,v) (upper_bound(x.begin(),x.end(),v)-x.begin())
int t,a;
string s;
int main()
{
	cin >> t;
	for(int i=1;i<=t;i++){
		cin >> s >> a; int c = 0;
		for(int j=0;j<=s.size()-a;j++){
			if(s[j] == '+') continue;
			c++;
			for(int jj=j;jj<j+a;jj++) s[jj] = (s[jj]=='-')?'+':'-';
		}
		for(int j=0;j<s.size();j++) if(s[j] == '-') goto fail;
		printf("Case #%d: %d\n",i,c); continue;
		fail:;printf("Case #%d: IMPOSSIBLE\n",i);
	}
}
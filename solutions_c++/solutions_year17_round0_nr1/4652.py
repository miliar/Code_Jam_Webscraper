#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <exception>
#include <numeric>
#include <algorithm> 
#include <sstream>
#include <cstring>
#include <deque>
using namespace std;
 
typedef long long lo;
typedef vector< vector<long long> > vvl;
typedef vector< long long> vl;
typedef pair<lo, lo> ll;
typedef vector< pair<lo, lo> > vll;
typedef vector< vll > vvll;
typedef pair<long, pair<long, long> > lll;
typedef vector<lll> vlll;
typedef vector<vvl> vvvl;
typedef vector<set<lo> > vs;
typedef map<lo, map<lo, lo> > mm;
const double PI = 3.141592653589793;

#define N 1100

char s[N];
bool a[N];

lo solve(){
	cin >> s;
	lo k, ans=0;
	cin >> k;
	lo n=strlen(s);
	for (lo i=0;i<n;i++)
		a[i]=s[i]=='+';
	
	for (lo i=0;i<n-k+1;i++) 
		if (!a[i]) {
			// cout << i << " ";
			ans++;
			for (lo j=i;j<i+k;j++)
				a[j]=!a[j];
		}
	for (lo i=0;i<n;i++)
		if (!a[i]){
			// cout << ans;
			return -1;
		}

	return ans;	
}

int main() {
	freopen("A-large(2).in","r",stdin);
	freopen("output.txt","w",stdout);
	lo t;
	scanf("%I64d", &t);
	for (lo i=1;i<=t;i++) {
		lo res = solve();
		if (res!=-1) 
			printf("Case #%I64d: %I64d\n", i, res);
		else 
			printf("Case #%I64d: IMPOSSIBLE\n", i);
	}
	return 0;
}
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

#define N 1010
lo k[N], s[N];

double solve(){
	lo d, n;
	scanf("%I64d%I64d", &d, &n);
	for (lo i=0;i<n;i++)
		scanf("%I64d%I64d", &k[i], &s[i]);
	lo argmax=0;
	for (lo i=1;i<n;i++)
		if ((d-k[i])*s[argmax]>=(d-k[argmax])*s[i])
			argmax=i;
	double ans=d*s[argmax] / ((double)(d-k[argmax]));	
	return ans;	
}

int main() {
	freopen("A-large(3).in","r",stdin);
	freopen("tcoA.txt","w",stdout);
	lo t;
	scanf("%I64d", &t);
	for (lo i=1;i<=t;i++) {
		printf("Case #%I64d: %.9f\n", i, solve());
	}
	return 0;
}
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

typedef long long ll;
#define INF 2000000000
#define MOD 1000000007
#define endl '\n'

int main(){
	ios::sync_with_stdio(false);
	int t,tc,d,n,s,k,i;
	double diff,maxT,time;
	cin >> t;
	tc = t;
	while(tc--){
		cout << "Case #" << t-tc << ": ";
		cin >> d >> n;
		maxT = 0;
		for(i=0;i<n;++i){
			cin >> k >> s;
			diff = (d-k);
			time = float(diff)/s;
			maxT = max(maxT,time);
		}
		cout << fixed << d/maxT << endl;
	}
	return 0;
}


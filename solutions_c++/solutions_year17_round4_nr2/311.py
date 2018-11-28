#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <sstream>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <utility>
#include <complex>

using namespace std;
typedef long long ll;
typedef double ld;

typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef complex<ll> pt;

int p[1<<10];
int b[1<<10];

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		int n, c, m; cin >> n >> c >> m;
		memset(p,0,sizeof(p));
		memset(b,0,sizeof(b));
		for (int i = 0; i < m; i++){
			int t1,t2; cin >> t1 >> t2;
			p[t1]++;
			b[t2]++;
			//cout << p[t1] << " " << b[t2] << endl;
		}
		int rides = 0;
		for (int i = 1; i <= c; i++)
			rides = max(rides, b[i]);
		int sum = 0;
		for (int i = 1; i <= n; i++){
			sum += p[i];
			rides = max(rides, (sum + i - 1)/i);
		}
		
		int pros = 0;
		for (int i = n; i > 0; i--){
			if (p[i] > rides) pros += p[i] - rides;
		}
		cout << "Case #" << zz << ": " << rides << " " << pros << endl;
	}
	
	return 0;
}

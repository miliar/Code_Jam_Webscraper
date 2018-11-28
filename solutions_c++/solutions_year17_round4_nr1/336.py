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

int g[1<<7];
int cnt[4];
int cntmod[4];

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		int n; cin >> n;
		int p; cin >> p;
		for (int i = 0; i < n; i++)
			cin >> g[i];
			
		for (int i = 0; i < 4; i++)
			cnt[i] = 0;
		for (int i = 0; i < n; i++){
			cnt[g[i]%p]++;
		}
		for (int i = 0; i < p; i++)
			cntmod[i] = cnt[i] % p;
		int ans;
		
		if (p == 2){
			ans = cnt[0] + (cnt[1]+1)/2;
		}
		
		else if (p == 3){
			int diff = max(cnt[1]-cnt[2],cnt[2]-cnt[1]);
			ans = cnt[0] + min(cnt[1],cnt[2]) + (diff+2)/3;
		}
		
		else if (p == 4){
			int diff = max(cnt[1]-cnt[3],cnt[3]-cnt[1]);
			int ma = max(cnt[1],cnt[3]);
			ans = cnt[0] + min(cnt[1],cnt[3]) + cnt[2]/2;
			if (cnt[2] % 2 == 1){
				if (diff <= 1) ans += 1;
				else ans += 1 + (diff+1)/4;
			}
			else ans+= (diff+3)/4;
		}
		cout << "Case #" << zz << ": " << ans << endl;
	}
	
	return 0;
}

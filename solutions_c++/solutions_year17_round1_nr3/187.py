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

const ld eps = 1e-9;

ll max (ll a, ll b){
	if (a > b) return a;
	return b;
}

int main(){
	int tt; cin >> tt;
	for (int zz = 1; zz <= tt; zz++){
		ll hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;
		
		ll atk_turns, temp;
		ll x;
		if (b > 0){
			x = (ll) (floor(sqrt((ld) hk / (ld) b) - (ld) ad / (ld) b + eps));
			if (x < 0) x = 0;
			atk_turns = x + (ll) ((hk+ad+b*x-1) / (ad+b*x));
			temp = x+1 + (ll) ((hk+ad+b*(x+1)-1) / (ad+b*(x+1)));
			if (atk_turns > temp) atk_turns = temp;
		}
		else{
			x = 0;
			atk_turns = x + (ll) ((hk+ad+b*x-1) / (ad+b*x));
		}
		//cout << "x = " << x << ", y = " << ((ll) ((hk+ad+b*x-1) / (ad+b*x))) << ", atk_turns = " << atk_turns << endl;
		
		if (atk_turns == 1){
			cout << "Case #" << zz << ": 1" << endl;
			continue;
		}
		else if (hd <= ak - d){
			cout << "Case #" << zz << ": IMPOSSIBLE" << endl;
			continue;
		}
		else if (atk_turns == 2){
			cout << "Case #" << zz << ": 2" << endl;
			continue;	
		}
		else if (hd <= ak - d + max(ak - 2*d, 0)){
			cout << "Case #" << zz << ": IMPOSSIBLE" << endl;
			continue;	
		}
		
		ll tot_turns = 1e15;
		ll nd = ak;
		ll debuff_turns = 0;
		ll rem_hp = hd;
		//bool okay = true;
		while (true){
			//cout << "debuff_turns = " << debuff_turns << ", nd = " << nd << ", rem_hp = " << rem_hp << endl;
			ll curr_cnt;
			if (nd == 0){
				curr_cnt = debuff_turns + atk_turns;
				if (tot_turns > curr_cnt) tot_turns = curr_cnt;
				break;
			}
			else{
				//cout << "here" << endl;
				ll interval = (hd-1) / nd;
				if (interval < 2){
					//cout << "here5" << endl;
					if (rem_hp <= nd - d){
						debuff_turns++;
						rem_hp = hd - nd;
					}
					else{
						debuff_turns++;
						nd -= d;
						if (nd < 0) nd = 0;
						rem_hp -= nd;
					}
					continue;
				}
				ll rem_interval = (rem_hp-1)/nd;
				//cout << "here4" << endl;
				if (atk_turns <= rem_interval+1){
					curr_cnt = debuff_turns + atk_turns;
					if (tot_turns > curr_cnt) tot_turns = curr_cnt;
					break;
					//cout << "here3" << endl;
				}
				else{
					//cout << "here2" << endl;
					curr_cnt = debuff_turns + atk_turns + (atk_turns - (rem_interval+1) + (interval-2))/(interval-1);
					if (tot_turns > curr_cnt) tot_turns = curr_cnt;
					if (rem_hp <= nd - d){
						debuff_turns++;
						rem_hp = hd - nd;
					}
					else{
						debuff_turns++;
						nd -= d;
						if (nd < 0) nd = 0;
						rem_hp -= nd;
					}
					if (d == 0) break;
				}
				
				
			}
			
		}
		cout << "Case #" << zz << ": " << tot_turns << endl;
		
	}
	
	return 0;
}

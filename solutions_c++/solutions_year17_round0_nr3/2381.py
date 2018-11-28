#include <string.h>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <functional>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <cstdio>
using namespace std;
#define sz(a)  int((a).size())
#define all(a) a.begin(), a.end()
#define pb push_back
#define mp make_pair
#define CLR(a) memset((a), 0, sizeof(a))
#define INF (1 << 31) - 1
const int dh[8] = {-1, 1, 0, 0,1,1,-1,-1};
const int dw[8] = {0, 0, 1, -1,1,-1,1,-1};
typedef long long ll;
typedef pair<ll, ll> p;
typedef vector <int> VI;
typedef vector <string> VS;

int main(){

	int tn;
	cin >> tn;
	
	for(int i = 1; i <= tn; i++){
		ll n,k;
		cin >> n;
		cin >> k;
		
		ll groupnum = 0;
		ll groupsize = 1;
		ll tally = 0;
		
		while(k > tally){
			tally += groupsize;
			groupsize *= 2;
			groupnum++;		
		}
		
		ll base = (n - tally) / (tally + 1);
		ll surplus = (n - tally) % (tally + 1);
		ll r = base;
		ll l = base;
		if((k - (tally - groupsize / 2)) <= surplus) r++;
		if((k - (tally - groupsize / 2)) + (groupsize / 2) <= surplus) l++;		
		
		cout << "Case #" << i << ": ";
		cout << r << " " << l << endl;
	}
	return 0;	
}

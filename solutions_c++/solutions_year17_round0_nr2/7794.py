#include <algorithm>
#include <cstdio>
#include <cmath>
#include <iterator>
#include <bitset>
#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <queue>
#include <deque>
#include <cassert>
#include <string>
#include <cstring>
#include <climits>

using namespace std;

#define ll long long
#define pii pair<int, int>
#define vi vector<int>
#define mp make_pair
#define pb push_back
#define fs first
#define sc second
#define sz(x) (int)x.size()
#define fill(x,a) memset(x, a, sizeof(x))
#define sortall(x) sort(x.begin(), x.end())


ll n, digs;
vi num;

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);


	int T;
	cin>>T;
	for(int t=1; t<=T; t++) {

		cin>>n;
		ll temp;
		while(1) {

			temp = n;
			num.clear();
			while(temp) {
				num.pb(temp%10);
				temp/=10;
			}
			reverse(num.begin(), num.end());


			digs = num.size();
			int i;
			for( i=0; i<digs-1; i++) {
				if(num[i+1]<num[i]) {
					break;
				}
			}
			if(i>=digs-1) {
				break;
			}
			ll res = 0;
			for(int j=0; j<=i; j++) {
				res = res*10+num[j];
			}
			res--;
			num.clear();
			while(res) {
				num.pb(res%10);
				res/=10;
			}
			reverse(num.begin(), num.end());
			for(int j=i+1; j<digs; j++) {
				num.pb(9);
			}
			n = 0;
			for(i=0; i<num.size(); i++) {
				n = n*10+num[i];
			}
			
		}

		cout<<"Case #"<<t<<": "<<n<<"\n";
	}

	return 0;
}






















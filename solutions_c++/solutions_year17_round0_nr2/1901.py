#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vl = vector<ll>;
using vvl=vector<vl>;
using vb=vector<bool>;
using vs=vector<string>;
using pll=pair<ll,ll>;
const ll oo = 0x3f3f3f3f3f3f3f3fLL;
const double eps = 1e-9;
#define sz(c) ll((c).size())
#define all(c) begin(c),end(c)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define FR(i,a,b) for(ll i = (a); i < (b); i++)
#define FRD(i,a,b) for(ll i = ll(b)-1;i>=(a);i--)
#define TR(X) ({if(1) cerr << "TR: " << (#X) << " = " << (X) << endl; })

int main() {
	ios_base::sync_with_stdio(false);
	ll tc;
	cin >> tc;
	cin.ignore();
	FR(a,0,tc) {
		string number;
		ll llnum;
		//getline(cin, number);
		cin >> llnum;
		number = to_string(llnum);
		if(number.size() > 1) {
			int eqidx = 0;
			FR(b,0,number.size()-1) {
				if(number[b] < number[b+1]) {
					eqidx = b+1;
				}
				else if(number[b] > number[b+1]) {
					number[eqidx]--;
					FR(b,eqidx+1,number.size()) {
						number[b] = '9';
					}
					break;
				}
			}
			llnum = stoll(number);
			number = to_string(llnum);
		}
		cout << "Case #" << a+1LL << ": " << number << '\n';
	}
}

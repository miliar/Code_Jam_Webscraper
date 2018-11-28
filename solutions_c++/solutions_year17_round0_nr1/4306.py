#define NDEBUG
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>
#include <bitset>
#include <vector>
#include <stack>
#include <queue>
#include <tuple>
#include <set>
#include <unordered_map>
#include <utility>
using namespace std; 

typedef long long ll;

// utility macros
#define pb push_back
#define mp make_pair
#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define FOR(i,a,b) for (ll i=a; i<b; i++)
#define ALL(v) v.begin(),v.end()
#define STOI(s) atoi(s.c_str())
#define ITOS(i) std::to_string(i) 

int main()
{
	std::ios_base::sync_with_stdio(false);cout.precision(12);cout<<fixed;
	int T;
	cin >> T;
	int t = 0;
	while (t++ < T) {
		vector<bool> pancake;
		string pan;
		cin >> pan;
		for (char ch : pan) {
			if (ch=='+') pancake.pb(1);
			if (ch=='-') pancake.pb(0);
		}
		int flipper; 
		cin >> flipper;
		int flips = 0;
		int i;
		for (i=0; i<pancake.size()-(flipper-1); i++) {
			if (pancake[i] == 0) {
				for (int j=i; j<i+flipper; j++) {
					pancake[j] = !pancake[j];
				}
				flips++;
			}
			else if (pancake[i] == 1) {
				continue;
			}
		}
		bool done = true;
		for (; i<pancake.size(); i++) {
			if (pancake[i] != 1)
				done = false;
		}
		if (done)
			cout << "Case #" << t << ": " << flips << "\n";
		else 
			cout << "Case #" << t << ": IMPOSSIBLE\n";
	}
}















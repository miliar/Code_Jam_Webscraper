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
	for (int t=1; t<=T; t++) {
		string N;
		cin >> N;
		for (int i=0; i<N.size()-1; i++) {
			if (N[i] > N[i+1]) {
				// not tidy
				int b = i;
				while (N[b] == '0') b--;
				N[b] -= 1;
				for (int j=b+1; j<N.size(); j++) {
					N[j] = '9';
				}
				if (N[i-1] > N[i]) i-=2;
			}
		}
		for (int i=0; i<N.size(); i++) {
			if (N[i]!='0') {
				cout << "Case #" << t << ": " << N.substr(i) << "\n";
				break;
			}
		}
	}
}















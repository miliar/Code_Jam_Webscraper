#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i = 0; i < int(n); ++i)
#define trav(a,x) for(auto &a : x)

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;

int main(){
	cin.sync_with_stdio(0);
	int t;
	cin >> t;
	rep(id, t){
		string s;
		int k, a = 0;
		cin >> s >> k;
		bitset<1000> b = {};
		rep(i,s.size()) if(s[i] == '+') b[i] = 1;

		rep(i, s.size()-k+1){
			//cout << endl;rep(i,s.size()) cout << b[i] << " ";
			//cout << endl;
			if(!b[i]){
				++a;
				for(int j = i; j < i+k; ++j) b[j] = !b[j];
			}
		}

		//rep(i,s.size()) cout << b[i] << " ";

		for(int i = s.size()-k+1; i < s.size(); ++i){
			if(!b[i]){
				cout << "Case #" << id+1 << ": IMPOSSIBLE" << endl;
				a = -1;
				break;
			}
		}
		if(a != -1){
			cout << "Case #" << id+1 << ": " << a << endl;
		}
	}
	exit(0);
}
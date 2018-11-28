#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = (a); i < int(b); ++i)
#define rrep(i,b,a) for(int i = (b); i --> int(a);)
#define trav(i,v) for(auto&i:v)
#define all(c) (c).begin(), (c).end()
#define sz(c) int((c).size())
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	rep(t,1,T+1){
		int N;
		cin >> N;
		auto tidy = [&](int a){
			int p = 10;
			while(a > 0){
				if(a%10 > p) return 0;
				p = a%10;
				a /= 10;
			}
			return 1;
		};
		while(!tidy(N)) --N;
		cout << "Case #" << t << ": " << N << endl;
	}
}
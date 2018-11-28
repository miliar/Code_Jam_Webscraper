#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define repu(i,a,b) for(int i=a;i<=b;i++)
#define repd(i,b,a) for(int i=b;i>=a;i--)
typedef long long LL;
typedef pair<int,int> ii;
typedef vector<int> vi;

int k, ans;
vector<bool> cakes;
void load(string& S){
	cakes.resize(S.size());
	rep(i, S.size()) {
		cakes[i] = S[i] == '+'? true: false;
	}
}
void flip(int pos) {
	ans ++;
	rep(i,k) {
		cakes[pos + i] = !cakes[pos + i];
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	int kase = 0, T;
	string S;
	cin >> T;
	while(kase < T){
		cin >> S >> k;
		load(S);
		bool flag = true;
		ans = 0;
		rep(i, cakes.size()) {
			if(!cakes[i]) {
				if(i + k > cakes.size()) {
					flag = false;
					break;
				}
				flip(i);
			}
		}
		cout<<"Case #"<<++kase<<": ";
		if(flag) {
			cout << ans << endl;
		}
		else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
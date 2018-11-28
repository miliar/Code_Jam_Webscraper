#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;

typedef long double ld;
typedef long long ll;

int n, c, m;

vector<int> t[1234];
int p[1234];
int cnt;

int upgrades(int rides){
	if(rides < cnt) return -1;
	int sm = 0;
	int ans = 0;
	//cerr << rides << " " << cnt << endl;
	REP(pos, n){
		sm+=p[pos];
		if(rides < (sm+pos)/(pos+1)){
			return -1;
		}
		ans+=max(0, p[pos]-rides);
	}
	return ans;
}

void testcase(int tcn){

	cin >> n >> c >> m;

	REP(i, c)t[i].clear();
	REP(i, n)p[i] = 0;

	int cus, pos;
	REP(i, m){
		cin >> pos >> cus;
		--cus; --pos;
		t[cus].push_back(pos);
		++p[pos];
	}

	cnt = 0;

	REP(i, c){
		cnt = max(cnt, (int)t[i].size());
	}

	int ans = 1000000;
	int l = 0, r = 1000000;
	while(r-l > 1){
		int m = (l+r)/2;
		int tmp = upgrades(m);
		if(tmp == -1){
			l = m;
		} else{
			r = m;
			ans = tmp;
		}
	}



	cout << "Case #"<< tcn<<": "<<r << " " << ans<<endl;

}

int main(){
	int T;
	cin >> T;
	REP(i, T){
		testcase(i+1);
	}
	return 0;

}
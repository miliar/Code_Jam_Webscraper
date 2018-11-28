#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

using namespace std;

typedef long double ld;
typedef long long ll;

int n, p;
int g[123];
int cnts[5];

void testcase(int tcn){

	cin >> n >> p;
	REP(i, n)cin >> g[i];

	REP(i, p)cnts[i] = 0;

	REP(i, n) ++cnts[g[i] % p];

	int ans = cnts[0];

	if(p == 2){
		ans += (1+cnts[1])/2;
	}
	if(p == 3){
		int x = max(cnts[1], cnts[2]),
			y = min(cnts[1], cnts[2]);
		ans += y;
		x-=y;
		ans += (2+x)/3;
	}
	if(p == 4){
		int x = max(cnts[1], cnts[3]),
			y = min(cnts[1], cnts[3]);
		ans += y;
		x-=y;
		int z = cnts[2];
		ans += z/2;
		z = z % 2;
		if(z == 0){
			ans+=(3+x)/4;
		} else{
			if(x < 2){
				++ans;
			} else{
				ans+=1+(1+x)/4;
			}
		}
	}



	cout << "Case #"<< tcn<<": "<<ans<<endl;

}

int main(){
	int T;
	cin >> T;
	REP(i, T){
		testcase(i+1);
	}
	return 0;

}

#include <iostream>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>
#include <stdio.h>


using namespace std;

#define MAXN 1000
#define M_PI 3.14159265358979323846

typedef long long ll;

int cmptype = 0;

struct Cake{
	ll r;
	ll h;
	ll s;

	bool operator<(const Cake &a) {
		if(cmptype == 0) return r < a.r;
		else return s < a.s;
	}
};

ll get_max(vector<Cake> pc, int K){
	ll max_ans = 0;
	cmptype = 0;
	sort(pc.begin(),pc.end());
	while(pc.size() >= K){
		ll rmax = pc.back().r;
		ll ans = rmax*rmax + 2*rmax*pc.back().h;

		pc.pop_back();

		cmptype = 1;

		sort(pc.begin(),pc.end());

		int j=pc.size()-1;
		int cnt = 1;
		while(cnt < K){

			ans += 2*pc[j].r*pc[j].h;
			cnt++;
			j--;
		}
		if(ans < 0) cout << "HERE IS OVERFLOW!" << endl;

		cmptype = 0;
		sort(pc.begin(),pc.end());
		if(ans > max_ans) max_ans = ans;
	}
	return max_ans;
}

int main(){
	int T;
	cin >> T;

	for(int tsc=0; tsc<T; tsc++){
		int N,K;
		cin >> N >> K;
//		if(tsc+1 == 13) cout << N<<" "<<K<<endl;

		vector<Cake> pc;
		for(int i=0; i<N; i++){
			ll r,h;
			cin >> r >> h;
//			if(tsc+1 == 13){
//				cout << r<<" "<<h<<endl;
//			}
			Cake c;
			c.r = r;
			c.h = h;
			c.s = r*h;
			pc.push_back(c);
		}

//		sort(pc.begin(),pc.end());
//
//		ll rmax = pc.back().r;
//		ll ans = rmax*rmax + 2*rmax*pc.back().h;
//
//		pc.pop_back();
//
//		cmptype = 1;
//
//		sort(pc.begin(),pc.end());
//
//		int j=pc.size()-1;
//		int cnt = 1;
//		while(cnt < K){
//			ans += 2*pc[j].r*pc[j].h;
//			cnt++;
//			j--;
//		}
		ll ans = get_max(pc,K);

		cout.precision(17);

		long double dans = ans * 3.141592653589793238462643383279l;


		//cout << "Case #" << tsc+1<<": " << fixed << dans << endl;
		printf("Case #%d: %1.20Lf\n",tsc+1,dans);

		// Remeber multiply with pi
	}
}


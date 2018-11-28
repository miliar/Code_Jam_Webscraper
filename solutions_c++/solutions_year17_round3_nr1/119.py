#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
using namespace std;

double PI = 3.14159265358979;
struct cake{
	long long r,h;
};
vector<cake> v(0);

bool cmp(cake a, cake b){
	return a.r*a.h > b.r*b.h;
}
int main(){
	int T; cin >> T;
	for (int t=1;t<=T;t++){
		v.clear();
		int N,K; cin >> N >> K;
		for (int i=0;i<N;i++){
			cake tmp; cin >> tmp.r >> tmp.h;
			v.push_back(tmp);
		}
		sort(v.begin(),v.end(), cmp);
		double ans = 0.;
		for (int i=0;i<N;i++){ //choose v[i]
			double tmpans = PI * v[i].r * v[i].r + 2*PI*v[i].r*v[i].h;
			int cn = 1;
			for (int j=0;j<N;j++){
				if (cn == K) break;
				if (i==j) continue;
				if (v[j].r > v[i].r) continue;
				tmpans += 2*PI*v[j].r * v[j].h;
				cn++;
				
			}
			if (cn == K) ans = max(ans, tmpans);
		}
		printf("Case #%d: %.9lf\n",t,ans);
	}
}

#include<bits/stdc++.h>
using namespace std;

double dim(double r, double h){
	return 2 * M_PI * r * h;
}

struct cake{
	double r;
	double h;

    bool operator>( const cake& right ) const {
        return dim(r, h) > dim(right.r, right.h);
    }

};


void solve(){
	long long N, K;
	cin >> N >> K;
	vector<struct cake> cakes;

	for(long long i = 0; i < N; i++){
		struct cake c;
		cin >> c.r >> c.h;
		cakes.push_back(c);
	}

	double ans = 0;
	for(int i = 0; i < N; i++){
		struct cake use = cakes[i];
		vector<struct cake> wcakes;
		for(int j = 0; j < N; j++){
			if(i != j){
				wcakes.push_back(cakes[j]);
			}
		}
		sort(wcakes.begin(), wcakes.end(), greater<struct cake>());

		double tmp = dim(use.r, use.h);
		double maxr = use.r;

		for(int j = 0; j < K-1; j++){
			tmp += dim(wcakes[j].r, wcakes[j].h);
			maxr = max(maxr, wcakes[j].r);
		}

		tmp += M_PI * maxr * maxr;
		ans = max(ans, tmp);
	}
	printf("%.10f\n", ans);
}

int main(){
	long long T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cout << "Case #" << i + 1 << ":" << " ";
		solve();
	}
}


#include <bits/stdc++.h>
using namespace std;
int X[1111], Y[1111];
int main(){
	int t; cin >> t;
	int cs = 0;
	int N, M, C;
	while(t--){
		memset(X, 0, sizeof X);
		memset(Y, 0, sizeof Y);
		++cs;
		cin >> N >> C >> M;
		int trips = 0, pr = 0;
		for(int i=1; i<=M; ++i){
			int x, y; cin >> x >> y;
			if(y & 1) X[x]++;
			else Y[x]++;
		}
		int clashes = 0;
		for(int i=1; i<=N; ++i) clashes += min(X[i], Y[i]);
		for(int i=1; i<=N; ++i){
			if(X[i]){
				for(int j=1; j<=N; ++j){
					if(i == j) continue;
					while(X[i] && Y[j] && X[j]){
						--X[i];
						--Y[j];
						++trips;
					}
				}
				for(int j=1; j<=N; ++j){
					if(i == j) continue;
					while(X[i] && Y[j]){
						--X[i];
						--Y[j];
						++trips;
					}
				}
			}
		}

		int xx = 0, yy = 0;
		for(int i=1; i<=N; ++i){
			if(X[i]) xx = 1;
			if(Y[i]) yy = 1;
		}
		if(xx == 0){
			for(int i=1; i<=N; ++i) trips += Y[i];
		}
		else if(yy == 0){
			for(int i=1; i<=N; ++i) trips += X[i];
		}
		else{
			int c = 0;
			for(int i=1; i<=N; ++i){
				if(X[i] && Y[i]){
					c++;
					if(i == 1){
						trips = trips + X[i] + Y[i];
					}
					else{
						trips = trips + max(X[i], Y[i]);
						pr += min(X[i], Y[i]);
					}
				}
			}
			assert(c <= 1);
		}
		cout << "Case #" << cs << ": " << trips << ' ' << pr << endl; 
	}
}
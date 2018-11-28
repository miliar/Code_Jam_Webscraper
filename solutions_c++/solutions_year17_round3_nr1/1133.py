#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int T, N, K;

class pancake{
public:
	long long r, h;
};

bool cmpRadius(pancake a, pancake b){
	return a.r > b.r;
}

bool cmpLateralArea(pancake a, pancake b){
	return a.r*a.h > b.r*b.h;
}

vector<pancake> V;

void print(){
	for(int i=0;i<V.size();i++)
		cout << V[i].r << " " << V[i].h << endl;
	cout << endl;
}

int main(){

	int testCase = 1;
	cin >> T;
	for(int j=0;j<T;j++){
		cin >> N >> K;
		pancake x;
		for(int i=0;i<N;i++){
			cin >> x.r >> x.h;
			V.push_back(x);
		}

		double max_res = 0;
		for(int i=0;i<N-K+1;i++){
			
			sort(V.begin()+i, V.end(), cmpRadius);
			long long res = V[i].r* (V[i].r + 2*V[i].h);
			sort(V.begin()+i+1, V.end(), cmpLateralArea);
			for(int k=i+1;k<i+K;k++)
				res += 2*V[k].r*V[k].h;
			max_res = max(max_res, (double)(res * M_PI));
		}
		cout << "Case #" << testCase++ << ": ";
		printf("%.9lf\n", max_res);
		V.clear();
	}
	return 0;
}
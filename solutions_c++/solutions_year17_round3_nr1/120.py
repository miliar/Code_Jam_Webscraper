#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
#define PI 3.1415926535897932384626433832795028841971


int T;

struct Pancake{
	long long R;
	long long H;
	long long SH;
} pancake[1003];

int cmp(const Pancake& lhs, const Pancake& rhs){
	return lhs.SH > rhs.SH;
}

double get(int i, long long minR){
	long long R = max(minR, pancake[i].R);
	return PI * pancake[i].SH*2 + PI * R * R;
}

int main(){
	cin>>T;
	for(int cs = 1; cs<=T; ++cs){
		int K, N;
		cin>>N>>K;
		for(int i = 0; i< N; ++i){
			cin>>pancake[i].R>>pancake[i].H;
			pancake[i].SH = pancake[i].R * pancake[i].H;
		}

		std::sort(pancake, pancake+N, cmp);

		long long res = 0;
		int mR = 0;
		for(int i = 0; i<K-1; ++i){
			if(pancake[i].R > mR){
				mR = pancake[i].R;
			}
			res +=pancake[i].SH;
		}

		double tres = 0;
		for(int j = K-1; j<N; ++j){
			tres = max(tres, get(j, mR));
		}
		
		double lres = PI * res * 2  + tres;
		printf("Case #%d: %.9f\n", cs, lres);
	}
	return 0;
}

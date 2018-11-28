#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

const long double pi = 3.14159265358979323846264338;// 3.1415926535897;

struct C {
	long long r;
	long long h;
};

bool compareByH(C a, C b){
	return a.h * a.r > b.h * b.r;
}

bool compareByR(C a, C b){
	return a.r > b.r;
}

void _main(){
	int n,k;
	vector <C> cakes;
	long long maxArea = 0;
	
	scanf("%d %d", &n, &k);
	for(int i=0;i<n;i++){
		C cake;
		scanf("%lld %lld", &cake.r, &cake.h);
		cakes.push_back(cake);
	}

	sort(cakes.begin(), cakes.end(), compareByR);

	vector<C>::iterator it = cakes.begin();
	for(int i=0;i<=n-k;i++){
		it++;
		vector <C> filtered (it, cakes.end());
		sort(filtered.begin(), filtered.end(), compareByH);

		long long cArea = (cakes[i].r * cakes[i].r); //area of base
		cArea += 2 * cakes[i].r * cakes[i].h;

		for(int x=0;x<k-1;x++){
			cArea += 2 * filtered[x].r * filtered[x].h;
		} 

		maxArea = max(maxArea, cArea);
	}

	printf("%.9Lf\n", maxArea * pi);

}

int main() {
	int T;
	scanf("%d", &T);
	for(int i=1;i<=T;i++){
		printf("Case #%d: ", i);
		_main();
	}
	return 0;
}
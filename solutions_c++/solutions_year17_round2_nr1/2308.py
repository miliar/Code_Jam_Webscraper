#include <bits/stdc++.h>

using namespace std;

const int N=1000070; //10e6

#define ll long long int
#define inf 0x3f3f3f3f
#define pb push_back
#define eb emplace_back
#define fi first
#define se second
#define ii tuple<int, int>
#define all(x) (x).begin(), (x).end()

int main(int argc, char const *argv[]){
	int t, counter=1;
	scanf("%d", &t);
	while(t--){
		double d;
		int n;
		scanf("%lf %d", &d, &n);
		double te=0.0;

		for(int i=0; i<n; i++){
			double a, b;
			scanf("%lf %lf", &a, &b);
			if(a<d)te=max(te, ((d-a)/b));
		}
		printf("Case #%d: %lf\n", counter++, d/te);
	}
	return 0;
}
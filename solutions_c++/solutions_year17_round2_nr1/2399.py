#include<stdio.h>
#include<vector>
#include<algorithm>
#include<string>
#include<map>
#include<math.h>

#define ll long long
using namespace std;


int n;
double s;

double sol() {
	int i, j;
	double ans = 0;
	scanf("%lf%d", &s, &n);
	for(i=0; i<n; i++) {
		double p, v;
		scanf("%lf %lf", &p ,&v);
		double t = (s - p)/v;
		ans = max(t, ans);
	}
	return s/ans;
}

int main(){
#pragma comment(linker, "/STACK:1073741824")
#ifdef _DEBUG
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#else
	//freopen("absmarkchain.in", "r", stdin);
	//freopen("absmarkchain.out", "w", stdout);
#endif
	int t;
	scanf("%d",&t);
	for(int i =0; i < t;i++) {
		printf("Case #%d: %.10lf\n",i+1 ,sol());
	}
	return 0;
}
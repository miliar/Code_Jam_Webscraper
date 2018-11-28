#include <cstdio>
#include <vector>
#include <set>
#include <unordered_map>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

void solve(){
	int n,k;
	scanf("%d %d",&n,&k);
	double u;
	scanf("%lf", &u);
	u-=1e-12;
	vector<double> p;
	for(int i=0; i<n; i++){
		double q;
		scanf("%lf", &q);
		p.push_back(q);
	}
	p.push_back(1);
	sort(p.begin(), p.end());
	for(int i=1; ; i++){
		// We want to move first i cores to the level of ith
		double uneeded=i*(p[i]-p[0]);
		if(u>uneeded){
			u-=uneeded;
			for(int j=0; j<i; j++){
				p[j]=p[i];
			}
		}
		else{
			double add=u/i;
			for(int j=0; j<i; j++){
				p[j]+=add;
			}
			break;
		}
	}
	double pok=1;
	for(auto pr: p){
		pok*=pr;
	}
	printf("%.9lf\n", pok);
}

int main(){
	int t;
	scanf("%d", &t);
	for(int tc=0; tc<t; tc++){
		fprintf(stderr, "%d/%d\n", tc, t);
		printf("Case #%d: ", tc+1);
		solve();
	}
}

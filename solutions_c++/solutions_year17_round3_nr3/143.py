#include <bits/stdc++.h>

using namespace std;

int t,i,j,n,k;
double u;

int main(){
	scanf("%d", &t);
	int tc = 0;
	
	while(t--){
		tc++;
		
		scanf("%d%d%lf", &n, &k, &u);
		
		vector <double> a;
		
		for(i = 0; i < n; i++){
			double tmp;
			scanf("%lf", &tmp);
			a.push_back(tmp);
		}
		
		sort(a.begin(), a.end());
		reverse(a.begin(), a.end());
		
		for(i = 0; i < n; i++){
			double diff = 0;
			for(j = i + 1; j < n; j++)
			diff += a[i] - a[j];
			
			if(diff > u) continue;
			
			double tar = min(1.0, a[i] + (u - diff) / (n - i));
			
			for(j = i; j < n; j++)
			a[j] = tar;
			
			break;
		}
		
		double res = 1.0;
		
		for(i = 0; i < n; i++)
		res = res * a[i];
		
		printf("Case #%d: %.12lf\n", tc, res);
	}
}


#include <bits/stdc++.h>

using namespace std;

const double pi = 3.14159265359;
const double INF = 1e20;

int t,n,k,i,j;
pair <int, int> a[1005];


double area(int r){
	return pi * r * r;
}

double side(int id){
	return 2.0 * pi * a[id].first * a[id].second;
}

int main(){
	scanf("%d", &t);
	int tc = 0;
	
	while(t--){
		tc++;
		
		scanf("%d%d", &n, &k);
		for(i = 0; i < n; i++)
		scanf("%d%d", &a[i].first, &a[i].second);
		
		sort(a, a + n);
		reverse(a, a + n);
		
		double res = 0.0;
		
		for(i = 0; i < n; i++){
			double now = area(a[i].first) + side(i);
			vector <double> ans;
			for(j = i + 1; j < n; j++)
			ans.push_back(side(j));
			sort(ans.begin(), ans.end());
			reverse(ans.begin(), ans.end());
			
			if(ans.size() < k - 1) continue;
			for(j = 0; j < k - 1; j++)
			now += ans[j];
			
			res = max(res, now);
		}
		
		printf("Case #%d: %.12lf\n", tc, res);
	}
}

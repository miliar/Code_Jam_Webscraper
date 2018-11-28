#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include <iomanip>  
#include <algorithm>
#include <math.h>
using namespace std;

bool comp(double a, double b){
	return a < b;
}
int main(){
	int tt;
	cin >> tt;
	int n, k;
	double p;
	for(int it = 0; it < tt; it ++){		
		cin >> n >> k;
		cin >> p;
		vector<double> q(n);
		for(int i = 0; i < n; i ++){
			cin >> q[i];
		}
		
		double ans = 0.0;
		
		sort(q.begin(), q.end(), comp);
		
		vector<double> sum(n);
		sum[0] = q[0];
		for(int i = 1; i < n; i ++)sum[i] = sum[i-1] + q[i];
		
		if(sum[n-1] + p >= n)ans = 1.0;
		else{
			int index = n;
			for(int i = 0; i < n; i ++){
				if(p < q[i] * (i+1) - sum[i]){
					index = i;
					break;
				}
			}
			
			p-= index * q[index-1]-sum[index-1];
			double res = p/index;
			ans = 1.0;
			for(int i = index; i < n; i ++)ans*=q[i];
			ans*= pow(q[index-1]+ res, index);
			
		}
		
		cout << fixed << setprecision(8)<< "Case #" << it + 1 << ": " << ans<< endl;
		
	}
	return 0;
} 

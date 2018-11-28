#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;
int main(){
	int t = 0;
	cin>>t;
	for(int l = 1; l <= t; l++){
		int n = 0, q = 0;
		cin>>n>>q;
		vector<long long> h(n);
		vector<long long> s(n);
		for(int i = 0; i < n; i++)
			cin>>h[i]>>s[i];
		vector<long long> d(n, 0);
		for(int i = 0; i < n; i++){
			for(int j =0; j < n; j++){
				long long a = 0;
				cin>>a;
				if(a != -1)
					d[i+1] = d[i] + a;
			}
		}
		int f = 0, to = 0;
		cin>>f>>to;
		int pos = 0;
		vector<double> time(n, pow(10, 12));
		time[0] = 0;
		for(int i = 1; i < n; i++){
			for(int j = 0; j < i; j++)
				if(h[j] >= d[i]-d[j])
					if(time[j] + (double)(d[i]-d[j])/s[j] >= 0) 
						time[i] = min(time[i], time[j] + (double)(d[i]-d[j])/s[j]);
		}
		/*for(int i = 0; i < n; i++){
			if(s[pos] < s[i])
				pos = i;
			else if(h[pos] < d[i])
				pos = i;
			time += (double)d[i]/(double)s[pos];
			s[pos] -= d[i];
		}*/
		cout<<"Case #"<<l<<": ";
		printf("%.6f\n", time[n-1]);
	}
	return 0;
}
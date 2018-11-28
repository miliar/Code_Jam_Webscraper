#include <vector>
#include <cstdio>
#include <iostream>
#include <math.h>
#include <string>
#include <unordered_map>
#include <iomanip>

using namespace std;

int main(){
	int t, n, b;
	long long d, a;
	long double p, u, m;
	bool r;
	cin>>t;
	for(int y=1; y<=t; y++){
		r = false;
		cin>>d>>n;
		unordered_map<long long, int> s;
		std::vector<long long> k;
		for(int i = 0; i<n ;i++){
			cin>>a>>b;
			s[a] = b;	
			k.push_back(a);		
		}
		sort(k.begin(), k.end());
		for(int i = n-2; i>=0; i--){
			if(s[k[i]]>s[k[i+1]]){
			p = (long double)(k[i+1]*s[k[i]]-k[i]*s[k[i+1]])/(long double)(s[k[i]]-s[k[i+1]]);
			if(p<d){
				if(i == 0){
					r = true;
				}
				m = (long double)(p-k[i])/(long double)s[k[i]];
				s[k[i]] = s[k[i+1]];
				u = (long double)(d-p)/(long double)s[k[i]];
			}
		}
		}
		cout <<fixed;
    	cout <<std::setprecision(6);
		if(r){
		printf("Case #%d: %0.6Lf\n", y,(long double)((long double)d/(long double)(m+u)));
	}
	else{
printf("Case #%d: %0.6Lf\n", y,(long double)((long double)(s[k[0]]*d)/(long double)(d-k[0])));
	}
	}
	return 0;
}
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t; ++i){
		int n,k;
		double u,tmp;
		vector<double>p;
		cin >> n >> k >> u;
		for(int j=0;j<n;j++){
			cin >> tmp;
			p.push_back(tmp);
		}
		sort(p.begin(),p.end());
		for(int x=0;x<n;x++){
			if(x==(n-1)){
				for(int j=0;j<n;j++){
					p[j] += u/n;
				}
			}else{
				if((p[x+1]-p[x])*(x+1)<=u){
					for(int j=0;j<x+1;j++){
						u -= p[x+1]-p[j];
						p[j] = p[x+1];
					}
				}else{
					for(int j=0;j<x+1;j++){
						p[j] += u/(x+1);
					}
					break;
				}
			}
		}
		double ans =1;
		for(int j=0;j<n;j++){
			ans *= p[j];
		}
		if(ans>1)ans=1.0;
		if(ans<0)ans=0.0;
		std::cout.setf(std::ios_base::fixed,std::ios_base::floatfield);
		cout.precision(30);
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}
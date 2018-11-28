#include<iostream>
#include <iomanip>  
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i = 1;i<=t;i++){
		int n;
		double ans,d,p,s,max = 0;
		cin >> d >> n;
		for(int j = 0;j<n;j++){
			cin >> p >> s;
			max = max > (d-p)/s ? max: (d-p)/s;
		}
		cout << "Case #"<<fixed << setprecision(6)<<i<<": "<< d/max<< endl;
	
	}
	return 0;
}

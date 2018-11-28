#include<iostream>
#include<vector>
#include<map>
#include <iomanip>  
using namespace std;

int main(){
	int tt;
	cin >> tt;
	
	long long d, n;
	
	for(int it = 0; it < tt; it ++){		
		cin >> d >> n;
		
		long long a, b;
		
		double max = -1.0;
		
		for(int i = 0; i < n; i ++){
			cin >> a >> b;
			double res = double(d - a) / double(b);
			if(res > max)max = res;
		}
		
		double ans = (double)d / max;
		 cout.setf (ios::showpoint);
		cout << fixed << setprecision(6) << "Case #" << it + 1 << ": " << ans << endl;
		
	}
	return 0;
} 

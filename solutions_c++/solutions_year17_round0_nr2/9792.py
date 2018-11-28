#include <iostream>
#include <cmath>
using namespace std;

long long f(long long n){
	bool as = true;
	int c = 0;
	long long temp = n;
	while(temp != 0){
   		c++;
   		temp/=10;
	}
	temp = n;
	if (c==1){
		return n;
	}
	while(c > 1){
		long long x,y,ans;
		x = temp / (long long)(pow(10,c-1));
		y = (temp % (long long)(pow(10,c-1)))/(long long)(pow(10,c-2));
		temp = temp%(long long)(pow(10,c-1));
		if(x>y){
			as = false;
			ans = n - (temp + 1);
			//cout << " temp: " << temp << " " << "ans: " << ans << endl;
			return f(ans);
		}
		c--;
	}
	if (as){
		return n;
	}


}


int main(){
	int t,s=1;
	long long n;
	cin >> t;
	while(t--){
		cin >> n;
		long long temp,ans;
		bool as = true;
		int c = 0;
		temp = n;
		while(temp != 0){
	   		c++;
	   		temp/=10;
		}
		if(c == 1) cout << "Case #" << s << ": " << n << endl;
		else cout << "Case #" << s << ": " << f(n) << endl;
		s++;
	}
}
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

bool check(long long num){
	int last = num%10;
	num/=10;
	bool breaker = false;
	while(true){
		if(num < 10) breaker = true;
		int now = num%10;
		num/=10;
		
		if(now>last) return false;
		
		last = now;
		
		if(breaker) break;
	}
	return true;
}

int solve(int test){
	long long num; cin >> num;
	long long ans = num;
	
	vector<int> how;
	if(!check(num)){
		int now = num%10;
		long long mult = 1;
		ans -= mult*(now+1);
		num -= now+1;
		num /= 10;
		mult *= 10;
		
		bool breaker = false;
		while(true){
			if(check(ans)) break;
			if(num < 10) breaker = true;
			now = num%10;
			if(now==9){
				num/=10; mult *= 10;
				continue;
			}
			
			ans -= mult*(now+1);
			num -= now+1;
			mult *= 10;
			num /= 10;
			if(breaker) break;
		}
	}
	
	cout << "Case #" << test << ": " << ans << endl;
}

int main(){
	int t; cin >> t;
	for(int i = 1; i <= t; i++) solve(i);
	return 0;
}

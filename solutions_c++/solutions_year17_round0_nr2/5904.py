#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
using namespace std;
bool check(long long num){
	int cur = 9;
	while(num){
		int dig = num % 10;
		if(dig > cur)
			return false;
		cur = dig;
		num /= 10;
	}
	return true;
}
int main(){
	int T;
	cin >> T;
	long long num;
	for(int _=1;_<=T;_++){
		cin >> num;
		printf("Case #%d: ", _);
		long long ans = 0;
		if(check(num))
			cout << num << endl;
		else{
			long long base = 10;
			while(base <= num){
				long long t = ((num / base) - 1 ) * base + base - 1;
				if(check(t) && t > ans && t <= num)
					ans = t;
				base *= 10;
			}
			cout << ans << endl;
		}
	}
	return 0;
}
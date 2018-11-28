#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

long long check(long long num){
	int lD = 10;
	long long dif = 1;
	while(num) {
		int cur = num % 10;
		if (cur > lD)
			return 1;
		lD = cur;
		num /= 10;
		dif *= 10;
	}
	return 0;
}



int main(){
	int T;
	cin>>T;
	int c = 1;
	while(T--){
		long long num;
		cin >> num;
		long long res = num;
		while(true){
			long long s = check(res);
			res -= s;
			if (!s)
				break;
		}
		cout<<"Case #"<<c++<<": "<<res<<endl;
	}
	return 0;
}
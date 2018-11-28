#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

bool isTidy(long long n);

int main(){
	int t = 0;
	scanf("%d", &t);
	int i = 0;
	while(i < t){
		long long n;
		scanf("%lld", &n);
		long long f = 10;
		while(!isTidy(n)){
			long long m = n%f;
			n = n-(m+1);
			f = f*10;
		}
		printf("Case #%d: %lld\n", i+1, n);
		
		i++;
	}

}

bool isTidy(long long n){
	string s = to_string(n);
	int l = s.length();
	int i = 0;
	int last = 0;
	while(i < l){
		int d = s[i] - '0';
		if (d < last) {
			return false;
		}
		last = d;
		i++;
	}
	return true;
}
#include "iostream"
#include "vector"
#include "string"
#include "algorithm"
#include "string.h"
#include "stdio.h"

using namespace std;

int isTidy(long long x) {
	int last = 10;
	while(x) {
		int c=x%10;
		x=x/10;
		if(c>last) return 0;
		last=c;
	}
	return 1;
}

int main() {
	int T;
	cin>>T;
	for(int tc=0;tc<T;tc++) {
		long long x;
		cin>>x;
		while(isTidy(x) == 0) {
			x--;
		}
		cout<<"Case #"<<tc+1<<": "<<x<<endl;
	}
	return 0;
}

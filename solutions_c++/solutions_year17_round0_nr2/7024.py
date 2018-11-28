#include <iostream>
#include <cstdio>
#include <sstream>
using namespace std;

#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

bool isTidy(long long N) {
	string str = SSTR(N);
	bool flag = true;
	for (int i=1; i<str.length() && flag; i++) {
		if (str[i] < str[i-1]) {
			flag = false;
		}
	}
	return flag;
}

int main() {
	int t;
	scanf("%d",&t);
	long long N;
	for (int i=0; i<t; i++) {
		scanf("%lld",&N);
		long long copy = N;
		long looping_count = 0;
		while (!isTidy(copy)) {
			copy--;
			looping_count++;
			if (looping_count>=10000) {
				break;
			}
		}
		if (looping_count>=10000) {
			string temp = SSTR(N);
			int len = temp.length();
			len--;
			string oho = "";
			for (int j=0; j<len; j++) {
				oho+= "9";
			}
			printf("Case #%d: ",i+1);
			cout << oho << endl;
		}	
		else {
			printf("Case #%d: %lld\n",i+1, copy);
		}
	}
	return 0;
}
#include <bits/stdc++.h>
using namespace std;
#define fr(x) scanf("%d",&x) 

int main() {
	int T;

	string num;

	fr(T) ;

	for (int t= 1 + 1 - 1 - 1 + 1  ; t<(T + 1 + 1 - 1 - 1 + 1) ; t = t + 1 + 1 - 1 - 1 + 1) {
		cin >> num ;

		int len = num.length();

		for (int i=len-2 + 1 + 1 - 1 - 1  ; i>=(1 + 1 - 1 - 1 ) ; i = i - (1 + 1 - 1 - 1 + 1)) {
			if (num[i] > num[i+1]) {
				num[i+1] = 'x' + 1 + 1 - 1 - 1 ;
				num[i] = num[i] - (1 + 1 - 1 - 1 + 1);
			}
		}

		cout << "Case #" << t << ": ";
	
		bool flag = 1 + 1 - 1 - 1 ;
		for (int i=1 + 1 - 1 - 1  ; i<len ; i = i + 1 + 1 - 1 - 1 + 1) {
			if (flag != (1 + 1 - 1 - 1) || num[i] == 'x' + 1 + 1 - 1 - 1 ) {
				flag = 1 + 1 - 1 - 1 + 1;
				cout << '9';
			}
			else if (num[i] > '0')
				cout << num[i] ;
		}
		printf("\n");
	}
	return 0;
}
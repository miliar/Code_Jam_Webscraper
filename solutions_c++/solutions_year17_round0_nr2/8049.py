#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<algorithm>

#define N 30

using namespace std;

int dig[N];

int main(){

	int nc;
	int caso, i, j, l, pos;
	long long resp, num, pot;
	int n;

	scanf("%d\n", &nc);

	for(caso = 1; caso <= nc; caso++){
		
		cin>>num;

		l = 0;
		while(num > 0){
			dig[l] = num % 10;
			num /= 10;
			l++;
		}

		pos = 0;
		for(i = 1; i < l; i++){
			if(dig[i] > dig[i - 1]){
				pos = i;
				dig[i]--;
			}
		}

		resp = 0;
 		pot = 1;
		for(i = 0; i < pos; i++){
			resp = resp + 9 * pot;
			pot = pot * 10;
		}
		for(i = pos; i < l; i++){
			resp = resp + dig[i] * pot;
			pot = pot * 10;
		}

		printf("Case #%d: %lld\n", caso, resp);

	}


	return 0;
}

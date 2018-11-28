#include <bits/stdc++.h>

using namespace std;

const int SIZE = 30;

int tc, pos, change, start, carry, v[SIZE];
long long n;
bool ok;

int main(){
	scanf("%d", &tc);
	for(int t = 1; t <= tc; t++){
		memset(v, 0, sizeof v);
		scanf("%lld", &n);
		pos = 0;
		while(n){
			v[pos++] = n % 10;
			n /= 10;
		}
		reverse(v, v + pos);
		carry = pos;
		while(carry){
			ok = true;
			change = -1;
			for(int i = 1; i < pos and ok; i++)
				if( v[i] < v[i - 1] ) change = i - 1, ok = false;
			carry--;
			if( change == -1 ) continue;
			v[change]--;
			for(int i = change + 1; i < pos; i++) v[i] = 9;
		}
		start = 0;
		while( v[start] <= 0 ) start++;
		printf("Case #%d: ", t);
		for(int i = start; i < pos; i++) printf("%d", v[i]); putchar('\n');
	}
	return(0);
}

#include <iostream>
#include <algorithm>
#include <cstring>
#include <stdio.h>
using namespace std;
#define ll long long
typedef pair<ll,ll> pi;
ll t, n, p, arr[105];
ll memo[105][105][105][4];

ll dp(ll x, ll y, ll z, ll cur){
	//number of 1s, number of 2s, number of 3s, current mod
	if (x == 0 && y == 0 && z == 0) return 0;
	if (memo[x][y][z][cur] != -1) return memo[x][y][z][cur];
	ll answer = 0;
	if (cur == 0){
		if (x > 0){
			answer = max(answer, dp(x - 1, y, z, 1));
		}
		if (y > 0){
			answer = max(answer, dp(x, y - 1, z, 2));
		}
		if (z > 0){
			answer = max(answer, dp(x, y, z - 1, 3));
		}
		answer += 1;
		return memo[x][y][z][cur] = answer;
	}
	if (x > 0){
		answer = max(answer, dp(x - 1, y, z, (cur + 1)%4));
	}
	if (y > 0){
		answer = max(answer, dp(x, y - 1, z, (cur + 2)%4));
	}
	if (z > 0){
		answer = max(answer, dp(x, y, z - 1, (cur + 3)%4));
	}
	return memo[x][y][z][cur] = answer;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("alargeout.txt", "w", stdout);
	scanf("%lld", &t);
	for (int i = 0; i < t; i++){
		scanf("%lld%lld", &n, &p);
		for (int j = 0; j < n; j++){
			scanf("%lld", &arr[j]);
		}
		if (p == 2){
			ll zero = 0, one = 0;
			for (int j = 0; j < n; j++){
				if (arr[j] % p == 0) zero++;
				else one++;
			}
			if (one % 2 == 0){
				one /= 2;
			} else {
				one = (one + 1)/2;
			}
			printf("Case #%d: %lld\n", i + 1, zero + one);
			
		} else if (p == 3){
			
			ll zero = 0, one = 0, two = 0;
			for (int j = 0; j < n; j++){
				if (arr[j] % p == 0) zero++;
				else if (arr[j] % p == 1) one++;
				else two++;
			}
			ll z = min(one, two);
			zero += z;
			one -= z;
			two -= z;
			if ((one + two)%3 == 0){
				zero += (one + two)/3;
			} else {
				zero += (one + two)/3;
				zero++;
			}
			printf("Case #%d: %lld\n", i + 1, zero);
			
			
		} else {
			memset(memo, -1, sizeof(memo));
			ll zero = 0, one = 0, two = 0, three = 0;
			for (int j = 0; j < n; j++){
				if (arr[j] % p == 0) zero++;
				else if (arr[j] % p == 1) one++;
				else if (arr[j] % p == 2) two++;
				else three++;
			}
			ll answer = zero + dp(one, two, three, 0);
			printf("Case #%d: %lld\n", i + 1, answer);
			
		}
	}
	
}

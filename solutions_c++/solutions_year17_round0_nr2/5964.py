#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;
const ll MAX_VALUE = 1000000000000000000;
// const ll MAX_VALUE = 100000;

vector<ll> sortedNumber;

void preFunc(ll number) {

	if (number > MAX_VALUE || number < 0) {
		return;
	}

	ll lastNumber = number % 10;
	sortedNumber.push_back(number);

	for (ll i = lastNumber; i < 10; i++) {
		ll currentNumber = number;
		currentNumber = currentNumber * 10LL + i;
		preFunc(currentNumber);
	}


}

int main() {
freopen("input.txt", "r", stdin);
freopen("output.txt", "w+", stdout);
	
	for (ll i = 1; i < 10; i++) {
		preFunc(i);
	}
	sort(sortedNumber.begin(), sortedNumber.end());

	int testCase;
	scanf("%d", &testCase);

	for (int t = 1; t <= testCase; t++) {

		ll N;
		scanf("%lld", &N);

		vector<ll>::iterator it = lower_bound(sortedNumber.begin(), sortedNumber.end(), N);
		if (*it != N) {
			it--;
		}

		printf("Case #%d: ", t);
		
		printf("%lld", *it);
		printf("\n");
	}	

}
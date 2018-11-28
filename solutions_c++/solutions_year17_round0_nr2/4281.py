#include <iostream>
#include <stdint.h>
#include <string>

using namespace std;
bool isTidy(uint64_t K)
{
	uint64_t dec = 10;
	while(dec <= K) {
		uint64_t upper = ((K / dec) % 10);
		uint64_t lower = ((K / (dec/10)) % 10);
		if(upper > lower) {
			return false;
		}
		dec *= 10;
	}
	return true;
}

uint64_t solve(uint64_t K)
{
	uint64_t dec = 10;
	uint64_t ret = K % (dec*10);
	
	while(dec <= K) {
		if(isTidy(ret) == false) {
			if(ret > dec) {
				ret /= dec;
				ret--;
				ret *= dec;
				ret += (dec - 1);
			} else {
				ret = (dec - 1);
			}
		}
		dec*=10;
		ret = (((K / dec) % 10) * dec) + ret;
	}
	return ret;
}

int main(void)
{
	uint64_t N, i;
	cin >> N;

	for(i=0; i<N; i++) {
		uint64_t K;
		cin >> K;
		cout << "Case #" << i + 1 << ": ";
		cout << solve(K) << endl;
	}
}
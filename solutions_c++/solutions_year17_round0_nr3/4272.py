#include <stdio.h>
#include <algorithm>
#include <math.h>

using namespace std;

int main(void)
{
	int test_case = 0;
	FILE * f;
	long long K=0,N=0;
	

	f = fopen("output.txt", "w");

	scanf("%d", &test_case);

	for (int t = 1; t <= test_case; t++) {
		scanf("%lld %lld", &N, &K);
		long long odd_num = 0;
		long long even_num = 0;
		long long odd = 0;
		long long even = 0;
		long long min, max;

		if (N % 2 == 0) {
			even_num++;
			even = N;
		}
		else {
			odd_num++;
			odd = N;
		}

		long long cnt;
		long long sum;
		for (cnt = 1,sum=1; sum< K; cnt++) {
			sum += (long long)pow(2, double(cnt));
		}

		for (int i = 1; i < cnt; i++) {
			long long new_odd = 0;
			long long new_even = 0;
			long long new_odd_num = 0;
			long long new_even_num = 0;
			sum = 0;
			sum += (long long)pow(2, double(cnt-1));

			if (even != 0) {
				//EVEN
				if ((even / 2) % 2 == 0) {
					new_even = even / 2;
					new_odd = even / 2 - 1;
				}
				else {
					new_odd = even / 2;
					new_even = even / 2 - 1;
				}
				new_odd_num = even_num;
				new_even_num = even_num;
			}
			else {
				new_odd_num = 0;
				new_even_num = 0;
			}

			//ODD
			if (odd != 0) {
				if ((odd / 2) % 2 == 0) {
					new_even_num += odd_num * 2;
					new_even = odd / 2;
				}
				else {
					new_odd_num += odd_num * 2;
					new_odd = odd / 2;
				}
			}

			odd_num = new_odd_num;
			even_num = new_even_num;
			odd = new_odd;
			even = new_even;
		}
		if (even > odd) {
			if (even_num > K - sum) {
				max = even / 2;
				min = even / 2 - 1;
			}
			else {
				max = odd / 2;
				min = odd / 2;
			}
		}
		else {
			if (odd_num > K - sum) {
				max = odd / 2;
				min = odd / 2;
			}
			else {
				max = even / 2;
				min = even / 2 - 1;
			}
		}

		fprintf(f,"Case #%d: %lld %lld\n", t,max,min);
	}

	return 0;
}
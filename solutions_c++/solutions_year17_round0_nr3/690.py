#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
using namespace std;

int main(void) {
	long long T, i, maxIndex, found;
	long long N, K, max, countBackup, left, right;
	
	cin >> T;
	for (int t=1; t<=T; t++) {
		printf("Case #%d: ", t);
		cin >> N >> K;
		//printf("%lld %lld", N, K);
		
		vector<long long> number;
		vector<long long> count;
		number.push_back(N);
		count.push_back(1);
		K--;
		
		while (1) {
			//find largest number and its index
			max = number[0];
			maxIndex = 0;
			for (i=1; i<number.size(); i++) {
				if (number[i] > max) {
					max = number[i];
					maxIndex = i;
				}
			}
			//printf("max %lld, count %lld, K %lld\n", max, count[maxIndex], K);
			
			//can we consume all occurrences of this largest number
			if (count[maxIndex] > K) break;
			K -= count[maxIndex];
			countBackup = count[maxIndex];
			
			//depop
			number[maxIndex] = number[number.size()-1];
			number.pop_back();
			count[maxIndex] = count[count.size()-1];
			count.pop_back();
			
			//allocate remaining distance after taking 1 spot for self
			max--;
			left = max / 2;
			right = max - left;
			
			//insert left
			found = 0;
			for (i=0; i<number.size(); i++) {
				if (number[i] == left) {
					found = 1;
					count[i] += countBackup;
					break;
				}
			}
			if (!found) {
				number.push_back(left);
				count.push_back(countBackup);
			}
			
			//insert right
			found = 0;
			for (i=0; i<number.size(); i++) {
				if (number[i] == right) {
					found = 1;
					count[i] += countBackup;
					break;
				}
			}
			if (!found) {
				number.push_back(right);
				count.push_back(countBackup);
			}
		}
		//printf("max %lld", max);
		//allocate remaining distance after taking 1 spot for self
		max--;
		left = max / 2;
		right = max - left;
		printf("%lld %lld", right, left);
		printf("\n");
	}
	
	return 0;
}
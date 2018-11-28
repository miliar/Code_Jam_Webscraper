//#define _CRT_SECURE_NO_WARNINGS
//#include <Windows.h>

#include <map>
#include <string>
#include <stdio.h>
#include <vector>
#include <sstream>
#include <stack>
#include <bitset>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <iostream>
#include <algorithm>
#include <limits.h>
#include <float.h>


using namespace std;



int main(){
	/*freopen("C-large.in", "r", stdin);
	freopen("result", "w", stdout);*/
	int t;
	
	scanf("%d", &t);

	for (int i = 1; i <= t; i++){
		long long n;
		long long k;

		scanf("%lld %lld", &n, &k);

		long long numMin(0), numMax(1);
		long long newMax, newMin;
		while (k > (numMin + numMax)){
			k -= (numMin + numMax);

			if (n % 2 == 0){
				newMax = numMax;
				newMin = 2 * numMin + numMax;
				
			}
			else{
				newMin = numMin;
				newMax = 2 * numMax + numMin;
			}
			n >>= 1;
			numMin = newMin;
			numMax = newMax;
			
		}
		
		if (k > numMax){
			n -= 1;
		}
		printf("Case #%d: %lld %lld\n", i, n / 2, n - n / 2 - 1);
	}
	
}

#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
unsigned long long int ipow(unsigned long long int base, int exp);
int main() {
//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);
	int T, tc;
	unsigned long long int N;
	unsigned long long int tmp;
	int i, j;
	int pivot;
	bool start;
	vector<int> vec;
	scanf("%d", &T);
	for (tc = 1; tc <= T; tc++) {
		//pre=============================================
		start = false;
		vec.clear();
		scanf("%llu", &N);
		for (i = 18;i>=0; i--) {
			tmp = (N / ipow(10, i));
			if (start==false && tmp != 0) {
				vec.push_back(tmp);
				N -= tmp*ipow(10, i);
				start = true;
				continue;
			}else if(start==true && tmp == 0){
				vec.push_back(0);
			}else if(start == true){
				vec.push_back(tmp);
				N -= tmp*ipow(10, i);
			}
		}
		//pre=============================================
		if (vec.size() == 1) {
			printf("Case #%d: %d\n",tc,vec[0]);
		}else {
			for (i = 1; i < vec.size(); i++) {
				if (vec[i-1] <= vec[i])
					continue;
				else {
					for (j = i; j < vec.size(); j++)
						vec[j] = 9;
					vec[i - 1]--;
					for (j = i - 1; j >= 1; j--) {
						if (vec[j - 1] > vec[j]) {
							vec[j - 1]--;
							vec[j] = 9;
						}
						else {
							pivot = j;
							for (int k = pivot + 1; k < vec.size(); k++)
								vec[k] = 9;
							break;
						}
					}
					
				}
			}
			bool outstart=false;
			printf("Case #%d: ", tc);
			for (i = 0; i < vec.size(); i++)
				if (outstart == false && vec[i] != 0) {
					outstart = true;
					printf("%d", vec[i]);
				}else if(outstart == true)
					printf("%d", vec[i]);
			printf("\n");
		}
	}

	return 0;
}
unsigned long long int ipow(unsigned long long int base, int exp)
{
	unsigned long long int result = 1ULL;
	while (exp)
	{
		if (exp & 1)
		{
			result *= base;
		}
		exp >>= 1;
		base *= base;
	}
	return result;
}
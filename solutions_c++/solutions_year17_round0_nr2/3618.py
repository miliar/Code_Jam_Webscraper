#include <cstdio>
#include <utility>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

vi number;

int caseNum = 0;
int main() {
	int t;

	scanf("%d", &t);

	while(t--){
		caseNum++;
		number.clear();
		unsigned long long n;

		scanf("%llu", &n);
		if(n== 0) {
			number.push_back(0);
		} else {
			while(n > 0) {
				number.push_back(n%10);
				n /= 10;
			}
		}

		for(int i = 1; i < number.size(); i++) {
			if(number[i] > number[i-1]) {
				number[i] -= 1;
				if(number[i] == 0 && i == number.size() - 1) {
					number.erase(number.begin() + i);
				}
				for(int j = 0; j < i; j++) {
					number[j] = 9;
				}
			}
		}
		printf("Case #%d: ", caseNum);

		for(int i = number.size() - 1; i >= 0; i--) {
			printf("%d", number[i]);
		}
		printf("\n");
	}
}
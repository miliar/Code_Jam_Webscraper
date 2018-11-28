#include <cstdio>
#include <utility>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

vi pancakes;
int k;

int caseNum = 0;
int main() {
	int t;

	scanf("%d", &t);

	while(t--){
		pancakes.clear();
		caseNum++;

		while(true){
			char c = getchar();
			if(c == ' '){
				break;
			}
			pancakes.push_back(c == '-' ? 0 : 1);
		}

		scanf("%d", &k);

		int flips = 0;
		for(int i = 0; i < pancakes.size() - k + 1; i++) {
			if(pancakes[i] == 0) {
				flips++;
				for(int j = i; j < i + k; j++) {
					pancakes[j] = 1 - pancakes[j];
				}
			}
		}

		bool solved = true;

		for(int i = 0; i < pancakes.size(); i++) {
			if(pancakes[i] == 0) {
				solved = false;
				break;
			}
		}



		printf("Case #%d: ", caseNum);

		if(solved) {
			printf("%d", flips);
		} else {
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}
}
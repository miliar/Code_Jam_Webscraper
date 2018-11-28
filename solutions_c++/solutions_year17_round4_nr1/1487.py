#include <iostream>
#include <sstream>
#include <numeric>
#include <set>
#include <algorithm>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <strings.h>
#include <limits.h>
#include <stdlib.h>
#include <float.h>
#include <strings.h>
#include <string.h>
using namespace std;

int main(){
	int tests;
	cin >> tests;
	for (int t = 0; t < tests; t++){
		int N, P;
		cin >> N >> P;
		int solution = 0;
		int counter = 0, counter1 = 0, counter2 = 0, counter3 = 0;
		for (int i = 0; i < N; i++){
			int g;
			cin >> g;
			if (P == 2){
				if ((g % 2) != 0){
					counter++;
				} else {
					solution++;
				}
			} else if (P == 3){
				if ((g % 3) == 1){
					counter1++;
				} else if ((g % 3) == 2){
					counter2++;
				} else {
					solution++;
				}
			} else if (P == 4){
				if ((g % 4) == 1){
					counter1++;
				} else if ((g % 4) == 2){
					counter2++;
				} else if ((g % 4) == 3){
					counter3++;
				} else {
					solution++;
				}
			}
		}
		if (P == 2){
			solution += (counter + 1) / 2;
		} else if (P == 3){
			int common = min(counter1, counter2);
			solution += common;
			counter1 -= common;
			counter2 -= common;
			if (counter1){
				solution += (counter1 + 2) / 3;
			} else {
				solution += (counter2 + 2) / 3;
			}
		} else if (P == 4){
			int common = min(counter1, counter3);
			solution += common;
			counter1 -= common;
			counter3 -= common;
			
			solution += (counter2) / 2;
			counter2 = (counter2 % 2);
			
			if (counter3){
				if (counter2){
					if (counter3 <= 2){
						solution++;
					} else {
						counter3 -= 2;
						solution++;
						solution += (counter3 + 3) / 4;
					}
				} else {
					solution += (counter3 + 3) / 4;
				}
			} else if (counter1){
				if (counter2){
					if (counter1 <= 2){
						solution++;
					} else {
						counter1 -= 2;
						solution++;
						solution += (counter1 + 3) / 4;
					}
				} else {
					solution += (counter1 + 3) / 4;
				}
			} else if (counter2){
				solution++;
			}
		}
		cout << "Case #" << (t+1) << ": " << solution << endl;
	}
}

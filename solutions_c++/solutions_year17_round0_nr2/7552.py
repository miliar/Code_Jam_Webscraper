#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cctype>
#include <cassert>
#include <numeric>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <bitset>
#include <stack>
#include <list>
#include <set>          
#include <map>
#include <unordered_set>
#include <cstdio>
#include <string>
#include <algorithm>
#include <ctime>
#include <sstream>
#include <climits>
#include <iomanip>

using namespace std;

int t, testnum = 1;
long long n;

long long gaand_lag_gai() {
	vector<int> array;
	long long new_n = n;
	while (new_n > 0) {
		array.push_back(new_n % 10);
		new_n /= 10;
	}
	reverse(array.begin(), array.end());
	int tatti = (int)array.size();
	while (true) {
		bool found = true;
		for (int i = 0; i + 1 < tatti; i++) {
			if (array[i] > array[i + 1]) {
				found = false;
				array[i]--;
				for (int j = i + 1; j < tatti; j++)
					array[j] = 9;

			}
		}
		if (found)	break;
	}
	int index_mine = 0;
	for (int i = 0; i < tatti; i++) if (array[i] != 0) {
		index_mine = i;
		break;
	} 
	long long resu = 0;
	for (int i = index_mine; i < tatti; i++) {
		resu = 10 * resu + array[i];
	}
	return resu;
}

int main(){

    
    scanf("%d", &t);
    while (testnum <= t) {
        scanf("%lld", &n);
        cout << "Case #" << testnum << ": " << gaand_lag_gai() << "\n";
        testnum++;
    }


    return 0;
}
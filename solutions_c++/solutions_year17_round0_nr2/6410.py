#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>

using namespace std;

int main(){
    int T;
	cin >> T;
	for(int i = 1; i <= T; i++){
		long long N;
		cin >> N;
		int a[20];
		long long x = N, d = 0;
		for(int j = 0; x != 0; j++){
			a[j] = x % 10;
			x = x/10;
			d++;
		}
		for(int j = 1; j < d; j++){
			if(a[j] > a[j-1]){
				a[j]--;
				for(int k = 0; k < j; k++)
					a[k] = 9;
			}
		}
		x = 1;
		N = 0;
		for(int j = 0; j < d; j++){
			N += a[j] * x;
			x = x * 10;
		}
		cout << "Case #" << i << ": " << N << endl;
	}
	return 0;
}

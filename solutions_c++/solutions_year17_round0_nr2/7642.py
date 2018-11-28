#include <stdio.h>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <iterator>
#include <utility>
#include <numeric>
using namespace std;
char stop;
const int CN = 1e4 + 10;

deque<int>arr;

void convertToArr(unsigned long long n){
	while (n != 0){
		arr.push_front(n % 10);
		n /= 10;
	}
}



int main(){
	freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
	int t;
	unsigned long long n;

	cin >> t;

	for(int i = 1; i <= t; ++i){
		cin >> n;
		arr.clear();
		convertToArr(n);
		bool counter;

		label:
		counter = 0;
		for (int j = 0; j < arr.size() - 1; ++j){
			if (arr[j] > arr[j+1]){
				counter = 1;
				arr[j]--;
				for (int k = j + 1; k < arr.size(); ++k)
					arr[k] = 9;
			}
		}
		if (counter) goto label;

		bool flag = 0;

		cout << "Case #" << i << ": ";
		for (int j = 0; j < arr.size(); ++j){
			if (arr[j]) flag = 1;
		    if (flag){
				if (j != arr.size()-1)
					cout << arr[j];
				else
					cout << arr[j] << endl;
			}
		}
	}


cin >> stop;
return 0;
}
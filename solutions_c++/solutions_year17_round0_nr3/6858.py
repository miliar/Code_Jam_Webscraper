#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <set>

using namespace std;

int index(set<int> arr);

void main() {
	int t, k, n; //Test cases, people entering, number of stalls

	cin >> t;

	for(int x = 1; x <= t; x++) {
		cin >> n >> k;
		set<int> arr;
		arr.insert(0);
		arr.insert(n + 1);

		int last;

		while(k) {
			arr.insert(last = index(arr));
			k--;
		}
		
		auto curr = arr.begin();
		for(; *curr != last; curr++);

		auto prev = curr;
		auto next = curr;

		advance(prev, -1);
		advance(next, 1);

		int y = max(*curr - *prev - 1, *next - *curr - 1);
		int z = min(*curr - *prev - 1, *next - *curr - 1);
		cout << "Case #" << x << ": " << y << " " << z << endl;
	}
}

//Get index of biggest range
int index(set<int> arr) {
	int m = 0, r = 0;
	auto prev = arr.begin();
	for(auto it = arr.begin(); it != arr.end(); it++) {
		if(*it - *prev > m) {
			m = *it - *prev;
			r = ((*it - *prev) / 2) + *prev;
		}
		prev = it;
	}
	return r;
}



/*
void main() {
int t, k, n; //Test cases, people entering, number of stalls

cin >> t;

for(int x = 1; x <= t; x++) {
cin >> n >> k;
bool *arr = new bool(n);
for(int i = 0; i < n; ++i)
arr[i] = false;

double m = n - 1; //calculating binary search location
while(n) {
m /= 2;
for(double i = m; i < n; i += m)
if(!arr[(int)i]) {
arr[(int)i] = true;
--n;
}
}
int r, t, f1, f2;
for(int i = 0; i < n; ++i) {
if(!arr[i])
++t;
else {
r = max(r, t);
f1 = t == r ? i : f1;
t = 0;
}
}
for(int i = f1 + 1; !arr[i]; ++i)
f2 = i;

cout << "Case #" << x << ": " << r << " " << f2 - f1;
delete arr;
}
}*/

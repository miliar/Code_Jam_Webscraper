#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <stdlib.h>
#include <string.h>
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <ctype.h>
#include <math.h>
#define FOR(x,y,z) for(int x = (y); x < (z); x++)
#define FORD(x,y,z) for(int x = (y); x >= z; x--)
#define REP(r,n) for(int r = 0; r < (n); r++)
#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define MAXUS 100001
#define MAXUS2 9000005
#define PI 3.1415926
#define SIZE(c) ((int)((c).size()))
#define FOREACH(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); i++)
#define ALL(u) (u).begin(),(u).end()
#define epsilon 0.000001
using namespace std;

typedef long long LL;
typedef long double LD;
typedef vector<int> VI;
typedef pair<int, int> PR;
LL global_top_number = 0;

LL getMaximalPossible(LL base) {
	LL sum = 1;
	const LL base_2 = 2;
	LL top_number = 1;
	while (sum + top_number*base_2 < base) {
		sum += top_number*base_2;
		top_number *= base_2;
	}
	global_top_number = top_number * base_2;
	return sum;
}

int main() {
	LL N, K, T;	
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N >> K;
		if (K == N) {
			cout << "Case #" << t << ": 0 0" << endl;
			continue;
		}
		if (K == 1) {
			cout << "Case #" << t << ": " <<  (N-1) / 2 + (N-1) % 2 << " " << (N-1) / 2 << endl;
			continue;
		}
	

		LL max_possible = getMaximalPossible(K);
		LL empty_stalls = N - max_possible;
		LL smallest_size_of_single_hole = empty_stalls / global_top_number;
//		cout << global_top_number << endl;
//		cout << max_possible << endl;
//		cout << empty_stalls << endl;
//		cout << smallest_size_of_single_hole << endl;

		LL count_of_one_bigger_than_smallest = empty_stalls % global_top_number;
		K -= max_possible;
		K -= count_of_one_bigger_than_smallest;
		LL size_of_choosed_one = smallest_size_of_single_hole;
		LL result1;
		LL result2;
		if (K <= 0) {
			size_of_choosed_one += 1;
		}
		result1 = (size_of_choosed_one-1)/2 + (size_of_choosed_one-1)%2;
		result2 = (size_of_choosed_one-1)/2;
		cout << "Case #" << t << ": " << result1 << " " << result2 << endl;
	}
	return 0;
}

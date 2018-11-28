#include <stdio.h>
#include <iostream>
#include <set>
using namespace std;

void solve(int case_num, unsigned long long num_stalls, unsigned long long num_people);

int main()
{
	int T;
	unsigned long long num_stalls, num_people;
	int casenum;


	scanf("%d", &T);

	for (casenum = 1; casenum <= T; casenum++) {
		scanf("%llu", &num_stalls);
		scanf("%llu", &num_people);

		solve(casenum, num_stalls, num_people);
	}

	return 0;
}

void solve(int case_num, unsigned long long num_stalls, unsigned long long num_people)
{
	unsigned long long left;
	unsigned long long right;
	unsigned long long val;

	multiset<unsigned long long> ms;
	multiset<unsigned long long>::iterator iter;

	ms.insert(num_stalls);
	while (num_people-- > 0) {
		iter = ms.end();
		--iter;
		val = *iter;
		val -=1;
		left = val / 2;
		right = val - left;
		ms.erase(iter);
		ms.insert(left);
		ms.insert(right);
	}

	printf("Case #%d: %llu %llu\n", case_num, right, left);
}

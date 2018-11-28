#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <utility>
#include <algorithm>

void solve(int caseNo)
{
	int N, K;
	scanf("%d %d", &N, &K);

	std::multiset<int, std::greater<int> > s;
	s.insert(N);
	int ls, rs;

	for (int i = 0; i < K; i++){
		int e = *(s.begin());
		s.erase(s.begin());

		if ((e%2) == 1){
			ls = e/2;
			rs = e/2;
		}
		else{
			ls = (e/2)-1;
			rs = e/2;
		}
		s.insert(ls);
		s.insert(rs);
		//std::cout << "e = " << e << " ls = " << ls << " rs = " << rs << std::endl;
	}

	if (caseNo != 1)
		printf("\n");
	printf("Case #%d: %d %d", caseNo, std::max(ls, rs), std::min(ls, rs));
}

/*void solve(int caseNo)
{
	int N, K;
	scanf("%d %d", &N, &K);

	std::vector<int> el, er;
	//Init el and er
	int ls, rs;

	for (int i = 0; i < K; i++){
		//find the best j location
		if ((e%2) == 1){
			ls = e/2;
			rs = e/2;
		}
		else{
			ls = (e/2)-1;
			rs = e/2;
		}
		s.insert(ls);
		s.insert(rs);
		//std::cout << "e = " << e << " ls = " << ls << " rs = " << rs << std::endl;
	}

	if (caseNo != 1)
		printf("\n");
	printf("Case #%d: %d %d", caseNo, std::max(ls, rs), std::min(ls, rs));
}*/

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}

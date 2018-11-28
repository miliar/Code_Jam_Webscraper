#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

bool IsValidServing(int p, int s, int number)
{
	double minSize = s*number*0.9;
	double maxSize = s*number*1.1;

	if (p >= minSize and p <= maxSize)
		return true;
	return false;
}

void solve(int caseNo)
{
	if (caseNo != 1)
		printf("\n");
	int N, P;

	std::cin >> N >> P;
	std::vector<int> S;
	for (int i = 0; i < N; i++){
		int a;
		std::cin >> a;
		S.push_back(a);
	}

	std::vector<std::multiset<int> > Q;
	for (int i = 0; i != N; i++){
		std::multiset<int> qi;
		for (int j = 0; j != P; j++){
			int a;
			std::cin >> a;
			qi.insert(a);
		}
		Q.push_back(qi);
	}

	int count = 0;

	std::vector<std::multiset<int>::iterator > toBeErased;

	while(Q[0].size())
	{
		int elem = *(Q[0].begin());
		Q[0].erase(Q[0].begin());

		int noOfServings = (int)std::ceil(elem/(S[0]*1.1));
		toBeErased.clear();
		bool flag = false;

		while (!flag and IsValidServing(elem, S[0], noOfServings))
		{
			//std::cout << "NoOfServing=" << noOfServings << std::endl;
			toBeErased.clear();
			for (size_t i = 1; i != Q.size(); i++)
			{
				std::multiset<int>::iterator it = Q[i].begin(), end = Q[i].end();
				bool found = false;
				for (; it != end; it++)
				{
					if (IsValidServing(*it, S[i], noOfServings))
					{
						//std::cout << "Found for " << i << std::endl;
						toBeErased.push_back(it);
						found = true;
						break;
					}
				}
				
				if (!found)
				{
					toBeErased.clear();
					break;
				}
			}

			if (toBeErased.size() == size_t(N-1)){
				count++;
				for (size_t k = 1; k != Q.size(); k++){
					Q[k].erase(toBeErased[k-1]);
				}
				flag = true;
			}
			noOfServings++;
		}

		/*noOfServings++;

		if (IsValidServing(elem, S[0], noOfServings))
		{
			//std::cout << "NoOfServing=" << noOfServings << std::endl;
			toBeErased.clear();
			for (size_t i = 1; i != Q.size(); i++)
			{
				std::multiset<int>::iterator it = Q[i].begin(), end = Q[i].end();
				bool found = false;
				for (; it != end; it++)
				{
					if (IsValidServing(*it, S[i], noOfServings))
					{
						std::cout << "Found for " << i << std::endl;
						toBeErased.push_back(it);
						found = true;
						break;
					}
				}
				
				if (!found)
				{
					toBeErased.clear();
					break;
				}
			}

			if (toBeErased.size() == size_t(N-1)){
				count++;
				for (size_t k = 1; k != Q.size(); k++){
					Q[k].erase(toBeErased[k-1]);
				}
				continue;
			}
		}*/
	}


	printf("Case #%d: %d", caseNo, count);
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}

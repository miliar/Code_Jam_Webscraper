#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>
#include <queue>
#include <map>

#define LLI unsigned long long int
#define LEAF 1
#define NODE 0

using namespace std;

class chunk{
	public:
	int size;
	int amount;

	chunk() : size(0), amount(0) {}
	chunk(int a, int b) : size(a), amount(b) {}
	bool operator<(const chunk& in) const {
		if(size < in.size)
			return true;
		return false;
	}
	bool operator>(const chunk& in) const {
		if(size > in.size)
			return true;
		return false;
	}
};


int main()
{
	ios_base::sync_with_stdio();
	int T;
	cin >> T;

	for(int aa=0;aa<T;++aa)
	{
		map<LLI, LLI> Map;
		LLI N, K;
		cin >> N;
		cin >> K;
		Map[N] = 1;
		LLI remain = K;
		LLI max, min;
		LLI smaller, larger;
		map<LLI, LLI>::iterator mit;
		while(remain > 0)
		{
			mit = Map.end();
			--mit;
			smaller = (mit->first-1)/2;
			larger = (mit->first-1)-smaller;
			if(mit->second < remain)
			{
				remain -= mit->second;
				if(Map.count(smaller) == 0)
					Map[smaller] = 0;
				if(Map.count(larger) == 0)
					Map[larger] = 0;
				Map[smaller] += mit->second;
				Map[larger] += mit->second;
				Map.erase(mit->first);
			}
			else
			{
				min = smaller;
				max = larger;
				break;
			}
		}
		
		cout << "Case #" << aa+1 << ": ";
		cout << max << " " << min;
		cout << endl;
	}
	
	return 0;
}


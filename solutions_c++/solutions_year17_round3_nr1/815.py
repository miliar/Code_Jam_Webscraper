#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <algorithm>
#define PI 3.1415926535897932384

using namespace std;
typedef long long int lli;

class pancake{
	public:
	double first, second;
	int index;
};

struct c{
	bool operator() (const pancake& a, const pancake& b)
	{
		if(2.0*a.first*PI*a.second > 2.0*b.first*PI*b.second)
			return true;
		else if(2.0*a.first*PI*a.second == 2.0*b.first*PI*b.second)
		{
			if(a.first > b.first)
				return true;
			else if(a.first == b.first)
				return (a.index < b.index);
			return false;
		}
		return false;
	}
}compare;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	
	int T, N, K, a, b;
	cin >> T;
	for(int aa=1;aa<=T;++aa)
	{
		cin >> N >> K;
		vector<pancake> pancakes(N);
		for(int i=0;i<N;++i)
		{
			cin >> a >> b;
			pancakes[i].first = a;
			pancakes[i].second = b;
			pancakes[i].index = i;
		}
		sort(pancakes.begin(), pancakes.end(), compare);
		double maxx = 0;
		for(int i=0;i<pancakes.size();++i)
		{
			//cerr << pancakes[i].first << ": " << endl;
			double amt = 0;
			int foundI = 0;
			double maxR = pancakes[i].first;
			for(int j=0;j-foundI < K-1;++j)
			{
				if(j == i)
					foundI = 1;
				else
				{
					if(pancakes[j].first > maxR)
						maxR = pancakes[j].first;
					amt += 2.0*PI*pancakes[j].first*pancakes[j].second;
				}
			}
			amt += maxR*maxR*PI;
			amt += pancakes[i].first*pancakes[i].second*PI*2;
			//cerr << "  " << amt << endl;
			if(amt > maxx)
				maxx = amt;
		}
		
		cout << "Case #" << aa << ": " << fixed << setprecision(8) << maxx << endl;
	}
	
	return 0;
}

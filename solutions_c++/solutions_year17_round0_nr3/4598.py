#include <iostream>
#include <cstdlib>
#include <map>
#include <vector>
#include <queue>
#include <sstream>

using namespace std;


class CompareInterval
{
public:
    bool operator()(pair<unsigned long long, unsigned long long> &n1, pair<unsigned long long, unsigned long long> &n2)
    {
		//  return (lenght of second interval) - (length of first interval)
		return (n2.second - n2.first + 1) > (n1.second - n1.first + 1);
		
		
		//return (n2.second+1 - n2.first) > (n1.second+1 - n1.first);
		
	}
};



int main()
{
	std::ios::sync_with_stdio(false);
	
	unsigned int T;
	cin >> T;
	
	
	
	for (unsigned int i = 0; i < T; ++i)
	{
		unsigned long long N, K;
		cin >> N >> K;
		
		
		priority_queue<pair<unsigned long long, unsigned long long>, vector<pair<unsigned long long, unsigned long long> >, CompareInterval> Q;
		Q.push(make_pair(0, N-1));
		
		
		unsigned long long LS, RS;
		
		
		bool empty = false;
		
		
		//while (!Q.empty())
		while(K--)
		{
			//  Pop largest interval in the queue
			unsigned long long startIndex = Q.top().first;
			unsigned long long endIndex = Q.top().second;
			Q.pop();
			
			if (startIndex == endIndex)
			{
				//  If we pop this interval, there is not a larger one
				cout << "Case #" << i+1 << ": 0 0" << endl;
				empty = true;
				K = 0;
				continue;
			}
			else
			{
				//  If odd length, sit to bottom, else sift to leftmid
				unsigned long long intervalLength = endIndex - startIndex;
				unsigned long long midPosition = startIndex + intervalLength/2;
				
				//  Add left interval to the queue
				Q.push(make_pair(startIndex, midPosition-1));
				
				//  Add right interval to the queue
				Q.push(make_pair(midPosition+1, endIndex));
				
				
				LS = midPosition - startIndex;
				RS = endIndex - midPosition;
			}
		}
		
		if (empty)
		{
			
		}
		else
		{
			unsigned long long maxS = (LS > RS) ? (LS) : (RS);
			unsigned long long minS = (LS < RS) ? (LS) : (RS);
			cout << "Case #" << i+1 << ": " << maxS << " " << minS << endl;
		}
		
	}
	
	
	return 0;
}

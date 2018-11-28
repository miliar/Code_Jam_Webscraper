#include<iostream>
#include<queue>
#include<vector>
#include<tuple>
using namespace std;

class compare{
public:
	bool operator()(pair<int, int>& a, pair<int, int>& b)
	{
		return a.first < b.first || a.first == b.first && a.second > b.second; 
	}
};

pair<int, int> solution(int n, int k)
{
	if(k / (float) n > 0.6)
		return pair<int, int>{0, 0};

	priority_queue<pair<int, int>, vector<pair<int, int>>, compare> heap;
	heap.emplace(n, 0);
	int len, idx;
	while(k-- > 1)
	{
		tie(len, idx) = heap.top();
		heap.pop();	
		if(len / 2 > 0)
		{
			heap.emplace(len / 2, idx + (len - 1) / 2);
			if((len - 1) / 2 > 0)
				heap.emplace((len - 1) / 2, idx);
		}	
	}
	tie(len, idx) = heap.top();
	return pair<int, int> {len / 2, (len - 1) / 2};
	
}

int main()
{
	int t, n, k;
	cin >> t;
	int l1, l2;
	for(int i = 1; i <= t; i++)
	{
		cin >> n >> k;
		tie(l1, l2) = solution(n, k);
		cout << "Case #" << i <<": "<< l1 << " " << l2 << endl;
	
	}
	return 0;
}

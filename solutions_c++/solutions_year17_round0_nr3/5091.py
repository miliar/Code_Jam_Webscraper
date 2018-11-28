#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct MaxHeapNode
{
    int startIndex;
    int endIndex;
    bool operator< (const MaxHeapNode& rhs) const
    {
        if(endIndex - startIndex < rhs.endIndex - rhs.startIndex)
            return true;
        else if(endIndex - startIndex == rhs.endIndex - rhs.startIndex)
            return startIndex > rhs.startIndex;
        return false;
    }
};

int main()
{
    int T;

    cin >> T;
    for(int t=1; t <= T; ++t)
    {
        int N, K;
        cin >> N >> K;
        MaxHeapNode node;
        priority_queue<MaxHeapNode> pq;

        node.startIndex = 1;
        node.endIndex = N;
        pq.push(node);

        int minDist, maxDist;
        for(int i=0; i < K; ++i)
        {
            node = pq.top();
            pq.pop();
            int placementIndex = (node.endIndex + node.startIndex) / 2;
            int p = node.startIndex, r = node.endIndex;
            minDist = min(placementIndex - p, r - placementIndex);
            maxDist = max(placementIndex - p, r - placementIndex);
            node.endIndex = placementIndex - 1;
            pq.push(node);
            node.startIndex = placementIndex + 1;
            node.endIndex = r;
            pq.push(node);
        }

        cout << "Case #" << t << ": " << maxDist << " " << minDist << endl;
    }

    return 0;
}

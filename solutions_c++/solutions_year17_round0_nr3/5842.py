#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
class Node
{
    public:
        int minDiff, maxDiff, ind;
        int st, end;
        int pos;
        Node(int st, int end)
        {
            this->st = st;
            this->end = end;
            int gap = (end - st) + 1;
            if(gap % 2)
            {
                minDiff = maxDiff = gap/2;
            }
            else
            {
                maxDiff = gap/2;
                minDiff = maxDiff - 1;
            }
            this->pos = end - (gap/2);
        }
};
class comp
{
    public:
    bool operator() (Node a, Node b) const
    {
        if(a.minDiff != b.minDiff)
        {
            return a.minDiff < b.minDiff;
        }
        else if(a.maxDiff != b.maxDiff)
        {
            return a.maxDiff < b.maxDiff;
        }
        else
        {
            return a.pos > b.pos;
        }
    }
};
pair<int, int> bfs(int n, int k)
{
    typedef priority_queue< Node , vector<Node>, comp> mypq_type;
    mypq_type q;
    int ind = 0;
    q.push(Node(1, n));
    while(!q.empty())
    {
        Node curr = q.top();
        curr.ind = ++ind;
        q.pop();
        if(curr.ind == k)
        {
            return make_pair(curr.maxDiff, curr.minDiff);
        }
        else
        {
            if(curr.maxDiff != 0)
            {
                if(curr.maxDiff > curr.minDiff)
                {
                    q.push(Node(curr.pos + 1, curr.end));
                    if(curr.st != curr.pos)
                        q.push(Node(curr.st, curr.pos - 1));
                }
                else
                {
                    if(curr.st != curr.pos)
                        q.push(Node(curr.st, curr.pos - 1));
                    q.push(Node(curr.pos + 1, curr.end));
                }
            }
        }
    }
    return make_pair(-1, -1);
}
int main()
{
    int t = 0;
    cin >> t;
    for(int c = 1; c < (t + 1); c++)
    {
        int n = 0, k = 0;
        cin >> n >> k;
        pair<int, int> res = bfs(n, k);
        cout << "Case #" << c << ": " << res.first << " " << res.second << endl;
    }
    return 0;
}

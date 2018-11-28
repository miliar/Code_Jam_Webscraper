#include <bits/stdc++.h>

using namespace std;

struct slot
{
    int leftMost, rightMost, index;
    int leftBet, rightBet;

};
struct comp
{
    bool operator()(const slot& a, const slot& b)
    {
        if(min(a.leftBet, a.rightBet) != min(b.leftBet, b.rightBet))
        {
            return min(a.leftBet, a.rightBet) < min(b.leftBet, b.rightBet);
        }
        else if(max(a.leftBet, a.rightBet) != max(b.leftBet, b.rightBet))
        {
            return max(a.leftBet, a.rightBet) < max(b.leftBet, b.rightBet);
        }
        else
        {
            return a.index < b.index;
        }

    }
};
int main()
{
    int t; cin >> t;
    for(int testCase = 1; testCase <= t; testCase++)
    {
        int n; cin >> n; int k; cin >> k;
        priority_queue<slot, vector<slot>, comp> pq;

        slot temp;
        temp.leftMost = -1;
        temp.rightMost = n;
        temp.index = (temp.leftMost + temp.rightMost)/2;;
        temp.leftBet = temp.index;
        temp.rightBet = temp.rightMost - temp.index -1;

        pq.push(temp);


        for(int i = 0; i < k-1; i++)
        {
            slot cur = pq.top();
           // cout << cur.index << endl;
            pq.pop();
            if(cur.index != cur.leftMost+1)
            {
                slot t1;
                t1.leftMost = cur.leftMost;
                t1.rightMost = cur.index;
                t1.index = (t1.leftMost + t1.rightMost)/2;
                t1.leftBet = (t1.index - t1.leftMost)-1;
                t1.rightBet = (t1.rightMost -t1.index)-1;
                pq.push(t1);
            }
            if(cur.index + 1 != cur.rightMost)
            {
                slot t1;
                t1.leftMost = cur.index;
                t1.rightMost = cur.rightMost;
                t1.index = (t1.leftMost + t1.rightMost)/2;
                t1.leftBet = (t1.index - t1.leftMost)-1;
                t1.rightBet = (t1.rightMost -t1.index)-1;
                pq.push(t1);
            }
        }

        slot ans = pq.top();
        cout <<"Case #" << testCase <<": "<< max(ans.leftBet, ans.rightBet) << " " <<min(ans.leftBet, ans.rightBet) << endl;
    }
    return 0;
}



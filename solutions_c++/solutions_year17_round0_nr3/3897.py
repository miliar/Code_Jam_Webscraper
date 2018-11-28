#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin >> t;
    for(int T = 1; T <= t; T++)
    {
        int n, k;
        cin >> n >> k;
        priority_queue<int> q;
        q.push(n);
        int l1 = 0, l2 = 0;
        while(k--)
        {
            int c = q.top();
            q.pop();
            if(c & 1)
            {
                c = c / 2;
                q.push(c);
                q.push(c);
                l1 = l2 = c;
            }
            else
            {
                c = c / 2;
                q.push(c);
                q.push(c - 1);
                l1 = c;
                l2 = c - 1;
            }
        }
        cout << "Case #" << T << ": ";
        cout << max(l1, l2) << " " << min(l1, l2) << endl;
    }
}

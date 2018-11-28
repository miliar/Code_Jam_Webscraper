#include<iostream>
#include<cstdio>
#include<queue>
using namespace std;

int main()
{
    freopen("C-small-2-attempt0.in.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    std::priority_queue<int> q;
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cout << "Case #" << t << ": ";
        int n, k;
        cin >> n >> k;
        while(!q.empty())
            q.pop();
        q.push(n);
        int ans1, ans2;
        for (int i = 1; i <= k; i++)
        {
            int w = q.top();
            q.pop();
            ans2 = (w - 1) / 2;
            ans1 = (w - 1) - ans2;
            q.push(ans1);
            q.push(ans2);
        }
        cout << ans1 << " " << ans2 << endl;
    }
    return 0;
}

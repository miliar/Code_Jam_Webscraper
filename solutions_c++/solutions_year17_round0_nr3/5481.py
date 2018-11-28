#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int t;
    int n;
    int k;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        priority_queue<int> q;

        cin >> n >> k;
        cout << "Case #" << i << ": ";

        q.push(n);
        for(int i = 0; i < k-1; i++)
        {
            int buff = q.top();
            q.pop();
            int max = (buff-1)/2 + (buff-1)%2;
            int min = (buff-1)/2;
            q.push(max);
            q.push(min);
        }
        int buff = q.top();
        q.pop();
        cout << (buff-1)/2 + (buff-1)%2 << " " << (buff-1)/2 << endl;
    }

    return 0;
}


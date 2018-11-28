#include <bits/stdc++.h>

using namespace std;


int main()
{
    int T, N, K;

    cin >> T;
    for (int i = 1; i <= T; i++) {
        cout << "Case #" << i << ": ";
        cin >> N >> K;
        
        priority_queue<int> Q;

        Q.push(N);

        while (--K)
        {
            Q.push(Q.top()/2);
            Q.push(Q.top()/2 - !(Q.top() % 2));
            Q.pop();
        }
        //cout << Q.top() << endl;
        cout << Q.top()/2 << " " << Q.top()/2 - !(Q.top()%2) << endl;        
    }

    return 0;
}
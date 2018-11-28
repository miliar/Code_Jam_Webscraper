#include <iostream>
#include <stdio.h>
#include <queue>

using namespace std;

int main()
{
    freopen("C-small-2-attempt0.in", "r", stdin);
    freopen("C-small-2-attempt0.out", "w", stdout);
    int t, i, n, k, j, queueFront;
    cin>>t;
    for(i=1; i<=t; i++)
    {
        priority_queue<int> myQueue;
        cin>>n>>k;
        myQueue.push(n);
        for(j=0; j<k; j++)
        {
            queueFront = myQueue.top();
            myQueue.pop();
            myQueue.push(queueFront/2);
            myQueue.push((queueFront-1)/2);
        }
        cout<<"Case #"<<i<<": "<<queueFront/2<<" "<<(queueFront-1)/2<<endl;
    }
    return 0;
}

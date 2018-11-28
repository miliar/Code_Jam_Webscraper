#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("bstalls.out", "w", stdout);
    priority_queue<int>pq;
    int t;
    scanf("%d",&t);
    for(int tc = 1; tc <= t; tc++){

    int n, k;
    cin >> n >> k;
    pq.push(n);
    while(k-- > 1)
    {
        int tp = pq.top();
        pq.pop();
        tp--;
        pq.push(tp/2);
        pq.push(tp - tp/2);
    }
    int tp = pq.top();
    tp--;
    printf("Case #%d: %d %d\n",tc,(tp&1? tp/2+1: tp/2), tp/2);

    while(!pq.empty()) pq.pop();
    }

}

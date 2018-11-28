#include <iostream>
#include <queue>
#include <bits/stdc++.h>
using namespace std;

int main(){
    freopen("F:\\Kavish\\Google Code Jam\\a.txt", "r", stdin);
	freopen("F:\\Kavish\\Google Code Jam\\b.txt", "w", stdout);
    int T;
    cin >> T;
    for(int i=1;i<=T;i++)
    {
        int n,k;
        cin >> n >> k;
        priority_queue<int> pq;
        pq.push(n);
        int l,r;
        while(k>=1)
        {
            int t = pq.top();
            pq.pop();
            l = t/2;
            r = t-t/2-1;
            pq.push(l);
            pq.push(r);
            k--;
        }

        cout << "Case #" << i << ": ";
        cout << l << " " << r << endl;
    }
    return 0;
}

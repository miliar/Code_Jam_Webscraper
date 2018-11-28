#include<bits/stdc++.h>

using namespace std;

int main() {
    freopen("C-small-2-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin>>t;

    for(int test=1; test<=t; test++) {
        int n, k;
        cin>>n>>k;

        priority_queue<int> pq;
        pq.push(n);
        for(int i=1; i<k; i++) {
            int e = pq.top();
            pq.pop();
            e = e-1;
            int e1=e/2, e2=e/2+e%2;
            if(e1!=0)
                pq.push(e1);
            if(e2!=0)
                pq.push(e2);
        }

        int r = pq.top();
        r = r-1;
        cout<<"Case #"<<test<<": "<<r/2+r%2<<" "<<r/2<<endl;
    }

    return 0;
}

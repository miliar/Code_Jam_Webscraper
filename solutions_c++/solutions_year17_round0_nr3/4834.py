#include <bits/stdc++.h>

using namespace std;

int t,i,now,k,n;
priority_queue < int > q;

int main() {
    freopen("C-small-2-attempt3.in","r",stdin);
    freopen("Csmall2.out","w",stdout);
    cin>>t;
    for (int t1=1;t1<=t;t1++) {
        cin>>n>>k;
        cout<<"Case #"<<t1<<": ";
        if (8*k/5 > n) { cout<<0<<" "<<0<<endl; continue; }
        n+=2;
        while (q.size() > 0) q.pop();
        q.push(n);
        for (i=0;i<k;i++) {
            now=q.top();
            q.pop();
            q.push((now+1)/2);
            q.push(now-(now+1)/2+1);
        }
        cout<<now/2-1<<" "<<(now-1)/2-1<<endl;
    }
}

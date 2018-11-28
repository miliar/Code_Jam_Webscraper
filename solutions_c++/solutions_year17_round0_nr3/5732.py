#include <bits/stdc++.h>
using namespace std;

int solve() {
    int n,k;
    cin >> n >> k;
    
    priority_queue<int> pq;
    
    pq.push(n);
    for (int i=0;i<k-1;++i){
        int top = pq.top();
        pq.pop();
        int l = top/2;
        int r = top - l;
        if (l==r) l--;
        else r--;
        pq.push(l);
        pq.push(r);
//        cout << "FAK " << top << endl;
    }
    
    
    int tmp = pq.top();
    int left = tmp/2;
    int right = tmp-left;
    if (left==right) left--;
    else right--;
//    cout << "INI " << tmp << endl;
    cout << max(left,right) << " " << min(left,right) << endl;
}

int main() {
    int ntest;
    scanf("%d",&ntest);
    for (int test=1;test<=ntest;++test){
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}

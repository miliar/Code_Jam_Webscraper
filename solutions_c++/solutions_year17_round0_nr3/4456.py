#include <bits/stdc++.h>
using namespace std;
int main(){
    ios::sync_with_stdio(0);
    
    int t,tc=0;
    cin >> t;
    while(t--){
        long long n,k,a,i;
        cin >> n >> k;
        priority_queue<int>q;
        cout << "Case #" << ++tc << ": ";
        q.push(n);
        for(i=0;i<k-1;++i){
            a=q.top(); q.pop();
            if(a&1){
                q.push(a/2);
                q.push(a/2);
            }else{
                q.push(a/2);
                q.push(a/2-1);
            }
        }
        a=q.top();
        if(a&1)
            cout << a/2 << ' ' << a/2 << '\n';
        else
            cout << a/2 << ' ' << a/2-1 << '\n';
    }
    return 0;
}
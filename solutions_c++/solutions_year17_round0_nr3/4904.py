#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int p=1;p<=t;p++){
        int n,k;
        cin >> n >> k;
        priority_queue<int> Q;
        Q.push(n);
        int a,b;
        while(k>0){
            int val=Q.top();
            Q.pop();
            if(val%2==0){
                a=val/2;
                b=a-1;
            }
            else{
                a=val/2;
                b=a;
            }
            if(a>0){
                Q.push(a);
            }
            if(b>0){
                Q.push(b);
            }
            k--;
        }
        cout << "Case #" << p << ": " << a << " " << b << endl;
    }
    // your code goes here
    return 0;
}

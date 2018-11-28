#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    freopen("C-small-2-attempt0.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,test=1;
    cin >> t;
    while(t--){
        int n,k;
        cin >> n >> k;
        priority_queue <int> parts;
        parts.push(n);
        int a,b;
        while(k--){
            int top = parts.top();
            if(top%2 == 0){
                a = top/2;
                b = top/2-1;
                parts.push(a);
                parts.push(b);

            }else{
                a = (top-1)/2;
                b = (top-1)/2;
                parts.push(a);
                parts.push(b);
            }
            parts.pop();
        }
        cout << "Case #" << test << ": ";
        cout << max(a,b) << " " << min(a,b) << endl;
        test++;
    }
    return 0;
}

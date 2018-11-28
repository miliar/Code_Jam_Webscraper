#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    cin >> t;
    int test = 1;
    while(test <= t) {
        priority_queue<int>q;
        int n,k;
        cin >> n >> k;
        q.push(n);
        for(int i=0;i<k-1;i++) {
            int t_ele = q.top();
            q.pop();
            if(t_ele % 2 == 0)  {
                q.push(t_ele/2);
                q.push(t_ele/2-1);
            }
            else {
                q.push(t_ele/2);
                q.push(t_ele/2);
            }
        }
        int ans=q.top();
        int ans1,ans2;
        if(ans % 2 != 0) {
            ans1 = ans/2;
            ans2 = ans/2;
        }
        else {
            ans1 = ans/2;
            ans2 = ans/2-1;
        }
        cout << "Case #" << test << ": " << ans1 << " " << ans2  << endl;
        test++;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


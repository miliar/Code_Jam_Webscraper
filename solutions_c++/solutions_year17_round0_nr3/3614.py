#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;
priority_queue <long long> q;
int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int cas=1;cas<=t;cas++) {
        long long n,k;
        cin>>n>>k;
        while (!q.empty()) q.pop();
        q.push(n);
        while (k>1) {
            long long now=q.top();
            if (now<=1) break;
            q.pop();
            if (now%2) {
                q.push(now/2);
                q.push(now/2);
            } else {
                q.push(now/2-1);
                q.push(now/2);
            }
            k--;
        }
        printf("Case #%d: ",cas);
        long long now=q.top();
        if (now<=1) cout<<"0 0"<<endl;
        else {
            if (now%2) cout<<now/2<<" "<<now/2<<endl;
            else cout<<now/2<<" "<<now/2-1<<endl;
        }
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}

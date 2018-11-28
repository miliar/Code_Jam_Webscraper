#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int main()
{
    freopen("data.out","w",stdout);
    int T,n,k;
    scanf("%d",&T);
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%d%d",&n,&k);
        priority_queue<int> q;
        q.push(n);
        int sl,sr;
        for(int i=1;i<=k;i++){
            int x=q.top();q.pop();
            if(x&1){
                sl=sr=x/2;
            }
            else{
                sl=x/2;
                sr=x/2-1;
            }
            if(sl)
            q.push(sl);
            if(sr)
            q.push(sr);
        }
        printf("Case #%d: %d %d\n",kase,max(sl,sr),min(sl,sr));
    }
    return 0;
}

#include<bits/stdc++.h>
#include<queue>
int n,k,x,y,ans;
using namespace std;
int main(){
    freopen("C.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
        scanf("%d%d",&n,&k);
        priority_queue<pair<int,int> > Q;
        Q.push(make_pair(n,1));
        while (k){
            x=Q.top().first;
            y=Q.top().second;
         //   cout<<x<<" "<<y<<endl;
            k-=y;
            if (k<=0) {
                ans=x;
                break;
            }
            Q.pop();
            Q.push(make_pair((x-1)/2,y));
            Q.push(make_pair(x/2,y));
        }
        while (!Q.empty()) Q.pop();
        printf("Case #%d: %d %d\n",cas,(ans)/2,(ans-1)/2);
    }
    return 0;
}

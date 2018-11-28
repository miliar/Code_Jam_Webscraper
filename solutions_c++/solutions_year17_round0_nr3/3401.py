#include <bits/stdc++.h>

using namespace std;
int n,k;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1;i<=t;i++) {
        if(i != 1)
            printf("\n");

        scanf("%d %d",&n,&k);
        priority_queue <pair<int,pair<int,int> > >pq;
//        cout<<pq.size()<<endl;
        pq.push(make_pair(n,make_pair(0,1-n )));

        for(int j = 0;j<k;j++) {
            pair<int,pair<int,int> > p = pq.top();
            pq.pop();
            p.second.first *= -1;
            p.second.second *= -1;
            int mid = (p.second.second+p.second.first) /2;
//            cout<<p.first<<" "<<p.second.first<<" "<<p.second.second<<" "<<mid<<endl;
            if(mid-p.second.first)
                pq.push(make_pair(mid-p.second.first,make_pair(p.second.first*-1,(mid-1)*-1 )));
            if(p.second.second-mid)
                pq.push(make_pair(p.second.second-mid,make_pair((mid+1)*-1,p.second.second*-1)));
            if(j == k-1) {
                printf("Case #%d: %d %d",i,p.second.second - mid,mid-p.second.first);
            }
        }
    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;

pair<pair<int,int>,int> b(int a, int b){
    assert(b != a+1);
    int mid = (a+b)/2;
    int L = mid-a-1;
    int R = b-mid-1;
    return {{min(L,R),max(L,R)},-mid};
}

int main(){
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t,k,n;
    scanf("%d",&t);
    for(int q = 0; q < t; q++){
        scanf("%d%d",&n,&k);
        set<int> s;
        priority_queue<pair<pair<int,int>,int>> pq;
        s.insert(0);
        s.insert(n+1);
        pq.push(b(0,n+1));
        s.insert((n+1)/2);
        for(int i = 0; i < k; i++){
            while(1){
                auto p = pq.top();
                pq.pop();
                int M = -p.second;
                auto it = s.find(M);
                it--;
                int L = *it;
                it++; it++;
                int R = *it;
                if(i == k-1){
                    printf("Case #%d: %d %d\n",q+1,p.first.second,p.first.first);
                    break;
                }
                if(M != L+1) pq.push(b(L,M)), s.insert((L+M)/2);
                if(R != M+1) pq.push(b(M,R)), s.insert((M+R)/2);
                break;
            }
        }
    }
}
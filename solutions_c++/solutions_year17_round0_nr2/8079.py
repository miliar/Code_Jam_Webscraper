#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
int main(){
    set<ull> tidy;
    set<ull>::iterator it;
    priority_queue<ull,vector<ull>,greater<ull> > pq;
    ull aux,n;
    int tc;
    pq.push(1),pq.push(2),pq.push(3),pq.push(4),pq.push(5),pq.push(6),pq.push(7),pq.push(8),pq.push(9);
    while(pq.top()<=1e18){
        aux=pq.top();
        pq.pop();
        tidy.insert(aux);
        for(int i=aux%10; i<=9; i++)
            pq.push(aux*10+i);
    }
    while(!pq.empty()){
        tidy.insert(pq.top());
        pq.pop();
    }
    cin>>tc;
    for(int i=1; i<=tc; i++){
        cin>>n;
        it=upper_bound(tidy.begin(),tidy.end(),n);
        it--;
        cout<<"Case #"<<i<<": "<<(*it)<<endl;
    }
}

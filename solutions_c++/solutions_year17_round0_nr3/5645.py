#include<bits/stdc++.h>

using namespace std;

priority_queue<long long> pq;

int main(){
    //freopen("C-small-2-attempt0.in","r",stdin);
   // freopen("stall1.txt","w",stdout);
    int T;
    cin>>T;
    for(int O=0;O<T;O++){
        pq = priority_queue<long long>();
        long long n,k,a,b;
        cin>>n>>k;
        pq.push(n);
        for(long long i=0;i<k;i++){
            long long z = pq.top();
            pq.pop();
            if(i==k-1){
                a=max(ceil((double)(z-1)/2),(double)0);
                b=max(floor((double)(z-1)/2),(double)0);
            }
            else{
                pq.push(floor(z/2));
                if(z%2==1)pq.push(floor(z/2));
                else pq.push((z/2)-1);
            }
        }

        cout<<"Case #"<<O+1<<": "<<a<<" "<<b<<endl;
    }
}

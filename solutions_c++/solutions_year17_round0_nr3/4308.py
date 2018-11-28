#include <bits/stdc++.h>
using namespace std;
int main()
{
    ifstream inp("C-small-2-attempt0.in");
    ofstream op;
    op.open("GCJ17C.txt",ios_base::app);
    int tc,caseno=1;
    inp>> tc;
    while(tc--){
        long long int n,k,m,x=0,p,q;
        inp>> n >> k;
        priority_queue <long long int> pq;
        pq.push(n);
        while(1){
            long long int m=pq.top();
            pq.pop();
            x++;
            if(m%2==0){
                pq.push(m/2);
                pq.push((m/2)-1);
                if(x==k){
                    p=m/2;
                    q=p-1;
                }
            }
            else{
                pq.push(m/2);
                pq.push(m/2);
                if(x==k) p=q=m/2;
            }
            if(k==x) break;
        }
        op<< "Case #" << caseno++ << ": " << p << " " << q <<endl;
    }
    op.close();
    return 0;
}

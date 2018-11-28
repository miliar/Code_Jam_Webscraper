#include<iostream>
#include<algorithm>
#include<queue>
#include<cstdio>
using namespace std;
int main (){
    freopen("C-large.in","r",stdin);
    freopen("CLout.txt","w",stdout);

    int T;
    long long N,K;
    cin >> T;
    for(int ca=1;ca<=T;ca++){
        cin >> N >> K;
       // priority_queue<int> pq;
       // pq.push(N);
       // int now;
        long long A,B;
        long long now;
        now = N;
        while(K > 1){
             if(now % 2 == 0){
                A = now/2;
                B = (now-1)/2;
            }else{
                A = now/2;
                B = now/2;
            }
            if( K % 2 == 0){
                now = A;
            }else{
                now = B;
            }
            K/=2;

        }
         if(now % 2 == 0){
                A = now/2;
                B = (now-1)/2;
            }else{
                A = now/2;
                B = now/2;
            }
       /* for(int i=0;i<K-1;i++){
            now = (pq.top());
            if(now == 0)break;
            pq.pop();
            if(now % 2 == 0){
                A = now/2;
                B = (now-1)/2;
            }else{
                A = now/2;
                B = now/2;
            }
            if(A > 0)pq.push(A);
            if(B > 0)pq.push(B);
            cout << now << "\n";
        }
        now = (pq.top());

        if(now % 2 == 0){
                A = now/2;
                B = (now-1)/2;
            }else{
                A = now/2;
                B = now/2;
            }*/
        cout << "Case #" << ca << ": " ;
        cout << A << " " << B << "\n";
    }
    return 0;
}

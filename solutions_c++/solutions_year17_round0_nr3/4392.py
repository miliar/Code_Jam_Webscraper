#include <cstdio>
#include <queue>
#include <algorithm>
using namespace std;

struct Data{
    long long int pos;
    long long int l;
    long long int r;
};

struct Data temp_mid, temp_l, temp_r, temp_q2;
int T;
long long int K,N;
long long int a,b, c, d;

int main(){
    while(~scanf("%d", &T)){
        for(int t=1; t<=T; t++){
            queue<struct Data> q;
            queue<struct Data> q2;
            scanf("%lld %lld", &N, &K);
            if(K==1){
                if(N%2==1){
                    a=N/2;
                    b=N/2;
                } 
                else{
                    a=N/2;
                    b=N/2-1;
                }
                if(a<0)
                    a=0;
                if(b<0)
                    b=0;
                printf("Case #%d: %lld %lld\n", t, a, b);      
                continue;
            }
            temp_mid.pos = (N+1)/2;
            temp_mid.l = 0;
            temp_mid.r = N+1;
            q.push(temp_mid);
            for(int i=0; i<K; i++){
                if(!q2.empty()){
                    temp_q2 = q2.front(); 
                    a = max(temp_q2.r-temp_q2.pos-1, temp_q2.pos-temp_q2.l-1);
                    b = min(temp_q2.r-temp_q2.pos-1, temp_q2.pos-temp_q2.l-1);
                    temp_mid = q.front();
                    c = max(temp_mid.r-temp_mid.pos-1, temp_mid.pos-temp_mid.l-1);
                    d = min(temp_mid.r-temp_mid.pos-1, temp_mid.pos-temp_mid.l-1);
                    if(b>d || b==d && a>=c){
                        temp_mid = q2.front();
                        q2.pop(); 
                    }
                    else{
                        temp_mid = q.front();
                        q.pop(); 
                    }
                }
                else{
                    temp_mid = q.front();
                    q.pop();
                }
                a = max(temp_mid.r-temp_mid.pos-1, temp_mid.pos-temp_mid.l-1);
                b = min(temp_mid.r-temp_mid.pos-1, temp_mid.pos-temp_mid.l-1);
                //printf("pop %lld %lld %lld %lld %lld\n", temp_mid.pos, temp_mid.l, temp_mid.r, a, b);
                if(i<=K){
                    if(temp_mid.r-temp_mid.pos>temp_mid.pos-temp_mid.l){
                        temp_r.pos = (temp_mid.pos+temp_mid.r)/2;
                        if(temp_r.pos != temp_mid.pos){
                            temp_r.l = temp_mid.pos;
                            temp_r.r = temp_mid.r;
                            q.push(temp_r);
                        }
                        temp_l.pos = (temp_mid.pos+temp_mid.l)/2;
                        if(temp_l.pos != temp_mid.l){
                            temp_l.l = temp_mid.l;
                            temp_l.r = temp_mid.pos;
                            q2.push(temp_l);
                        }
                    }
                    else{
                        temp_l.pos = (temp_mid.pos+temp_mid.l)/2;
                        if(temp_l.pos != temp_mid.pos){
                            temp_l.l = temp_mid.l;
                            temp_l.r = temp_mid.pos;
                            q.push(temp_l);
                        } 
                        temp_r.pos = (temp_mid.pos+temp_mid.r)/2;
                        if(temp_r.pos != temp_mid.l){
                            temp_r.l = temp_mid.pos;
                            temp_r.r = temp_mid.r;
                            q.push(temp_r);
                        }                   
                    }
                }
            } 
            a = max(temp_mid.r-temp_mid.pos-1, temp_mid.pos-temp_mid.l-1);
            b = min(temp_mid.r-temp_mid.pos-1, temp_mid.pos-temp_mid.l-1);
            if(a<0)
                a=0;
            if(b<0)
                b=0;
            printf("Case #%d: %lld %lld\n", t, a, b);   
        }
    }
}

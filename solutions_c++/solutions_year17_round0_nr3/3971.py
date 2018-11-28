#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <queue>
using namespace std;

int main(){
    int cas;
    while(scanf("%d", &cas)!=EOF){
        for(int t=1;t<=cas;t++){
            long long int n, k;
            scanf("%lld %lld", &n, &k);
            priority_queue<long long int> q;
            q.push(n);
            long long int count = 0;
            while(count != k-1){
                count++;
                long long int tmp = q.top();
                q.pop();
                if(tmp % 2){
                    q.push(tmp/2);
                    q.push(tmp/2);
                }
                else{
                    q.push(tmp/2);
                    q.push(tmp/2-1);
                }
            }
            long long int tmp = q.top();
            printf("Case #%d: ", t);
            if(tmp % 2)
                printf("%lld %lld\n", tmp/2, tmp/2);
            else if(tmp == 0)
                printf("0 0\n");
            else
                printf("%lld %lld\n", tmp/2, tmp/2-1);
        }
    }
    return 0;
}

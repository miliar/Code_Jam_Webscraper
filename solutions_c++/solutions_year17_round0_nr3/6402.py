#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<vector>
#include<set>
#include<stack>
#include<map>
#include<ctime>
#include<bitset>
#define LL long  long
#define db double
#define EPS 1e-8
#define inf 1e9
#define pi 3.1415926535898
using namespace std;

const int maxn = 30;
priority_queue<pair<LL,LL>> Q;

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    scanf("%d",&T);
    int icase = 1;
    LL n,k;
    while(T-- && ~scanf("%lld %lld",&n,&k)){
        while(Q.empty() == false) Q.pop();
        Q.push(make_pair(n,1));
        while(k > Q.top().second){
            auto head = Q.top();
           // printf("%lld %lld\n",head.first,head.second);
            Q.pop();
            k -= head.second;
            if(head.first & 1){
                Q.push(make_pair( (head.first - 1) / 2,head.second * 2));
            }
            else{
                Q.push(make_pair(head.first / 2,head.second));
                Q.push(make_pair(head.first / 2 - 1,head.second));
            }
            head = Q.top();
            Q.pop();
            while(Q.empty() == false && Q.top().first == head.first){
                head.second += Q.top().second;
                Q.pop();
            }
            Q.push(head);
        }
        LL v = Q.top().first;
        LL l,r;
        if(v & 1){
            l = r = v / 2;
        }
        else{
            l = r = v / 2;
            r--;
        }
        printf("Case #%d: %lld %lld\n",icase++,l,r);
    }
    return 0;
}

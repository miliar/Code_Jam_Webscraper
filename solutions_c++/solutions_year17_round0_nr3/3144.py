#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <queue>
#include <math.h>
#include <set>
#include <map>
#include <climits>
#define INF 0x3f3f3f3f
using namespace std;
typedef long long ll;
int t;
ll seen = 0;
map<ll, ll> dict;
vector<ll> lefts;
int main()
{
    scanf("%d",&t);
    for(int test= 0;test<t;test++){
        ll n,k;
        dict.clear();
        lefts.clear();
        seen = 0;
        scanf("%lld %lld",&n,&k);
        priority_queue<ll> que;
        que.push(n);
        lefts.push_back(1);
        dict[n]=seen++;
        ll served = 0;
        while (true) {
            ll now = que.top();
            que.pop();
            ll a = (now-1)/2;
            ll b = now-1-a;
            ll cnt = lefts[dict[now]];
            if(a==b){
                ll newct = cnt*2;
                if(dict.find(a)==dict.end()){
                    lefts.push_back(newct);
                    dict[a]=seen++;
                    if(a>0){
                        que.push(a);
                    }
                }else{
                    lefts[dict[a]]+=newct;
                }
                
            }else{
                if(dict.find(b)==dict.end()){
                    lefts.push_back(cnt);
                    dict[b]=seen++;
                    if(b>0){
                        que.push(b);
                    }
                }else{
                    lefts[dict[b]]+=cnt;
                }
                
                if(dict.find(a)==dict.end()){
                    lefts.push_back(cnt);
                    dict[a]=seen++;
                    if(a>0){
                        que.push(a);
                    }
                }else{
                    lefts[dict[a]]+=cnt;
                }
                
            }
            served+=cnt;
            if(served>=k){
                printf("Case #%d: %lld %lld\n",test+1,b,a);
                break;
            }
            
            lefts[dict[now]]=0;
        }
    }
    
    return 0;
}

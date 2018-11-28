#include <stdio.h>
#include <iostream>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <string.h>
#include <string>
#include <math.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

struct p{
    int s,e,w;
};

bool cmp(p a, p b){
    return a.s < b.s;
}

p arr[400];

void process(){
    priority_queue<int,vector<int>,greater<int> > cc, cj;
    int ac, aj;
    int ctot = 720, jtot = 720;
    scanf("%d %d",&ac,&aj);
    int tot=  0;
    for(int i = 0 ; i < ac + aj ; i++){
        scanf("%d %d",&arr[i].s,&arr[i].e);
        arr[i].w = i < ac ? 1 : 2;
        if(arr[i].w == 1) ctot -= arr[i].e-arr[i].s;
        else jtot -= arr[i].e-arr[i].s;
    }
    sort(arr,arr+ac+aj,cmp);

    for(int i = 1 ; i < ac + aj ; i++){
        if(arr[i].w==1){
            if(arr[i-1].w==1){
                cc.push(arr[i].s-arr[i-1].e);
                tot+=2;
            }
            else{
                tot++;
            }
        }
        else{
            if(arr[i-1].w==2){
                cj.push(arr[i].s-arr[i-1].e);
                tot+=2;
            }
            else{
                tot++;
            }
        }
    }
    if(arr[0].w==arr[ac+aj-1].w){
        if(arr[0].w==1) cc.push(1440+arr[0].s-arr[ac+aj-1].e);
        else cj.push(1440+arr[0].s-arr[ac+aj-1].e);
        tot+=2;
    }
    else{
        tot++;
    }
    while(!cc.empty()&&cc.top() <= ctot){
        ctot -= cc.top();
        cc.pop();
        tot -= 2;
    }
    while(!cj.empty()&&cj.top() <= jtot){
        jtot -= cj.top();
        cj.pop();
        tot -= 2;
    }
    printf("%d",tot);
}

int main(){
    //freopen("input.txt","rt",stdin);
    //freopen("output.txt","wt",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++){
        printf("Case #%d: ",i);
        process();
        puts("");
    }
}

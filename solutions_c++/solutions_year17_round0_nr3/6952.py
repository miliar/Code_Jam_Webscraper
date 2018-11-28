
#include <iostream>
#include <vector>
#include <string.h>
#include <stdlib.h>
#include <climits>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <stdio.h>

#define LL unsigned long long
using namespace std;
int const maxN = 10000 + 100;
int const maxM = 100000 + 5000;
int T;
LL n,m;

class Stall{
public:
    bool empty = true;
    int left, right ,self;
    int minRL(){
        return min(self - left , right - self) -1;
    };
    int maxRL(){
        return max(self - left , right - self) -1;
    }
};

Stall ss[1002];

int main(){
//    freopen("C-small-1-attempt0.in", "r", stdin);
//    freopen("oy.txt","w",stdout);
//    freopen("input.txt", "r", stdin);
    //    freopen("oy.txt","w",stdout);
    scanf("%d",&T);
    int t = 0;
    while(T--){
        t++;
        scanf("%llu%llu",&n,&m);
        ss[0].empty = false;
        ss[n + 1].empty = false;
        for (int i = 1; i < n + 1; i ++) {
            ss[i].left = 0;
            ss[i].right = n + 1;
            ss[i].self=i;
            ss[i].empty = true;
        }
        int index = 0;
        for (int i = 0 ; i < m; i++) {
            int me = INT_MIN;
            bool repeated = false;
            for (int j = 1; j < n + 1; j ++) {
                if(!ss[j].empty) continue;
                if(ss[j].minRL() == me)
                    repeated = true;
                if(ss[j].minRL() > me){
                    me = ss[j].minRL();
                    index = j;
                    repeated = false;
                }
            }
            
            if(repeated){
                int m2 = INT_MIN;
                for (int j = 1; j < n + 1; j ++) {
                    if(!ss[j].empty) continue;
                    if(ss[j].minRL()!= me) continue;
                    if(ss[j].maxRL() > m2){
                        m2 = ss[j].maxRL();
                        index = j;
                        repeated = false;
                    }
                }
            }
            ss[index].empty = false;
            for (int j = 1; j < n + 1; j ++) {
                if(!ss[j].empty)continue;
                if(index < j && ss[j].left < index)
                    ss[j].left = index;
                if(index > j && ss[j].right > index)
                    ss[j].right = index;
            }
        }
        
        printf("Case #%d: %d %d \n",t, ss[index].maxRL(), ss[index].minRL());
        
    }
}

/*
 ---+-+--
 ++++-+--
 +++++-+-
 ++++++-+
 +++----+
 +++----+
 */
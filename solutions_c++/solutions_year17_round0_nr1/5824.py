#include <iostream>
#include <cstdio>
#include <cstring> 
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <queue> 
#define ll long long

using namespace std;

int main() {
    int t; scanf("%d",&t);
    for(int tc=1; tc<=t; tc++) {
        int k,total,hcnt=0,ans=0,r;
        string pp; cin >> pp >> k;
        total = pp.size();
        r = -1;
        for(int i=0; i<total; i++) {
            if(pp[i] == '+')
                hcnt++;
            else r = max(r,i);
        }
        if(hcnt == total) {
            printf("Case #%d: %d\n",tc,ans);
            continue;
        }
        bool imp = 0;
        while(hcnt!=total) {
            for(int i=r; i>r-k; i--) {
                if(i<0) {
                    printf("Case #%d: IMPOSSIBLE\n",tc);
                    imp = 1;
                    break;
                } else {
                    if(pp[i] == '+') {
                        pp[i] = '-';
                        hcnt--;
                    } else {
                        pp[i] = '+';
                        hcnt++;
                    }
                }
            }
            if(imp) break;
            ans++;
            for(int i=r; i>=0; i--) {
                if(pp[i] == '-') {
                    r = i;
                    break;
                }
            }
        }
        if(imp) continue;
        printf("Case #%d: %d\n",tc,ans);
    }
}

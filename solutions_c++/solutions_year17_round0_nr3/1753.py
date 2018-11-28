//
//  main.cpp
//  Google
//
//  Created by Mec0825 on 13-4-13.
//  Copyright (c) 2013年 Mec0825. All rights reserved.
//

#include <iostream>
#include <map>

using namespace std;

map<long long, long long> gao(map<long long, long long> a) {
    
    map<long long, long long> res;
    map<long long, long long>::iterator p;
    
    for(p = a.begin(); p != a.end(); p++) {
        if(p->first == 1) continue;
        
        if(res.find(p->first/2) == res.end()) {
            res[p->first/2] = p->second;
        }
        else {
            res[p->first/2] += p->second;
        }
        
        if(res.find((p->first-1)/2) == res.end()) {
            res[(p->first-1)/2] = p->second;
        }
        else {
            res[(p->first-1)/2] += p->second;
        }
    }
    
    return res;
    
}

int main()
{
    freopen("/Users/mec/Documents/Competition/Google/2017/Qualification/C-large.in", "r", stdin);
    freopen("/Users/mec/Documents/Competition/Google/2017/Qualification/C-out.txt", "w", stdout);
    
    int numc;
    
    scanf("%d", &numc);
    
    for(int t = 0; t < numc; t++) {
        
        long long N, K;
        
        scanf("%lld %lld", &N, &K);
        
        long long total_cnt = 0;
        
        map<long long, long long> a;
        a[N] = 1;
        
        long long res = 1;
        
        while(!(a.size() == 1 && a.find(1) != a.end())) {
            
            map<long long, long long>::reverse_iterator p;
            for(p = a.rbegin(); p != a.rend(); p++) {
//                printf("%lld ", p->first);
                if(total_cnt + p->second >= K) {
                    res = p->first;
                    break;
                }
                total_cnt += p->second;
            }
//            printf("\n");
            
//            printf("%lld\n", total_cnt);
            if(res != 1) break;
            
            map<long long, long long> b = gao(a);
//            for(p = b.rbegin(); p != b.rend(); p++) {
//                printf("%lld ", p->first);
//            }
//            printf("\n");
            a = b;
            
        }
        
        printf("Case #%d: %lld %lld\n",t+1, res/2, (res-1)/2);
        
    }
    
    return 0;
}

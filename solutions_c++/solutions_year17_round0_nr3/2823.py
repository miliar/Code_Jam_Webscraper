//
//  main.cpp
//  gcj_qual_c
//
//  Created by yupeng gou on 4/8/17.
//  Copyright © 2017 yupeng gou. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
//pair<int,int> cal(bool maps[20],int pos,int len){
//    int l = 0;
//    int lp = pos;
//    int rp = pos;
//    int r = 0;
//    while(lp > 0 && !maps[--lp]) l++;
//    while(rp + 1 <len &&!maps[++rp]) r++;
//    
//    return make_pair(l,r);
//}
//
//pair<int, int> dfs(int len ,int k){
//    bool maps[20];
//    memset(maps, false, sizeof maps);
//    int result = 0;
//    for(int i = 1 ; i <= k ; i++){
//        int cur = -1;
//        int ma = -1;
//        for(int j = 0 ; j < len ; j++){
//            if(!maps[j]){
//                auto tmp_c =cal(maps,j,len);
//                int c = min(tmp_c.first, tmp_c.second);
//                if(c > cur){
//                    cur = c;
//                    result = j;
//                    ma = max(tmp_c.first, tmp_c.second);
//                }
//                else if (c == cur){
//                    if(max(tmp_c.first, tmp_c.second) > ma){
//                        cur = c;
//                        result = j;
//                        ma = max(tmp_c.first, tmp_c.second);
//                    }
//                }
//            }
//        }
//        
//        maps[result] = true;
//    }
////    cout<<result<<endl;
//   auto re = cal(maps, result , len);
////    cout<<re.first<<' '<<re.second<<endl;
//    return make_pair(max(re.first , re.second), min(re.first , re.second));
//}
int main(int argc, const char * argv[]) {
    freopen("/Users/yupenggou/Documents/gcj_2016_practice/gcj_qual_c/in.txt", "r", stdin);
    freopen("/Users/yupenggou/Documents/gcj_2016_practice/gcj_qual_c/out.txt", "w", stdout);

    int cases;
    cin >> cases;
    for(int it = 1 ; it <= cases ; it ++){
        long long k,n;
        cin >> n >> k;
        long long index = 1;
        while(index <= k){
            index *= 2;
        }
        index /= 2;
//        cout<<index<<endl;
        long long times = (n - k) / index;
        
        long long lmax = times / 2 + (times % 2);
        long long lmin = times  - lmax;
        
        cout<<"Case #"<<it<<": "<<lmax<<' '<<lmin<<endl;
    }
    
//    auto test = dfs(1000,400);
//    cout<<"test"<<' '<<test.first<<' '<<test.second<<endl;
//    for(int n = 1 ; n <= 25  ;n ++){
//        for(int k = 1 ; k <= n ; k ++){
//            auto result = dfs(n,k);
//            cout<<n<<' '<<k<<" : " << result.first<<' '<<result.second<<endl;
//        }
//    }
    return 0;
}

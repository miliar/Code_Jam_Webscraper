#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <map>

using namespace std;

int main (){
    freopen ("in.txt", "r", stdin);
    freopen ("out.txt", "w", stdout);

    int T;
    
    cin >> T;
    


    for (int cas = 1; cas <= T; ++cas){
        map<int64_t, int64_t> cnt;
        queue<int64_t> que;
        int64_t n, k;
        cin >> n >> k;  

        que.push(n);
        cnt[n] = 1;
        int64_t have = 0;
        int64_t resmax = 0, resmin = 0;
        while (!que.empty()){ 

            int64_t x = que.front();
            que.pop();

            if (have + cnt[x] >= k){
                resmax = x / 2; 
                resmin = (x-1) / 2;
                resmin = max(resmin, 0LL);
                break;
            }
            
            have += cnt[x];

            if ( x / 2  > 0) {
                if (cnt.find(x/2) == cnt.end())
                    que.push(x/2);
                cnt[x / 2] += cnt[x];
            }
            if ( (x-1) / 2 > 0){
                if (cnt.find((x-1)/2) == cnt.end()) 
                    que.push((x-1)/2);
                cnt[(x-1)/2] += cnt[x]; 
            } 

        }

        cout << "Case #"<< cas << ": " << resmax << " " << resmin << endl;
    }
    return 0;
}








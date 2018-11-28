#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cmath>
#include <algorithm>

using namespace std;

int main(){
    size_t T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        int N, K;
        cin >> N >> K;
        vector<int> stall(N, 0);
        vector<int> ls(N, 0);
        vector<int> rs(N, 0);

        for(int i = 0; i < N; ++i){
            ls[i] = i;
            rs[i] = N - 1 - i;
        }
        for(int k = 0; k < K; ++k){
            int mxi = -1;
            for(int i = 0; i < N; ++i){
                if(stall[i] == 0 
                        && (min(ls[i], rs[i]) > min(ls[mxi], rs[mxi]) || mxi == -1 )){
                    mxi = i; 
                }
            }
            int mmxi = mxi;
            for(int i = mxi+1; i < N; ++i){
                if(stall[i] == 0 
                        && min(ls[i], rs[i]) == min(ls[mxi], rs[mxi])
                        && max(ls[i], rs[i]) > max(ls[mmxi], rs[mmxi])){
                    mmxi = i; 
                }
            }
            stall[mmxi] = 1;
            for(int i = 0; i < N; ++i){
                if(i < mmxi && stall[i] == 0){
                    rs[i] = min(rs[i], mmxi - i -1);
                }
                if(i > mmxi && stall[i] == 0){
                    ls[i] = min(ls[i], i - mmxi - 1);
                }
            }
            if( k == K -1){
                cout << "Case #" << t << ": " << max(ls[mmxi], rs[mmxi]) << " " << min(ls[mmxi], rs[mmxi]) << endl;
            }
        }
    }
}


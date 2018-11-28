#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <deque>
#include <complex>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstring>

#define REP(i,x) for(int i=0 ; i<(int)(x) ; i++)
#define ALL(x) (x).begin(),(x).end()
#define LL long long

using namespace std;

int main(){
    const double PI = acos(-1.0);
    int T;
    cin >> T;
    REP(tc, T){
        int N, K;
        cin >> N >> K;
        vector<LL> R(N);
        vector<LL> H(N);
        REP(i, N){
            cin >> R[i] >> H[i];
        }
        LL res = 0;
        REP(i, N){
            vector<LL> area;
            REP(j, N){
                if(i==j)continue;
                if(R[j]>R[i])continue;
                area.push_back(2LL*R[j]*H[j]);
            }
            if((int)area.size()<K-1)continue;
            sort(ALL(area));
            reverse(ALL(area));
            LL sum = R[i]*R[i] + 2LL*R[i]*H[i];
            REP(j, K-1){
                sum += area[j];
            }
            res = max(res, sum);
            //cerr << R[i] << " " << area.size() << " " << res << " " << sum << endl;
        }
        printf("Case #%d: %.9f\n", tc+1, PI*res);
    }
    return 0;
}

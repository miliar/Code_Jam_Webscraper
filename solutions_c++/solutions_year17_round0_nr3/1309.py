#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
//#include <unordered_map>
#include <list>
#include <bitset>
#include <utility>
#include <cassert>
#include <iomanip>
#include <ctime>
#include <fstream>
#include <bitset>

using namespace std;

const int me = 10025;

pair<long long, long long> brute(int N, int K){
    int used[N + 5], l[me], r[me];
    int last = -1;
    fill(used, used + N + 5, 0);
    used[0] = 1;
    used[N + 1] = 1;
    for(int i = 1; i <= K; i ++){
        for(int k = 1; k <= N; k ++){
            if(used[k])
                continue;
            for(int j = k - 1; j >= 0; j --)
                if(used[j]){
                    l[k] = k - j - 1;
                    break;
                }
            for(int j = k + 1; j <= N + 1; j ++)
                if(used[j]){
                    r[k] = j - k - 1;
                    break;
                }
        }
        int vl = -1;
        for(int j = 1; j <= N; j ++)
            if(!used[j])
                vl = max(vl, min(l[j], r[j]));
        int pos = -1, mx = -1;
        for(int j = 1; j <= N; j ++)
            if(!used[j])
                if(min(l[j], r[j]) == vl){
                    if(pos == -1)
                        pos = j, mx = max(l[j], r[j]);
                    else if(max(l[j], r[j]) > mx)
                        pos = j, mx = max(l[j], r[j]);
                }
        used[pos] = 1;
        last = pos;
    }
    int L = 0, R = 0;
    for(int i = last - 1; i >= 0; i --)
        if(used[i]){
            L = last - i - 1;
            break;
        }
    for(int j = last + 1; j <= N + 1; j ++)
        if(used[j]){
            R = j - last - 1;
            break;
        }
    return make_pair(max(L, R), min(L, R));
}
long long getMax(long long N, long long K){
    if(K == 2)
        return N - 2;
    if(K == 3)
        return N / 2 - 1;
    long long middle = (N + 1) / 2;
    if(K % 2 == 0)
        return max(0LL, getMax(N - middle + 1, K - K / 2 + 1));
    return max(getMax(middle, K / 2 + 1), 0LL);
    // max(getMax(middle, K / 2 + 1), getMax(N - middle + 1, K - K / 2 + 1));
}
long long getMin(long long N, long long K){
    if(K == 2)
        return N - 2;
    if(K == 3)
        return (N - 1) / 2 - 1;
    long long middle = (N + 1) / 2;
    if(K % 2 == 0)
        return max(0LL, getMin(N - middle + 1, K - K / 2 + 1));
    return max(getMin(middle, K / 2 + 1), 0LL);
    // max(getMin(middle, K / 2 + 1), getMin(N - middle + 1, K - K / 2 + 1));
}
bool check(){
    for(int i = 0; i < 1234; i ++){
        int N = 1LL * rand() * rand() % 1234 + 1;
        int K = 1LL * rand() % rand() % N + 1;
        if(make_pair(getMax(N + 2, K + 2), getMin(N + 2, K + 2)) != brute(N, K)){
            cout << N << " and " << K << endl;
            return false;
        }
    }
    return true;
}

int main(int argc, const char * argv[]) {
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    //srand(unsigned(time(NULL)));
    //cout << check() << endl;
    int T;
    long long N, K;
    cin >> T;
    for(int c = 0; c < T; c ++){
        cin >> N >> K;
        cout << "Case #" << c + 1 << ": ";
        // pair<int, int> g = brute(N, K);
        // cout << g.first << " " << g.second << endl;
        cout << getMax(N + 2, K + 2) << " " << getMin(N + 2, K + 2) << endl;
    }
    
    return 0;
}

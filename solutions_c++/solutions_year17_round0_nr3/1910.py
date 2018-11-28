#include <iostream>
#include <string>
#include <vector>
#include <utility>

using namespace std;
typedef long long LL;

pair<LL,LL> solve(LL N, LL K){
    LL base = 0;
    while((1LL << (base+1))-1 < K) ++base;
    LL div = (1LL << base)-1;
    LL rest = N - div;
    LL width = rest / (div+1);
    LL plus1cnt = rest - (div+1) * width;
    //cerr << div << " " << rest << " " << width << " " << plus1cnt << endl;
    LL place = K - div;
    if(place <= plus1cnt){
        return pair<LL,LL>((width+1)/2, (width+0)/2);
    }else{
        return pair<LL,LL>((width+0)/2, (width-1)/2);
    }
}

int main(){
    int T;
    cin >> T;
    for(int t = 1; t <= T; ++t){
        LL N, K;
        cin >> N >> K;
        pair<LL,LL> res = solve(N, K);
        cout << "Case #" << t << ": " << res.first << " " << res.second << endl;
    }
    return 0;
}


#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;

//123
//61 61
//30 30 30 30
//15 14 15 14 15 14 15 14
//7 7 7 6 7 7 7 6 7 7 7 6 7 7 7 6
//3 3 3 3 3 3 3 2 3 3 3 3 3 3 3 2 3 3 3 3 3 3 3 2 

int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        ll N, K;
        cin >> N >> K;
        
        K--;
        ll pow2 = 1;
        ll factor = N;
        ll left = N;
        while(K >= pow2){
            K -= pow2;
            factor = (factor-1)/2;
            left -= pow2;
            pow2 *= 2;
        }

        ll plusones = (left - pow2*factor);
        ll ans = factor;
        if(K<plusones) ans++;

        cout << "Case #" << t << ": " << ans/2 << " " << (ans-1)/2 << endl;
    }

    return 0;
}
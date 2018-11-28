#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;
typedef long long ll;



int main(){
    int T;
    cin >> T;
    for(int t=1;t<=T;t++){
        string pancakestring;
        int K;
        cin >> pancakestring >> K;
        
        int L = pancakestring.length();
        vector<int> pancakes(L, 0);
        for(int i=0;i<L;i++){
            if(pancakestring[i]=='+') pancakes[i]=1;
            else pancakes[i] = -1;
        }

        int ans = 0;
        for (int i=0;i<=L-K;i++){
            if(pancakes[i]==-1){
                ans ++;
                for(int j=i;j<i+K;j++) pancakes[j] = -pancakes[j];
            }
        }

        bool good = true;
        for (int i=0;i<L;i++) if(pancakes[i]==-1) good=false;

        if(good){
            cout << "Case #" << t << ": " << ans << endl;
        }else{
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
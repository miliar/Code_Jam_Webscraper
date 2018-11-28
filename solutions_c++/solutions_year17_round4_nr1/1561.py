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
        int N, P;
        cin >> N >> P;
        vector<int> freq(P, 0);
        for(int i=0;i<N;i++){
            int G;
            cin >> G;
            freq[G%P]++;
        }

        int ans = 0;
        if(P==2)
        {
            ans = freq[0] + (freq[1]+1)/2;
        }
        else if(P==3)
        {
            ans = freq[0];
            int p12s = min(freq[1], freq[2]);
            ans += p12s;
            freq[1] -= p12s;
            freq[2] -= p12s;
            ans += (freq[1]+2)/3;
            ans += (freq[2]+2)/3;  
        }
        
        cout << "Case #" << t << ": " << ans << endl;

    }

    return 0;
}
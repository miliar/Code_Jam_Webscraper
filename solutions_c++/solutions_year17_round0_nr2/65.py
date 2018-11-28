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
        ll N;
        cin >> N;
        
        vector<int> digits;
        while(N!=0){
            digits.push_back(N%10);
            N/=10;
        }
        digits.push_back(0);

        bool decreasing=true;
        for(int i=0;i+1<digits.size();i++){
            if(digits[i]<digits[i+1]) decreasing=false;
        }
        if(!decreasing){
            int min_ok = -1;
            for(int i=0;i+1<digits.size();i++){
                if(digits[i]<digits[i+1]){
                    min_ok=-1;
                }else if(digits[i]>digits[i+1]){
                    if(min_ok==-1) min_ok = i;
                }
            }

            digits[min_ok]--;
            for(int i=0;i<min_ok;i++) digits[i] = 9;
        }

        ll ans = 0;
        for(int i=digits.size()-1;i>=0;i--){
            ans*=10;
            ans+=digits[i];
        }

        cout << "Case #" << t << ": " << ans << endl;
        
    }

    return 0;
}
#include<bits/stdc++.h>
using namespace std;

int T;

int main(){
    freopen("B-small.in", "r", stdin);
    freopen("B-small.out", "w", stdout);

    cin >> T;

    for(int c=1; c<= T;++c){
        long long N;
        cin >> N;

        for(long long i=N;i>0;i--){
            long long j = i;
            long long lastNum = 9;
            long long currentNum;
            bool flag = true;
            while(j > 0){
                currentNum = j%10;
                if(currentNum <= lastNum){
                    j /= 10;
                    lastNum = currentNum;
                }else{
                    flag = false;
                    break;
                }
            }
            if(flag){
                cout << "Case #" << c << ": " << i << endl;
                break;
            }

        }
    }

}

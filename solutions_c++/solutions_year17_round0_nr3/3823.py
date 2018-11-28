//
// Created by Dai Tao on 2017/4/8.
//
#include <iostream>
#include <map>

using namespace std;


int main(){
    int T;
    cin >> T;

    for(int i = 0; i < T; i++){
        long long int N;
        long long int K;
        cin >> N;
        cin >> K;
        int power = 0;
        while((K >> power) > 0){
            power++;
        }
        power--;
        long long int tmp = (1 << power) - 1;
        // M is slot left
        long long int M = N - tmp;
        long long int small = (M / (1 << (power)));
//        long long int bigNumber = (small != 0) ? M % small : M;
        long long int bigNumber = M - (1 << power) * small;
        long long int max = 0;
        long long int min = 0;
        if(K <= bigNumber + tmp){
            // it split the big number
            if((small + 1) % 2){
                max = small / 2;
                min = small / 2;
            } else{
                max = (small + 1)/2;
                min = max - 1;
            }
        } else{
            if(small % 2){
                max = (small - 1) / 2;
                min = max;
            }else{
                max = small / 2;
                min = max - 1;
            }
        }
        cout << "Case #" << i + 1 << ": " << max << " " << min << endl;

    }
}

/*
    Problem C: Bathroom Stalls
    @author: Christopher W. Frost
 */

#include<iostream>
#include<string>
using namespace std;

int main(){
    int t = 0;
    long long N;
    long long K;
    
    cin >> t;
    for(int i = 1; i <= t; i++){
        cin >> N >> K;
        cout << "Case #" << i << ": ";
        
        long long Ls, Rs;
        long long numSpaces = N;
        
        while(K >= 2){
            if(K%2 == 0){
                if(numSpaces%2 == 0){
                    numSpaces = numSpaces/2;
                    K = K/2;
                }
                else{
                    numSpaces = numSpaces/2;
                    K = K/2;
                }
            }
            else{
                if(numSpaces%2 == 0){
                    numSpaces = numSpaces/2 - 1;
                    K = K/2;
                }
                else{
                    numSpaces = numSpaces/2;
                    K = K/2;
                }
            }
        }
        if(numSpaces%2 == 0){
            Ls = numSpaces/2 - 1;
            Rs = numSpaces/2;
        }
        else{
            Ls = numSpaces/2;
            Rs = Ls;
        }
        
        cout << max(Ls, Rs) << " " << min(Ls, Rs) << '\n';
    }
}

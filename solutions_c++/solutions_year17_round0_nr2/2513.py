/*
 Problem B: Tidy Numbers
 @author: Christopher W. Frost
 */

#include<iostream>
using namespace std;

bool isTidy(long long N){
    while(N%10 >= (N/10)%10 && N != 0)
        N /= 10;
    if(N == 0)
        return true;
    return false;
}

int main(){
    int t = 0;
    long long N = 0;
    cin >> t;
    for(int i = 1; i <= t; i++){
        cin >> N;
        cout << "Case #" << i << ": ";
        
        while(!isTidy(N)){
            int count = 0;
            
            while(N%10 >= (N/10)%10 && N != 0){
                N /= 10;
                count++;
            }
            count++;
            
            long long multiplier = 1;
            for(int i = 0; i < count; i++)
                multiplier *= 10;
            
            N = ((N/10)-1) * multiplier; //Raise N back to its proper power
            N += multiplier-1; //Append necessary 9s
        }
        cout << N << '\n';
    }
}

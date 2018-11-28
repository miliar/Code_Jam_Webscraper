#include<iostream>
#include<vector>
#include<map>
#include<string>

using namespace std;

bool is_tidy(long long n){
    int min = n % 10;
    while(n){
        if(n % 10 > min){
            return false;
        }
        min = n % 10;
        n/=10;
    }
    return true;
}

long long solve(long long numb){
     if(is_tidy(numb)){
        return numb;
     }
     long long mant = 1;
     long long nines = 0;

     while(numb){
         nines *= 10;
         nines += 9;
         numb /= 10;
         mant *= 10;
         long long tmp = (numb - 1) * mant + nines;
         if (is_tidy(tmp)){
             return tmp;
         }


     }
     return nines;
}

int main(){

    int ncases;

    cin >> ncases;


    for(int i = 0; i < ncases;i++){
        long long k;
        cin >> k;
        cout << "Case #" << i + 1 << ": " << solve(k);
        cout << endl;
    }
}

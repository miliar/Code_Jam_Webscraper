#include<bits/stdc++.h>
using namespace std;

#define INT long long int
INT n, k;

void work(INT n, INT k){
//    cout << endl << n << " fsd " << k << endl;
    if(k == 1){
        if(n%2){
            cout << n/2 << " " << n/2;
        }else{
            cout << n/2 << " " << n/2 - 1;
        }  
    }else{
        if(n%2){
            work(n/2, k/2);
        }else{
            // n is   n/2-1   n/2 
            if(k%2){
                work(n/2-1, k/2);
            }else{
                work(n/2, k/2);  
            }        
        } 
    }
}


int main(){
    INT t;
    cin >> t;
    for(INT i = 1; i <= t; i++){
        printf("Case #%ld: ", i);
        cin >> n >> k;
        work(n, k);
        printf("\n");
    }
}

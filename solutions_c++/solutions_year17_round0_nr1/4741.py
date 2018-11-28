#include<iostream>
#include<cmath>
#include<stdint.h>
#include <vector>
using namespace std;



int main(){
   ios::sync_with_stdio(false);
   cin.tie(NULL);
   int T, K, l, odp, licznik;
   string S;
   cin >> T;
   
   for (int o=0; o<T; o++){
   licznik=0;
      odp=0;
      cin >> S >> K;
      l=S.length();
      for (int i=0; i<l-K; i++){
        //cout << i << ' ';
        if (S[i]=='-'){ 
            odp++;
             for(int p=i; p<i+K; p++){
            // cout << p << ' ' << S[p] << ' ';
             if(S[p]=='+') {S[p]='-';}
             else  {S[p]='+';}
             //  cout << S[p] << '\n';
              }
            }
      }
      //cout << '\n';
      for(int i=l-K; i<l; i++){
      //cout << i << ' ';
        if(S[i]=='-'){
          licznik++;
          }
      }
      if(licznik==K){
        odp++;
      }
      
      if(licznik==0 or licznik==K){
        cout << "Case #" << o+1<<": "<<odp<<'\n';
      }
      else{cout << "Case #" << o+1<<": "<<"IMPOSSIBLE"<<'\n';}
      
      
   }
   
    return 0;
}
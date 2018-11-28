#include<iostream>
#include<cmath>
#include<stdint.h>
using namespace std;
int main(){   
ios::sync_with_stdio(false);   
cin.tie(NULL);   
int T,l, licznik;
   string S;   
cin >> T;   
//vector<int> v;  
 for (int o=0; o<T; o++){
    cout << "Case #" << o+1<<": ";
    licznik=0;
    cin >> S;
    l=S.length();
    if(l==1){cout << S[0];}
    for(int i=1; i<l; i++){
        if(S[i]>S[i-1]){
          //cout << 'w' << ' ';
          for(int q=0; q<=licznik; q++){
          cout << S[i-1]-'0';}
          licznik=0;
          if(i==l-1){cout << S[i];}
          }
        else if (S[i]==S[i-1]){
             licznik ++;//cout << "l: " << licznik << ' ';}
             if(i==l-1){
              for(int s=0; s<=licznik; s++){cout << S[i-1]-'0';}
             }
             }
        else{//cout << 'e' << ' ';
            if(S[i-1]=='1'){
            //cout << "jed ";
              for(int v=0; v<l-1; v++){
                cout << 9 ;
              }
              
           } 
           else {
           //cout << "inne "<<licznik << ' ';
              //for(int w=0; w<=licznik; w++){
              cout << S[i-1]-'0'-1;
              //}
              for(int v=i-licznik-1; v<l-1; v++){
                cout << 9 ;
              }
           }
           break;
        }
        
      }
     
     
   cout <<'\n';   }      
 return 0;} 
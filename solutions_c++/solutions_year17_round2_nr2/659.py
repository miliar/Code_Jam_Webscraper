#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <complex>

// #include <gmpxx.h>
//g++ mycxxprog.cc -lgmpxx -lgmp

using namespace std;


int main(){
	int nb;
	cin >>nb;
	for(int cases=0; cases<nb; cases++){
    cout << "Case #"<<cases+1<<": ";
    int N, R, O, Y, G, B,V;
    cin>>N>>R>>O>>Y>>G>>B>>V;
    vector<char> sol(N);
    int s=0;
    if(O==0 && G==0 && V ==0){
      if(R> Y && R > B){sol[s++]= 'R'; R--;N--;}
      else if(Y>B){sol[s++]= 'Y'; Y--;N--;}
      else{sol[s++]= 'B'; B--;N--;}
    }else{
      if(V>0){
        while(V>0){
          sol[s++]= 'Y'; Y--;N--;
          sol[s++]= 'V'; V--;N--;
        }
        if(Y<0){
          cout <<  "IMPOSSIBLE"<<endl;
          continue;
        }
        if (N>0){
          if(Y==0){
            cout <<  "IMPOSSIBLE"<<endl;
            continue;
          }else{
            sol[s++]= 'Y'; Y--;N--;
          }
        }
      }
      
      if(B-O>Y+R-G){sol[s++]= 'B'; B--;N--;}
      
      if(G > 0){
        while(G>0){
          sol[s++]= 'R'; R--;N--;
          sol[s++]= 'G'; G--;N--;
        }
        if(R<0){
          cout <<  "IMPOSSIBLE"<<endl;
          continue;
        }
        if (N!=0){
          if(R==0){
            cout <<  "IMPOSSIBLE"<<endl;
            continue;
          }else{
            sol[s++]= 'R'; R--;N--;
          }
        } 
      }
        
      if(Y>=B-O+R){sol[s++]= 'Y'; Y--;N--;}
      
      if(O>0){
        while(O>0){
          sol[s++]= 'B'; B--;N--;
          sol[s++]= 'O'; O--;N--;

        }
        if(B<0){
          cout <<  "IMPOSSIBLE"<<endl;
          continue;
        }
        if (N!=0){
          if(B==0){
            cout <<  "IMPOSSIBLE"<<endl;
            continue;
          }else{
            sol[s++]= 'B'; B--;N--;
          }
        }
      }
    }
    
    while(N>0){
      if(sol[s-1]=='B'){
        if(R>Y || (R==Y && sol[0]=='R')){sol[s++]= 'R'; R--;N--;}
        else{sol[s++]= 'Y'; Y--;N--;} 
      } else if(sol[s-1]=='Y'){
        if(R>B|| (R==B && sol[0]=='R')){sol[s++]= 'R'; R--;N--;}
        else{sol[s++]= 'B'; B--;N--;} 
      }else if(sol[s-1]=='R'){
        if(B>Y|| (Y==B && sol[0]=='B')){sol[s++]= 'B'; B--;N--;}
        else{sol[s++]= 'Y'; Y--;N--;} 
      }
    }
    if(R<0 || B<0 || Y<0){
      cout <<  "IMPOSSIBLE"<<endl;
      continue;
    }
    if(sol[0]==sol[sol.size()-1]){
      cout <<  "IMPOSSIBLE"<<endl;
      continue;
    }
    for(int i=0;i<sol.size();i++){
      cout << sol[i];
    }
    cout <<endl;
  }
	return 0;
}

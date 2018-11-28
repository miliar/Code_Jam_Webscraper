#include<iostream>
#include<string>
using namespace std;
int T,R,C;
string G[25];
void solve(){
    for(int c =0;c<C;c++){
       char f = '?';
       for(int r=0;r<R;r++){
          if(G[r][c] == '?')
              G[r][c] = f;
          else
              f = G[r][c];
       }
    }
    for(int c =0;c<C;c++){
       char f = '?';
       for(int r=R-1;r>=0;r--){
          if(G[r][c] == '?')
              G[r][c] = f;
          else
              f = G[r][c];
       }
    }
    for(int r =0;r<R;r++){
       char f = '?';
       for(int c=0;c<C;c++){
          if(G[r][c] == '?')
              G[r][c] = f;
          else
              f = G[r][c];
       }
    }
    for(int r =0;r<R;r++){
       char f = '?';
       for(int c=C-1;c>=0;c--){
          if(G[r][c] == '?')
              G[r][c] = f;
          else
              f = G[r][c];
       }
    }
    

}
int main(){
   cin>>T;
   for(int _c = 1; _c<=T ;_c++){
      cin>>R>>C;
      for (int r=0;r<R;r++)
          cin>>G[r];
      solve();
      cout<<"Case #"<<_c<<":"<<endl;
      for(int r=0;r<R;r++)
          cout<<G[r]<<endl;
   }
   return 0;
}

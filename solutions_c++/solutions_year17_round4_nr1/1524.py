#include<bits/stdc++.h>
#include<iostream>
#include<queue>
#include<algorithm>
#include<utility>
#include <cmath>
#include <cstdio>

using namespace std;
int N,P;
int G[5];

void printG(int * G){
  for( int i = 0;i<P;i++){
    cout<< "G["<<i<<"] = "<<G[i]<<endl;
  }
}
int sum(int* G){
  int res = 0;
  for( int i = 0;i<P;i++){
    res+=G[i];
  }
  return res;
}

bool f( int * G, int cnt, int sum, int index){

  //  cout<< N<<" "<<P<<endl;
  if( index==P-1 ){
    //  cout << G<< " "<<cnt<<" "<<sum<<" i = "<<i<<endl;
    if( (cnt*index +sum ) % P == 0 && cnt <= G[index]){
      G[index]-=cnt;
      return true;
    }
    return false;

  }
  if( cnt == 0 ){
    return (sum%P==0);
  }
  for (int c = 0;c<=cnt && c<=G[index];c++){
    G[index]-=c;
    int tmpsum = (sum + c * index)%P;
    if( f( G,cnt-c,tmpsum,index+1) ){
      return true;
    }
    G[index]+=c;
  }
  return false;
}





int main(void){
  int T;
  cin>>T;
  for( int c=1;c<=T;c++){
    int G[5] = {};
    cin>>N>>P;
    for(int i = 0;i<N;i++){

      int g;
      cin>>g;
      G[g%P]++;
    }
    //        cout<<"sumG() = "<<sum(G)<<endl;
    //        printG(G);
    //    printG(G);
    int res = 0;
    for( int gc = 1; gc<= sum(G);gc++){

      while(f(G,gc, 0,0) ){
        //        cout<<"sumG() = "<<sum(G)<<endl;
        //        printG(G);
        res++;

        if(sum(G) < gc )break;
      }
      //      cout<<"sumG() = "<<sum(G)<<endl;
      //      printG(G);

    }
    if( sum(G) > 0 ) res++;
    cout<<"Case #"<<c<<": "<<res<<endl;
    //    printf("Case #%d: %.9f\n", c, r);
  }
  return 0;
}


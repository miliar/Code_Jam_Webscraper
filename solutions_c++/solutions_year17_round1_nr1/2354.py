#include<algorithm>
#include <string>
#include <iostream>
#define fori(l,n) for(int l=0;l<n;l++)
using namespace std;

int main() {
	int I,IT,nada;
     int min,tamano;
     int a,n,t,i,j,pos,p,k;
     //int A[1000];
     //int ban;
     int ban;
     char le;
     string ss[50];
     long R,C;
   // string letra;
	 //string name[2000];
	 

	 
    freopen("sucake.in","r",stdin);
    freopen("cake10.out","w",stdout);
    I=1;
    //scanf("%d", &IT); 
    cin>>IT;
    //IT=1;
    while(I<=IT){
       
       cin>>R>>C;//ss>>tt;
      // a=alien.length();
       //n=ss.length();
       //t=tt.length();
     //  cout<<"alien:"<<alien;
       
       i=0;
       while(i<R){
          cin>>ss[i];
          i++;
       }
       i=0;
   //    while(i<R){
     //     cout<<ss[i]<<endl;
     //     i++;
     //  }
       
       i=0;
       while(i<R){
          j=0;  ban=1;
          while(j<C && ban){
             if(ss[i][j]=='?'){
             }
             else{
                le=ss[i][j];
                ban=0;
                k=j-1;
                while(k>=0){
                   ss[i][k]=le;
                   k--;
                }
             }
             j++;
          }
          
          if(ban==0){
             while(j<C){
                if(ss[i][j]=='?'){
                   ss[i][j]=le;
                }
                else{
                   le=ss[i][j];
                }
                j++;
             }
          }
          
          i++;
       }
       
       i=0;
       ban=-1;
       while(i<R & ban==-1){
          if(ss[i][0]=='?'){
                 i++; 
            }
            else{
                ban=i; 
           }
          
          
       }       
       i=0;
       
       while(i<ban){
          ss[i]=ss[ban];
          i++;
       }
       i=ban+1;
       while(i<R){
          if(ss[i][0]=='?'){
             ss[i]=ss[ban];
          }
          else{
             ban=i;
          }
          i++;
       }
       
       //fin
       cout<<"Case #"<<I<<":\n";
       for(i=0;i<R;i++){
         // for(j=0;j<C;j++){
         //  cout<<ss[i][j];
         // }
         cout<<ss[i];
         cout<<endl;
       }
      // cout<<endl;
     
       I++;
    }
  //  scanf("%d", &nada);
	return 0;
}


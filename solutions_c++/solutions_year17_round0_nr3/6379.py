#include<algorithm>
#include <string>
#include <iostream>
#define fori(l,n) for(int l=0;l<n;l++)
using namespace std;

int main() {
    long int I,IT,nada;
    long int min,tamano;
   
     int ban;
 	 
//	 long int ,p1,p2,i,j,pos,ee,mayor,l;
	 
	 unsigned long int R;	 
	 long double CC;
	 long long N,S,K,D;

    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("s2.out","w",stdout);
    I=1;
    //scanf("%d", &IT); 
    cin>>IT;

  
    while(I<=IT){
      // cout<<"newwwwwwww\n";
       cin>>N>>K;
       
       S=1;
       while(K>=S){
          S=S<<1;
       }
       S=S>>1;
       
       D=N-K;
      /* cout<<"\nN:"<<N;
       cout<<"\nK:"<<K;
       cout<<"\nD:"<<D;
       cout<<"\nS:"<<S;*/
       CC=double(D/S);
     //  cout<<"\nCC:"<<CC;
       R=long(CC);
      // cout<<"\nR:"<<R;
       //cout<<"\n "<<N<<" "<<K<<" "<<S<<" "<<(R+1)/2<<" "<<R/2;
       cout<<"Case #"<<I<<": ";
       cout<<(R+1)/2<<" "<<R/2;
    
    
       cout<<endl;
   
       I++;
    }
	return 0;
}


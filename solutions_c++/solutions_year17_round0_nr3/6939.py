#include<algorithm>
#include <string>
#include <iostream>
#define fori(l,n) for(int l=0;l<n;l++)
using namespace std;

int main() {
	int I,IT,nada;
     int min,tamano;
   
     int ban;
     char letra;
     string sss;
   // string letra;
	 //string name[2000];
	 
	string resp;
	 string alien,ss,tt;
	 
	 
//	 long int ,p1,p2,i,j,pos,ee,mayor,l;
	 
	 long int R;	 
	 double  N,K,S,D;
	 
	 
	 char c;
	 int nume;
	 
    freopen("C-small-2-attempt1.in","r",stdin);
    freopen("stall9.out","w",stdout);
    I=1;
    //scanf("%d", &IT); 
    cin>>IT;
    //IT=1500;
    
   // N=1;K=1;
  // N=10;
  // K=1;
  
    while(I<=IT){
      // cout<<"newwwwwwww\n";
       cin>>N>>K;
       
       S=1;
       while(K>=S){
          S=S*2;
       }
       S=S/2;
       
       D=N-K;
       R=long(D/S);
       
       //cout<<"\n "<<N<<" "<<K<<" "<<S<<" "<<(R+1)/2<<" "<<R/2;
       cout<<"Case #"<<I<<": ";
       cout<<(R+1)/2<<" "<<R/2;
       //cout<<" n k "<<N<<" "<<K<<" ";
    
       cout<<endl;
       K++;
       I++;
    }
  //  scanf("%d", &nada);
	return 0;
}


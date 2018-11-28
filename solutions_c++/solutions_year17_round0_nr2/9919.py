#include<algorithm>
#include <string>
#include <iostream>
#define fori(l,n) for(int l=0;l<n;l++)
using namespace std;

int main() {
	int I,IT,nada;
     int min,tamano;
     int a,n,t,i,j,pos,p,k;
     int A[1000];
     int ban;
     char letra;
     string sss;
     int ini,fin;
    long long int num;
   // string letra;
	 //string name[2000];
	 
	string resp;
	 string alien,ss,tt;
	 char c;
	 int nume;
	 
    freopen("tidy.in","r",stdin);
    freopen("tidy.out","w",stdout);
    I=1;
    //scanf("%d", &IT); 
    cin>>IT;
    //IT=1;
    while(I<=IT){
       
       cin>>alien;//>>//ss>>tt;
       a=alien.length();
       //n=ss.length();
       //t=tt.length();
     //  cout<<"alien:"<<alien;
       
       
       //pos=ss.find(alien[0]);
       //cout<<"pos: "<<pos<<endl;
       i=0;
       ini=0;
       //num=ss.find(alien[0]);
       ban=1;
       printf("Case #%d: ",I);
       while(i<a-1 && ban){
          //num=num*n+ss.find(alien[i]);;
          if(alien[i]<alien[i+1])          {
             //na                       da
              i++;
          }
          else{
             ini=i;
             ban=0;
          }
          
          
          /*
          c=alien[i];
          printf("%c%c",c,c);*/
          
         
       
       }
       ban=1;
       while(i<a-1 && ban){
          if(alien[i]>alien[i+1])          {
            fin=i;
            ban=0;
          }
          i++;
       }
       
       if(ban==1) {
       // printf("%s",alien);
           j=0;
            while(j<a){
               cout<<alien[j];
               j++;
            }
       }
       else{
//          printf("ini:%d, fin: %d",ini,fin);//*/
            j=0;
            
            
            while(j<ini){
               cout<<alien[j];
               j++;
            }
            //-; 
           // cout<<"--"<<alien[j];
            nume=int(alien[j]-48);
            nume=nume-1;
            if(nume==0 && j==0){
            }
            else{
             cout<<nume;
            }
            //cout<<"--"<<nume;
            //+;   
            j++;
            while(j<a){
               cout<<"9";
               j++;
            }
            
//       printf("ini:%d, fin: %d",ini,fin);//*/
       
       }
       cout<<endl;
     
       I++;
    }
  //  scanf("%d", &nada);
	return 0;
}


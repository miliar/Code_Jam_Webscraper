#include<iostream>
using namespace std;
#include<bits/stdc++.h>
#define f(i,n) for(int z=i; z<n; z++)
#define fe(i,n) for(int z=i; z<=n; z++)

long long int distance(int a[], long long int i, bool fmax){
    long long int LS=0,RS=0,j=i;
    j--;
    while(a[j]!=1){
        LS++;
        j--;
    }
    i++;
    while(a[i]!=1){
        RS++;
        i++;
    }
    if(fmax)
    return max(RS,LS);
    else return min(RS,LS);
}

int main()
{ int T;


 cin>>T;


 for(int z=0;z<T;z++){
      long long int L, lol;
      long long int nah,kah,n,k;
    
     cin>>L;
     cin>>lol;
 
     k=lol;
    n=L+2;
     
     int arr[n];
     
     for(int i=0;i<n;i++){
         
         arr[i]=0;
         //cout<<"g";
     }
     
     arr[0]=1;
     arr[n-1]=1;
     long long int tempInd;
     for(int t=1;t<=k;t++){
     	
         long long int max=-1,min=-1, disMin=-1, disMax=-1, index=-1;
     for(int x=1;x<=L ;x++){
     	
         if(arr[x]==1)continue;
         disMin=distance(arr,x, false);
      if(disMin>min){
          min=disMin;
          index=x;
      }   
     if(disMin==min){
          disMax=distance(arr,x, true);
         max=distance(arr,index, true);
          if(disMax>max){
              max=disMax;
              index=x;}
         
      }    
        
     }
     tempInd=index;
     arr[index]=1;
          //cout<<max<<" "<<min<<endl;
     }
     cout<<distance(arr,tempInd, true)<<" "<<distance(arr,tempInd, false)<<endl;
 }
     
    
	return 0;
}
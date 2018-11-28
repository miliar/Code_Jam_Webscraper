#include<iostream>
using namespace std;

int main()
{  
	int t;
	cin>>t;
for(int k=1;k<=t;k++){	
	long long int n; 
    cin>>n;
    long int a[1000],b[1000];
    for(int i=n;i>=1;i--){
    long int q=i,r;
    int j=0,flag=0;
    while(q!=0)
     {
         r=q%10;
         a[j]=r;
         b[j]=r;
         j++;
         q=q/10;
     }
     sort(a,a+j);
   
    for(int m=0,p=j-1;m<j,p>=0;m++,p--){
      	if(a[m]!=b[p]){
            flag=1;
            break;
     	}
     }
    if(flag==0){
      cout<<"Case #"<<k<<": "<<i<<"\n";  	
      break; 
    }
    //cout<<"---";  
   }
}
return 0;
} 
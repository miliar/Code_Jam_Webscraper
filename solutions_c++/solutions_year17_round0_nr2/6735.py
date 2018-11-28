#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
   long t,k,i,j=1;
    cin>>t;
    while(j<=t){
        long n;
        cin>>n;
        vector<long>a;
        while(n>0){
            a.push_back(n%10);
            n/=10;
        }
        for(i=0;i<a.size()-1;i++){
            if(a[i+1]>a[i]){
                for(k=i;k>=0;k--)
                    a[k]=9;
                a[i+1]-=1;
            }
            else if(a[i+1]==0 && a[i]==0){
                if(i==0){
                    a[i]=9; a[i+1]=9;}
                else{
                a[i]=a[i-1];
                    a[i+1]=a[i-1];}
            }
            
        }
        printf("Case #%ld: ",j);
        for(i=a.size()-1;i>=0;i--){
            if(a[i]!=0)
                printf("%ld",a[i]);
    }    
        
            
        
        cout<<endl;
        j++;
    }
    return 0;
}
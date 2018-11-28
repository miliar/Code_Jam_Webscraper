#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("codejamin.txt","r",stdin);
    freopen("codejamout.txt","w",stdout);
   long long n,arr[100000],j,k,arr1[100000],ck,m,T,cs=1;
   cin>>T;
   while(T--){
        cin>>n;
   while(1){
        k=0,j=0,ck=1,m=n;
       while(n>0)
       {
           arr[j++]=n%10;
           n=n/10;
       }
       for(long long i=j-1 ; i>=0 ; i--)
        arr1[k++]=arr[i];

       for(long long i=0 ; i<k-1 ; i++){
            if(arr1[i]<=arr1[i+1])
            continue;
           else{
            ck=0;
            break;
      }
   }
   if(ck==0)
    n=m-1;
   else
    break;
   }
   cout<<"Case #"<<cs++<<": "<<m<<endl;
   }

    return 0;
}

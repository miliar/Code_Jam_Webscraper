#include<bits/stdc++.h>
using namespace std;

long long int check(long long int x){
    int nod=0;
    long long int num=x;
    while(num>0){
        nod++;
        num/=10;
    }
    num=x;
    int arr[nod];
    for(int i=nod-1;i>=0;i--){
        arr[i]=num%10;
        num/=10;
    }
    for(int i=0;i<nod-1;i++){
        if(arr[i]>arr[i+1]){
            for(int j=i+1;j<nod;j++){
                arr[j]=9;
            }
            arr[i]--;
            i=-1;
        }
    }
    long long int ans=0;
    for(int i=0;i<nod;i++){
        ans+=arr[i];
        ans*=10;
    }
    return ans/10;
}

void open(){ freopen("input.txt","r",stdin);
				freopen("output.txt","w",stdout);}

int main(){
  open();
  long long int T,N;
  scanf("%lld",&T);
  for(int i=1;i<=T;i++){
     scanf("%lld",&N);
     long long int ans=check(N);
     printf("Case #%d: %lld\n",i,ans);
  }
  return 0;
}

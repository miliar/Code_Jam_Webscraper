#include<bits/stdc++.h>
#include <iostream>
using namespace std;
const int INF = 20000000;
#define FOR(i,n) for(int i=0,_n=n; i<_n; ++i)

int flips(int a[], int n, int k,int want){
  int s[n]; FOR(i,n) s[i]=0;
  int sum=0, ans=0;
  FOR(i,n){
    s[i]=(a[i]+sum)%2!=want;
    sum+=s[i]-(i>=k-1?s[i-k+1]:0);
    ans+=s[i];
    if(i>n-k and s[i]!=0) return INF;
  }
  return ans;
}

int main() {
freopen("A-large.in","r",stdin);
freopen("A_large_output_file_name.out","w",stdout);

  int t;
  scanf("%d",&t);
  for(int x=1;x<=t;x++){
    char arr1[1001];
    int n,k,arr2[1001];
    cin>>arr1>>k;
    n=strlen(arr1);
    for(int i=0;i<strlen(arr1);i++){
        if(arr1[i]=='+')
            arr2[i]=1;
        else arr2[i]=0;
    }
    int limit=flips(arr2,n,k,1);
    if(limit!=20000000)
        cout<<"Case #"<<x<<": "<<limit<<endl;
    else cout<<"Case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
  }
}

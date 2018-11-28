#include<bits/stdc++.h>
using namespace std;

void open(){ freopen("input.txt","r",stdin);
				freopen("output.txt","w",stdout);}

int main(){
   open();
   long long int T,K;
   string str;
   scanf("%lld",&T);
   for(int t=1;t<=T;t++){
      cin>>str>>K;
      int len=str.length();
      char arr[len];
      for(int i=0;i<len;i++){
        arr[i]=str.at(i);
      }
       int ans=0;
       for(int i=0;i<=len-K;i++){
          if(arr[i]=='-'){
            ans++;
            for(int j=i;j<i+K;j++){
                if(arr[j]=='-')arr[j]='+';
                else arr[j]='-';
            }
          }
       }
       int flag=0;
       for(int i=len-1;i>=0;i--){
        if(arr[i]=='-'){
            printf("Case #%d: IMPOSSIBLE\n",t);
            flag=1;
            break;
        }
       }
       if(flag==0){
          printf("Case #%d: %d\n",t,ans);
       }
   }
   return 0;
}

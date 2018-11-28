#include<bits/stdc++.h>

using namespace std;

int deepu[1001];

void solve(int num){
    int n=num;
   int last=10000;
   while(n!=0){
       int r=n%10;
       if(r>last)
          break;
       last=r;
       n=n/10;
   }
   if(n==0) deepu[num]=1;
return;
}

int main(){
freopen("input.in","r",stdin);
freopen("output.out","w",stdout);
  int i;
  for(i=0;i<=1000;i++)

    solve(i);
  int test;

  int l=1;

  cin >> test;
  while(test--){
    int xwer;
    cin >> xwer;
    do{
        if(deepu[xwer]==1){

            printf("Case #%d: %d\n",l,xwer);

        break;}

    }while(xwer--);


   l++;
  }
}

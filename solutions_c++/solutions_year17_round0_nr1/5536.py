#include <bits/stdc++.h>
using namespace std;
void Solve();
int main(){
    //  freopen("input.txt","r",stdin);
    //  freopen("output.txt","w",stdout);
    int t; cin>>t;
    for(int i=1;i<=t;i++){
      cout<<"Case #"<<i<<": ";
      Solve();
    }
    return 0;
}

void Solve(){
    int K;string str;
    bool allNeg=true,allPos=true;
    cin>>str>>K;
    for(int i=0;i<str.length();i++){
            if(str[i]=='+') allNeg = false;
            if(str[i]=='-') allPos = false;
     }

    if(allPos){cout<<"0\n";return;}
    if(allNeg and str.length()%K==0){cout<<str.length()/K<<"\n";return;}
    if(allNeg and str.length()%K){cout<<"IMPOSSIBLE\n";return;}


    int low = 0;
    int high = str.length()-1;
    while(str[low]=='+') low++;
    while(str[high]=='+') high--;

    int res=0,nlow=low,nhigh=high,neg=0;
    for(int i=low;i<=high;i++){
        if(str[i]=='+') break;
        else neg++;
        if(neg==K){
            res++;
            neg=0;
            nlow = i+1;
        }
    }
    // cout<<nlow<<" ";
    neg = 0;

    for(int i=high;i>=nlow;i--){
        if(str[i]=='+') break;
        else neg++;
        if(neg==K){
            res++;
            neg=0;
            nhigh = i-1;
        }
    }
    //    cout<<nhigh<<"\n";

   while(str[nlow]=='+') nlow++;
   while(str[nhigh]=='+') nhigh--;
//    cout<<nlow<<" "<<nhigh<<"\n";

   for(int i=nlow;i<=(nhigh-K+1);i++){     
    //    cout<<" before i="<<i<<" target string is "<<str<<endl ;
      if(str[i]=='-'){
          for(int j=i;j<i+K;j++){
              if(str[j]=='-') str[j]='+';
              else str[j]='-';
          }
          res++;
       }                 
        // cout<<" upto i="<<i<<" target string is "<<str<<endl ;
   }
   //cout<<str<<"\n";

   allPos = true;
   for(int i=nlow;i<=nhigh;i++){
       if(str[i]=='-'){allPos = false;break;}
   }
   if(allPos){
       cout<<res<<"\n";
   }
   else{
       cout<<"IMPOSSIBLE\n";
   }

}
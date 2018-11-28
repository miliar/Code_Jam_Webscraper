#include<bits/stdc++.h>
using namespace std;
int t_cases;
bool check(string s){
 for(int i=0; i<s.length(); i++){
  if(s[i]=='-') return false;
 }
 return true;
}

void flip(string s, int k){
 string s1=s;
 int n=s.length();
 int i=0,flips=0;
 bool flag=false;
 while(i<=n-k){



   if(s[i]=='-'){

    for(int j=i; j<i+k; j++) s[j]=(s[j]=='-')?'+':'-';
    flips++; //flip pancake
   }
   if(check(s)){
   flag=true;
   break;
  }

  i++;
 }
 if(!flag){
  cout<<"Case #"<<t_cases<<": IMPOSSIBLE"<<endl;
 }
 else{
  cout<<"Case #"<<t_cases<<": "<<flips<<endl;
 }
}

int main(){
int t_case;
 cin>>t_case;
 string s; int k;
 for(t_cases=1; t_cases<=t_case; t_cases++){
  cin>>s>>k;
  flip(s,k);
 }
 return 0;
}

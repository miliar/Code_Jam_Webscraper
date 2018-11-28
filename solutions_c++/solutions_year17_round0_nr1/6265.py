#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<cstring>
using namespace std;
typedef vector<int> vi;
void flip(int *a,int start,int end){
  for(int i=start;i<end;i++)
    a[i]=a[i]^1;
}
int main(){
  int TC;
  cin>>TC;
  for(int t_i=0;t_i<TC;t_i++){
    string s;
    int k;
    cin>>s;
    cin>>k;
    int n=s.size();
    int a[n];
    for(int i=0;i<s.size();i++){
      if(s[i]=='-')
        a[i]=0;
      else
        a[i]=1;
    }
    int m=0;
    for(int i=0;i<=(n-k);i++){
      if(!a[i]){
        flip(a,i,i+k);
        m++;
      }
    }
    bool correct=true;
    for(int i=n-k;i<n;i++){
      if(!a[i]){
        correct=false;
        break;}
  }
    if(correct){
      printf("Case %c%d: %d\n",'#',t_i+1,m);

    }
    else{
      printf("Case %c%d: IMPOSSIBLE\n",'#',t_i+1);
    }
  }
  return 0;
}

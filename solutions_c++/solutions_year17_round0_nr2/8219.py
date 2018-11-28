#include <bits/stdc++.h>

using namespace std;

int check(string n){
  for(int i=1;i<n.size();i++){
    if(n[i]<n[i-1]){
      return i;
    }
  }
  return 100;
}

string OwO(string n){
  for(int i; i != 100;){
    i=check(n);
    for(int k=i;k<n.size();k++){
      n[k]='9';
    }
    n[i-1]--;
  }

  while(n[0]=='0'){
    n.erase(0,1);
  }

  return n;
}
int main(){
  freopen("B-large.in", "r", stdin);
  freopen("output.out", "w", stdout);
  int t;
  string n;
  scanf("%d",&t);
  for(int i=1;i<=t;i++){
    cin>>n;
    cout<<"Case #"<<i<<": "<<OwO(n)<<endl;
  }
  return 0;
}
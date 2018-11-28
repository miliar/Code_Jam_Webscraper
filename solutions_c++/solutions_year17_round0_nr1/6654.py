#include "bits/stdc++.h"
using namespace std;
 
#define ll long long

void toogle(char &c){
  if(c=='-') c='+';
  else c = '-';
}

bool ok(string &s){
  for(int i=0;i<s.length();i++)
    if(s[i]=='-') return false;
  return true;
}

int main(int argc, char const *argv[])
{
  // freopen("input.txt","r",stdin);
  // freopen("output.txt","w",stdout);
  int t,tt=0; cin >> t;
  while(t--){
    tt++;
    string s1,s2;
    int k;
    cin >> s1 >> k;
    int l = s1.length();
    s2=s1;
    for(int i=l-1;i>=0;i--) s2[l-1-i] = s1[i];

    int ans1=0,ans2=0;
    for(int i=0;i<l;i++){
      if(s1[i]=='-' and i+k<=l){
        ans1++;
        for(int j=i;j<i+k;j++)
          toogle(s1[j]);
      }
    }
    for(int i=0;i<l;i++){
      if(s2[i]=='-' and i+k<=l){
        ans2++;
        for(int j=i;j<i+k;j++)
          toogle(s2[j]);
      }
    }

    if(!ok(s1)) ans1=l+1;
    if(!ok(s2)) ans2=l+1;

    if(ans1!=l+1 or ans2!=l+1){
       printf("Case #%d: %d\n",tt,min(ans1,ans2));
    }
    else{
      printf("Case #%d: IMPOSSIBLE\n",tt);
    }

  }
  return 0;
}

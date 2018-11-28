#include <bits/stdc++.h>
#define op(a) "Case #"<<a<<": "
#define ll long long
using namespace std;
bool check(string s){
  string ns=s;
  sort(ns.begin(), ns.end());
  if(ns==s) return 1;
  return 0;
}
string fn(string s){
  ll n=s.length();
  string ss=s;
  //if(check(s)) return s;
  while(!check(s)){
   for(int i=0;i<n;i++){
    if(s[i]<s[i-1]){
      s[i-1]--;
      while(i<n){
       s[i]='9';i++;
      }
    }
   }
 }
 for(int i=0;i<n;){
  if(s[i]=='0') i++;
    else {s=s.substr(i,n-i+1);     break;}
 }
 return s;
}
int main(int argc, char const *argv[])
{
	ifstream fin("B-large.in");
    ofstream fout("B-large.out");
     int No_testCase; fin>>No_testCase;
  
    for(int test_id=1;test_id<=No_testCase;test_id++){    
       string s; 
       fin>>s;
       fout<<"Case #"<<test_id<<": "<<fn(s)<<endl;;
   }
	return 0;
}
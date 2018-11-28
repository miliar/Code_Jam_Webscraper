#include<bits/stdc++.h>
typedef long long ll;
using namespace std;

string filter(string str) {
  ll len = str.length();
  int first = str[0] - '0';
  //cout<<str<<" len "<<len<<endl;
  for(ll i=1;i<len;i++) {
    int curr = str[i] - '0';
    // cout<<"curr "<<curr<<" first "<<first<<endl;
    if(curr < first) {
      string subs = str.substr(0, i);

      //cout<<subs<<" earlier"<<endl;
      ll val = std::stoll (subs,NULL,10);
      subs = to_string (val - 1);
      //cout<<"val "<<val<<" subs "<<subs<<endl;
      str.replace(0,subs.length(),subs);
      for(ll j=i;j<len;j++) {
      	str[j] = '9';
      }
      //cout<<"STR "<<str<<endl;
      return str;
    }
    first = curr;
  }
  return str;
}

int main() {
  ll t;
  ios::sync_with_stdio(false);
  cin>>t;
  for(ll i=1;i<=t;i++) {
    string str;
    cin>>str;
    string str2 = filter(str);
    while(str2!=str) {
    	str = filter(str2);
    	string tmp =str2;
    	str2 = str;
    	str = tmp;
    }
    ll val = std::stoll (str,NULL,10);
    cout<<"Case #"<<i<<": "<<val<<endl;
  }
  return 0;
}

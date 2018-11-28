#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>


#define MOD 1000000007
#define ll long long
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pll pair<long long,long long>
#define PI 3.14159

using namespace std;

int main() {
	// your code goes here
	ll t;
	scanf("%lld",&t);
    for(ll q=1;q<=t;q++){
	  string s;
	  ll k;
	  cin>>s>>k;
	  ll c=0;
	  for(ll i=0;i<s.size()-k+1;i++){
	      if(s[i]=='-'){
	          c++;
	          for(ll j=i;j<i+k;j++){
	              if(s[j]=='-'){
	                  s[j]='+';
	              }else{
	                  s[j]='-';
	              }
	          }
	      }
	  }
	  ll flag=0;
	  for(ll i=0;i<s.size();i++){
	      if(s[i]=='-'){
	          flag=1;
	          break;
	      }
	  }
	  if(flag==0){
	      printf("Case #%lld: %lld\n",q,c);
	  }else{
	      printf("Case #%lld: IMPOSSIBLE\n",q);
	  }
	}
	return 0;
}

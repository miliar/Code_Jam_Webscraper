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
    for(ll k=1;k<=t;k++)
	{
	 string s;
	 cin>>s;
	
     ll mini=9;
     ll b=1;
     ll ans=0;
     for(ll i=s.size()-1;i>=0;i--){
         string c="";
         c+=s[i];
         ll val=stoi(c);
         if(mini>=val){
            mini=val; 
            ans+=b*val;
         }else{
             mini=val-1;
             ans=b-1+(val-1)*b;
         }
         b*=10;
     }
     printf("Case #%lld: %lld\n",k,ans);
	}
	return 0;
}

#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <time.h>
#include <string.h>
#include <queue>
#include <stack>
#include <cstring>
using namespace std;
#define MOD 1000000007
#define ll long long int
#define rep(i,a,b) for(int (i) = (a) ; (i) <= (b) ; (i)++)
#define per(i , a , b) for(int (i) = (a) ; (i) >= (b) ; (i)--)

ll exp(ll t,ll x){if(x==0) return 1;if(x==1) return t;if(x%2==1) return (t*exp((t*t)%MOD,x/2))%MOD;if(x%2==0) return exp((t*t)%MOD,x/2);} 
ll gcd(ll x,ll y){return x%y==0?y:gcd(y,x%y);}
ll lcm(ll x,ll y){return x*(y/gcd(x,y));}
bool isprime(ll x){for(ll i=2;i*i<=x;i++){if(x%i==0){return false;}}return true;}

char inpt[100];
int main(){
  freopen("output.txt","w",stdout);
  freopen("B.in","r",stdin);
  int t;
  cin>>t;
  rep(i,1,t){
	cin>>inpt;
	int l=strlen(inpt);
	rep(j,0,l-2){
	    if (inpt[j]<=inpt[j+1])continue;
	    inpt[j]--;
	    rep(k,j+1,l-1)inpt[k]='9';
            per(k,j,1){
		if (inpt[k]<'0'||inpt[k-1]>inpt[k]){
		     inpt[k]='9';
		     inpt[k-1]--;
		}else break;
	    }
	    break;
	}
        printf("Case #%d: ",i);
        if (l==1||inpt[0]>'0')cout<<inpt[0];
        rep(j,1,l-1)cout<<inpt[j];
	cout<<endl;
  }
  return 0;
}

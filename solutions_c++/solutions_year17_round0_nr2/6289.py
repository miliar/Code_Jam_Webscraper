/// i am on fire
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <string.h>

using namespace std;

const int N=200005;
const int M=5005;

typedef long long ll;
typedef pair<ll,ll>ii;
typedef pair<int,ii>jj;

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }

bool is(int a){
 vector<int>v;
 while(a){
    v.push_back(a%10);
    a/=10;
 }
 int prev=9;
 for(int i=0;i<v.size();i++){
    if(v[i]>prev)
        return 0;
    prev=v[i];
 }
 return 1;
}
int main(){

   freopen("test.in","r",stdin);
   freopen("A.out","w",stdout);;
   int t,i=1;
   scanf("%d",&t);
   while(t--){
      int n;
      cin>>n;
      for(int j=n;j>=0;j--){
        if(is(j)){
           n=j;
           break;
        }
      }
      printf("Case #%d: %d\n",i,n);
      i++;
   }
   return 0;
}

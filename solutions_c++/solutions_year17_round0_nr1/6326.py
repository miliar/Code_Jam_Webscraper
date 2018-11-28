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

int arr[M];
int get(char a){
 if(a=='+')return 0;
 return 1;
}
int main(){

   freopen("test.in","r",stdin);
   freopen("A.out","w",stdout);;
   int t,i=1;
   scanf("%d",&t);
   while(t--){
      string s;
      int k,sum=0;
      cin>>s>>k;
      memset(arr,0,sizeof(arr));
      int cur=0,sz=s.length();
      bool ok=1;
      for(int i=0;i<sz;i++){
        cur+=arr[i];
        if(i+k<=sz){
           int state=(get(s[i])+cur)%2;
           if(state){
             sum++;
             cur++;
             arr[i+k]=-1;
           }
        }
        else{
            int state=(get(s[i])+cur)%2;
            if(state)
                ok=0;
        }
      }
      if(ok)printf("Case #%d: %d\n",i,sum);
      else printf("Case #%d: IMPOSSIBLE\n",i);
      i++;
   }
   return 0;
}

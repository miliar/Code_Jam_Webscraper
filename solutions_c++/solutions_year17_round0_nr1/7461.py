#include <stdio.h>
#include <vector>  
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <map>
#include <cstring> 
#include <queue>   
#include <list>


#define pb push_back
#define pp pop_back
#define sz(a) (int)(a.size())
#define mp make_pair
#define F first
#define S second
#define next _next
#define prev _prev
#define left _left
#define right _right
#define y1 _y1
#define all(x) x.begin(), x.end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin();i!=(c).end();i++)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = (int)1e5 + 123;
const ll INF = (ll)1e18 + 123;
const int inf = (int)1e9 + 123;
const int MOD = (int)1e9 + 7;


int main() {
  char s[1005];
  int t,c=1;
  scanf("%d",&t);
  while(t--) {
    int k,n=0;
    scanf("%s",s);
    scanf("%d",&k);
    int arr[1005];
    for(int i=0;s[i]!='\0';i++) {
      arr[i]=(s[i]=='+');
      n++;
    }
    int ans=0;
    for(int i=0;i<=n-k;i++) {
      if(arr[i]==0) {
        ans++;
        for(int j=i;j-i<k;j++) {
          arr[j]=1-arr[j];
        }
      }
    }

    for(int i=0;i<n;i++) {
      if(arr[i]==0) {
        ans=-1;
        break;
      }
    }
    printf("Case #%d: ",c++);
    if(ans<0) printf("IMPOSSIBLE\n");
    else printf("%d\n",ans);
  }
  return 0;
}
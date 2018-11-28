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
typedef pair<int,ii>node;

int gcd(int a, int b) { return b == 0 ? a : gcd(b, a % b); }
ll lcm(ll a, ll b) { return a * (b / gcd(a, b)); }


int main(){

   freopen("test.in","r",stdin);
   freopen("A.out","w",stdout);;
   int t,i=1;
   scanf("%d",&t);
   while(t--){
      int n,k;
      cin>>n>>k;
      set<node>st;
      st.insert(node(-n,ii(1,n)));
      for(int i=1;i<k;i++){
        node cur=*st.begin();
        cur.first*=-1;
        st.erase(st.begin());
            int taken=cur.second.first+(cur.first-1)/2;
            int a=cur.second.first,b=taken-1,x=taken+1,y=cur.second.second;
            if(b-a+1>0){
                st.insert(node(-(b-a+1),ii(a,b)));
            }
            if(y-x+1>0){
                st.insert(node(-(y-x+1),ii(x,y)));
            }
      }
      if(st.empty()){
         printf("Case #%d: 0 0\n",i);
      }
      else{
        node cur=*st.begin();
        cur.first*=-1;
        int mx=cur.first/2,mn=(cur.first-1)/2;
        printf("Case #%d: %d %d\n",i,mx,mn);
      }
      i++;
   }
   return 0;
}

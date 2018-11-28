#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

#define sc(x) scanf("%d",&x)
#define scll(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x)
#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define clr(a,v) memset(a,v,sizeof a)

#define N 1123
int t;
ll n,k,mini,maxi,q;


int main(){
    sc(t);
    fre(ca,1,t){
      printf("Case #%d: ",ca);
      scll(n), scll(k);

      map<ll,ll> m;
      set<ll> has;
      priority_queue<ll> pq;
      pq.push(n);
      m[n] = 1;
      ll look;
      int cnt = 0;
      while (k > 0){
        //cnt++;
        look = pq.top();
        pq.pop();

        q = m[look];
        if (!q) continue;
        //printf("k:%lld look:%lld q:%lld\n",k,look,q);
        k -= q;
        m[look] = 0;
        has.erase(look);

        maxi = look/2;
        mini = (look-1)/2;
        if (has.find(maxi) == has.end()){
            pq.push(maxi);
            has.insert(maxi);
            m[maxi] = q;
        } else {
            m[maxi] += q;
        }

        if (has.find(mini) == has.end()){
            pq.push(mini);
            has.insert(mini);
            m[mini] = q;
        } else {
          m[mini] += q;
        }
        //printf("m[%lld]:%lld m[%lld]:%lld\n",maxi,m[maxi],mini,m[mini]);
      }

      printf("%lld %lld\n", maxi, mini);

    }
    return 0;
}

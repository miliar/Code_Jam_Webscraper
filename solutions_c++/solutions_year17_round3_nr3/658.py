#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int> ii;
typedef pair<int,int> dd;

#define sc(x) scanf("%d",&x)
#define scs(x) scanf("%s",x)
#define fr(i,a,b) for(int i = a; i < b; i++)
#define fre(i,a,b) for(int i = a; i <= b; i++)
#define clr(a,v) memset(a,v,sizeof a)
#define F first
#define S second

#define N 112
int t,n,k;
double u,ans;
double P[N];

int main(){
    sc(t);
    fre(ca,1,t){
      printf("Case #%d: ",ca);
      sc(n), sc(k);
      scanf("%lf",&u);
      fr(i,0,n) scanf("%lf",&P[i]);


      priority_queue<double> pq;
      fr(i,0,n) pq.push(-P[i]);
      double now, next, dif;
      int q;

      int z = 0;
      while (u > 0){
        now = pq.top();
        if (now == -1) break;
        pq.pop();
        q = 1;

        while (pq.size() && pq.top() == now){
          pq.pop();
          q++;
        }

        if (pq.size()) next = pq.top();
        else next = -1;

        //printf("u:%lf now:%lf q:%d next:%lf\n",u,now,q,next);

        dif = now - next; // negatives
        dif = min(dif*q, u);
        now -= dif/q;
        u -= dif;

        fr(i,0,q) pq.push(now);
      }
      ans = 1;

      while (pq.size()){
        ans *= -pq.top();
        pq.pop();
      }

      printf("%.6lf\n",ans);

    }
    return 0;
}

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <iterator>
#include <string>
#include <vector>
#include <cstring>
using namespace std;

typedef long long LL;

#define FOR(v,p,k) for(int v=p;v<=k;++v)
#define FORD(v,p,k) for(int v=p;v>=k;--v)
#define FORL(v,p,k) for(int v=p;v<k;++v)
#define REP(i,n) for(int i=0;i<(n);++i)
#define VAR(v,i) __typeof(i) v=(i)
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define SIZE(x) (int)x.size()
#define ALL(c) c.begin(),c.end()

int main(){
 int te;
 char t[1000];
 scanf("%d",&te);
 FOR(ii, 1, te){
   scanf("%s", t);
   int n = strlen(t);
   FORD(i, n-2, 0) if (t[i] > t[i+1]){
     t[i]--;
     FOR(j, i+1, n-1)
       t[j] = '9';
   }
   int a = 0;
   while (t[a] == '0') ++a;
   printf("Case #%d: %s\n", ii, t+a);
 }
  return 0;
}

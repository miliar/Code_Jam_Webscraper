#include <iostream>
#include <algorithm>
#include <fstream>
#define f(i,a,b) for(int i=a; i<=b; i++)

using namespace std;
const int MAXPT=(int)(5e6+1);


long long s,items[MAXPT],n;
int nitems,t;
void backtrack(int i, int pre) {
   if (i>18) return;
   f(j,pre,9) {
       s=s*10+j;
       nitems++;
       items[nitems]=s;
       backtrack(i+1,j);
       s=s/10;
   }
}

long long Find(long long gt) {
  int dau=1, cuoi=nitems, giua;
  long long res;
  while (dau<=cuoi) {
    giua=(dau+cuoi)/2;
    if (items[giua]<=gt) {
            res=items[giua]; dau=giua+1;
    }    else cuoi=giua-1;
  }
  return res;
}

int main() {
   ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
   nitems=0;
   s=0;
   backtrack(1,1);
   sort(items+1,items+nitems+1);
   freopen("B-large.in","r",stdin);
   freopen("B-large.out","w",stdout);
   cin >> t;
   f(i,1,t) {
      cin >> n;
      cout << "Case #" << i << ": " << Find(n) << endl;
   }
}

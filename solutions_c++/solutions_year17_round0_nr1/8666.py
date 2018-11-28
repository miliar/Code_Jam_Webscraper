#include <bits/stdc++.h>
using namespace std;

const int INF = INT_MAX;
const int N = 1010;
int a[N];

int solve(int bits[], int N,int sz)
{
  queue<int> flips;
  int moves = 0;

  for (int i = 0; i < sz; ++i)
  {
    if (!flips.empty() && flips.front() <= i - N)
      flips.pop();

    if ((bits[i] ^ (flips.size() % 2 == 0)) == 1)
    {
      if (i > sz - N)
        return -1;
      moves++;
      flips.push(i);
    } 
  }

  return moves;
}

int main() {
   int t,k;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        printf("Case #%d: ",tt);
        string str;
        cin>>str;
        scanf("%d",&k);
        for(int i=0;i<str.size();i++){
            if(str[i]=='+')
                a[i] = 1;
            else
                a[i] = 0;
        }
        int xx = solve(a,k,str.size());
        reverse(a,a+str.size());
        int yy = solve(a,k,str.size());
        if(xx==-1 && yy==-1)
           puts("IMPOSSIBLE");
        else
          printf("%d\n",min(xx,yy));
    }
    return 0;
}

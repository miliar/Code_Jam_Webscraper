#include <bits/stdc++.h>
#include<string.h>
typedef long long ll;
typedef unsigned long long ull;
using namespace std;
ll  mini(ll  a,ll  b )
{
    if(a<b)
    return a;
    else
    return b;
}
ll  max(ll  a,ll  b )
{
    if(a<b)
    return b;
    else
    return a;
}
int main() {
  freopen("C-small.in", "r", stdin);
  freopen("C-small.out", "w", stdout);
  long long int N,K,Ls,Rs,next,ans1,ans2,left,right,i;
  int tt,A[10001],T;

  cin >> T;
  for (int tt = 1; tt <= T; tt++)
  {
      ans1=0;
      ans2=0;
      Ls=0;
      Rs=0;
      left=right=0;
      cin >> N >> K;
      for(i=0;i<=N;i++)
      A[i]=0;
      A[0]=1;
      A[N+1]=1;
      Ls=0;
      Rs=N+1;
        while(K--)
        {
            next=(Ls+Rs)/2;
         //   cout << "next = " << next << endl;
            A[next]=1;
            for(i=next-1;i>=0;i--)
            {
                if(A[i]==1){
                    left=next-i-1;
                    break;
                }
            }
           // cout << "left side 1= " << left << endl;
            for(i=next+1;i<=N+1;i++)
            {
                if(A[i]==1){
                    right=i-next-1;
                    break;
                }
            }
            //cout << "right side 1= " << right << endl;
            int max=-1;
            int p=1;
            for(i=p;i<=N+1;i++)
            {
                if(A[i]==1)
                {
                    int tem=i-p;
                    if(tem>max)
                    {
                        max=tem;
                        Ls=p;
                        Rs=i;
                    }
                    p=i;
                }
              //  cout << "next maxm gap between " << Ls << "and " << Rs << endl;
            }

        }
        ans1=mini(left,right);
        ans2=max(left,right);
       printf("Case #%d: ", tt);
        cout << ans2 << " " << ans1 << endl;

  }

  return 0;
}



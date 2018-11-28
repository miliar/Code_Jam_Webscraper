#include <bits/stdc++.h>
using namespace std;                // @ Author MD. Chand Alam

typedef long long ll;
typedef unsigned long long ull;
ll  mini(ll x,ll  y )
{
    if(x<y)
    return x;
    else
    return y;
}
ll  maxi(ll x,ll  y )
{
    if(x<y)
    return y;
    else
    return x;
}

int main()
{

    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
  ll N,K,Ls,Rs,next,ans1,ans2,left,right,i;
  int tt,A[10001],t;

  cin >> t;
  for (int cs = 1; cs <= t; cs++)
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
            A[next]=1;
            for(i=next-1;i>=0;i--)
            {
                if(A[i]==1){
                    left=next-i-1;
                    break;
                }
            }
            for(i=next+1;i<=N+1;i++)
            {
                if(A[i]==1){
                    right=i-next-1;
                    break;
                }
            }

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
            }

        }
        ans1=mini(left,right);
        ans2=max(left,right);
       cout<<"Case #"<<cs<<": "<<ans2<<" "<<ans1<<endl;

  }

  return 0;
}

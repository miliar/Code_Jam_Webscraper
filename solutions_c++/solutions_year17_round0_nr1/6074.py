#include<bits/stdc++.h>
using namespace std;
char s[1005];
long long int a[1005];
int k;
int z;

/*long long int flips() {
  long long int sum=0, ans=0;
  for(int i=0;i<z;i++) {

      int p;
  if(s[i]=='-')
    p=0;
  else
    p=1;
    a[i] = (p+sum)%2 != 1;
    sum += a[i] - (i>=k-1?a[i-k+1]:0);
    ans += a[i];
    if(i>z-k and a[i]!=0) return -1;
  }

  return ans;
}*/
long long int solve()
{
  queue<long long int> flips;
  long long int moves = 0;

  for (int i = 0; i <z; ++i)
  {
    if (!flips.empty() && flips.front() <= i - k)
      flips.pop();
  int p;
  if(s[i]=='-')
    p=0;
  else
    p=1;
    if ((p ^ (flips.size() % 2 == 0)) == 1)
    {
      if (i > z- k)
        return -1; // IMPOSSIBLE

      moves++;
      flips.push(i);
    }
  }

  return moves;
}
int main()
{
    //freopen("i.in","r",stdin);
	//freopen("o.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        scanf("%s",s);
        scanf("%d",&k);
        z=strlen(s);
        //printf("*");
        long long int ans=solve();
        //printf("*");
        //printf("%lld\n",ans);
        if(ans==-1)
            printf("Case #%d: IMPOSSIBLE\n",i);
        else
            printf("Case #%d: %lld\n",i,ans);


    }
    return 0;
}

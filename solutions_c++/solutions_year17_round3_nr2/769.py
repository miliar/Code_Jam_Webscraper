#include<bits/stdc++.h>
using namespace std;

bitset<1500> isCAvailable;
bitset<1500> isJAvailable;

long long  memo1[800][1500][2];
long long  memo2[800][1500][2];
//Quota of C, elapsed minutes, turn

long long dp1(int Cquota, int currTime, int turn)
{
  long long Jquota = 720-(currTime-(720-Cquota));
  if(currTime == 1440)
  {
    if(Cquota!=0) return 99999;
    if(Jquota!=0) return 99999;
    if(turn==0) return 0;
    return 1;
  }
  if(Cquota < 0 || Jquota < 0) return 99999;
  if(memo1[Cquota][currTime][turn]!=-1) return memo1[Cquota][currTime][turn];
  int ans = 0;
  if(turn == 0 && !isCAvailable[currTime])
  {
    ans = 1 + dp1(Cquota,currTime+1,1);
  }
  else if(turn == 0 && !isJAvailable[currTime])
  {
    ans = dp1(Cquota-1,currTime+1,0);
  }

  else if(turn == 1 && !isCAvailable[currTime])
  {
    ans = dp1(Cquota,currTime+1,1);
  }
  else if(turn == 1 && !isJAvailable[currTime])
  {
    ans = 1 + dp1(Cquota-1,currTime+1,0);
  }
  else if(turn == 0)
  {
    long long  ans1 = 1 + dp1(Cquota,currTime+1,1);
    long long  ans2 = dp1(Cquota-1,currTime+1,0);
    ans = min(ans1,ans2);
  }
  else if(turn == 1)
  {
    long long  ans1 = 1 + dp1(Cquota-1,currTime+1,0);
    long long  ans2 = dp1(Cquota,currTime+1,1);
    ans = min(ans1,ans2);
  }

  return memo1[Cquota][currTime][turn] = ans;
}

long long dp2(int Cquota, int currTime, int turn)
{
  long long Jquota = 720-(currTime-(720-Cquota));
  if(currTime == 1440)
  {
    if(Cquota!=0) return 99999;
    if(Jquota!=0) return 99999;
    if(turn==1) return 0;
    return 1;
  }
  if(Cquota < 0 || Jquota < 0) return 99999;
  if(memo2[Cquota][currTime][turn]!=-1) return memo2[Cquota][currTime][turn];
  int ans = 0;
  if(turn == 0 && !isCAvailable[currTime])
  {
    ans = 1 + dp2(Cquota,currTime+1,1);
  }
  else if(turn == 0 && !isJAvailable[currTime])
  {
    ans = dp2(Cquota-1,currTime+1,0);
  }

  else if(turn == 1 && !isCAvailable[currTime])
  {
    ans = dp2(Cquota,currTime+1,1);
  }
  else if(turn == 1 && !isJAvailable[currTime])
  {
    ans = 1 + dp2(Cquota-1,currTime+1,0);
  }
  else if(turn == 0)
  {
    long long  ans1 = 1 + dp2(Cquota,currTime+1,1);
    long long  ans2 = dp2(Cquota-1,currTime+1,0);
    ans = min(ans1,ans2);
  }
  else if(turn == 1)
  {
    long long  ans1 = 1 + dp2(Cquota-1,currTime+1,0);
    long long  ans2 = dp2(Cquota,currTime+1,1);
    ans = min(ans1,ans2);
  }

  return memo2[Cquota][currTime][turn] = ans;
}

int Ac, Aj;
int main()
{
  int T; cin>>T;
  for(int tc = 0; tc<T; tc++)
  {
    isCAvailable.set();
    isJAvailable.set();

    cin>>Ac>>Aj;

    for(int i = 0; i< Ac; i++)
    {
      int Ci, Di;
      cin>>Ci>>Di;
      for(int t = Ci; t < Di; t++)
      {
        isCAvailable[t] = 0;
      }
    }

    for(int i = 0; i< Aj; i++)
    {
      int Ji, Ki;
      cin>>Ji>>Ki;
      for(int t = Ji; t < Ki; t++)
      {
        isJAvailable[t] = 0;
      }
    }

    memset(memo1,-1,sizeof memo1);
    memset(memo2,-1,sizeof memo2);

    cout<<"Case #"<<(tc+1)<<": "<<min(dp1(720,0,0),dp2(720,0,1))<<endl;
  }
}

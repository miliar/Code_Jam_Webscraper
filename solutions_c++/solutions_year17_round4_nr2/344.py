//In the Name of God
//Ya Ali

#include<bits/stdc++.h>

#define err(A) cout<<#A<<" = "<<(A)<<endl

using namespace std;

const int maxn=1024;

int n,c,m;

int mx,prm;
int tkt[maxn];
int cnt[maxn];

void reset()
{
  mx=0,prm=0;
  memset(cnt,0,sizeof cnt);
  memset(tkt,0,sizeof tkt);
}

int main()
{
  ios::sync_with_stdio(0);cin.tie(0);

  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      reset();
      
      cin>>n>>c>>m;
      for(int p,a;m--;)
	{
	  cin>>p>>a;
	  cnt[p]++;
	  tkt[a]++;
	}
      for(int i=1;i<=c;i++)
	mx=max(mx,tkt[i]);
      for(int cur=0,i=1;i<=n;i++)
	{
	  cur+=cnt[i];
	  mx=max(mx,(cur+i-1)/i);
	}
      for(int z=0,i=n;i>=1;i--)
	{
	  int me=cnt[i];
	  if(me<=mx)
	    z=max(0,z-(mx-me));
	  else
	    prm+=me-mx,z+=me-mx;
	}
      cout<<"Case #"<<t<<": "<<mx<<" "<<prm<<endl;
    }
  
  return 0;
}

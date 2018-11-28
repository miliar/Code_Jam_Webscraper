#include<bits/stdc++.h>
#define pb push_back
#define F first
#define S second
#define ll long long int
#define inf 1450000090
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define sd(x) scanf("%d",&x)
#define sd2(x,y) scanf("%d%d",&x,&y)
#define sdl(x) scanf("%lld",&x)
#define nax 100010
#define mp make_pair
#define sz(x) (int)(x.size())
#define pl pair <ll , ll>
#define pii pair < int , pair <int ,int > >
#define MOD 1000000007
using namespace std;
set< pl > sett;
set< pl > :: iterator it;
map<ll,ll> mapp;
int main(int argc, char const *argv[])
{
  freopen("input.txt","read",stdin);
  freopen("output.txt","write",stdout);
  int t;
  sd(t);
  for(int tt=1;tt<=t;tt++)
  {
  	 printf("Case #%d: ",tt);
  	 ll n,k;
  	 sdl(n);sdl(k);k--;
  	 sett.clear();
  	 mapp.clear();
  	 sett.insert(mp(-n,1));
  	 mapp[n]+=1;
  	 ll done = 0;
  	 ll ans1,ans2;
  	 while(done < k)
  	 {
  	 	pl top  = *sett.begin();
  	 	ll ff = -top.F;
  	 	ff--;
  	 	ll ss = top.S;
  	 	ll diff =k-done;
  	 	if(diff >= ss) // break all
  	 	{
  	 		sett.erase(top);
  	 		mapp[ff] = 0;
  	 		done+=ss;
  	 		ll h1 = ff/2;
  	 		ll h2 = ff/2;
  	 		if(ff%2==1)
  	 			h2++;
	  	 	if(mapp[h2] == 0)// not there
	  	 	{
	  	 		sett.insert(mp(-h2,ss));
	  	 	}
	  	 	else
	  	 	{
	  	 		ll ctr = mapp[h2];
	  	 	    sett.erase(mp(-h2,ctr));
	  			ctr+=ss;
	 			sett.insert(mp(-h2,ctr));
	  	 	}
	  	 	mapp[h2]+=ss;
			if(mapp[h1] == 0)// not there
	  	 	{
	  	 		sett.insert(mp(-h1,ss));
	  	 	}
	  	 	else
	  	 	{
	  	 		ll ctr = mapp[h1];
	  	 	    sett.erase(mp(-h1,ctr));
	  	 		ctr+=ss;
	  	 		sett.insert(mp(-h1,ctr));
	  	 	}
	  	 	mapp[h1]+=ss;
  	 	}
  	 else
  	 	{
  	 		//only some of largest numbers need to be split
  	 		// ans arrived;
  	 		// break some;
  	 		done = k;
  	 		ll maxcnt = mapp[ff];
  	 		sett.erase(mp(-ff,maxcnt));
  	 		maxcnt-=diff;
  	 		sett.insert(mp(-ff,maxcnt-diff));
  	 		ll h1 = ff/2;
  	 		ll h2 = ff/2;
  	 		if(ff%2==1)
  	 			h2++;
  	 		if(h2!=0)
	  	 	{
	  	 		if(mapp[h2] == 0)// not there
	  	 		{
	  	 			sett.insert(mp(-h2,diff));
	  	 		}
	  	 		else
	  	 		{
	  	 			ll ctr = mapp[h2];
	  	 			sett.erase(mp(-h2,ctr));
	  	 			ctr+=diff;
	  	 			sett.insert(mp(-h2,ctr));
	  	 		}
	  	 		mapp[h2]+=diff;
	  	 	}
	  	 	if(h1!=0)
	  	 	{
				if(mapp[h1] == 0)// not there
	  	 		{
	  	 			sett.insert(mp(-h1,diff));
	  	 		}
	  	 		else
	  	 		{
	  	 			ll ctr = mapp[h1];
	  	 			sett.erase(mp(-h1,ctr));
	  	 			ctr+=diff;
	  	 			sett.insert(mp(-h1,ctr));
	  	 		}
	  	 		mapp[h1]+=ss;
	  	 	}
  	 	}
  	 }
  	 ll ans = -1*sett.begin()->F;
  	 ans1 = ans2 = (ans-1)/2;
  	 if((ans-1)%2==1)
  	 	ans1++;
  	 printf("%lld %lld\n",ans1,ans2);
  }
  return 0;
}
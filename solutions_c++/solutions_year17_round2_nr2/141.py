//In the Name of God
//Ya Ali

#include<bits/stdc++.h>

#define ld long double

#define pb push_back

#define err(A) cout<<#A<<" = "<<(A)<<endl

using namespace std;

const string bad="IMPOSSIBLE";

vector<string> B,R,Y;

void reset()
{
  B.resize(0);
  R.resize(0);
  Y.resize(0);
}

void blue()
{
  cout<<B.back();
  B.pop_back();
}

void red()
{
  cout<<R.back();
  R.pop_back();
}

void yellow()
{
  cout<<Y.back();
  Y.pop_back();
}

int main()
{
  ios::sync_with_stdio(0);cin.tie(0);

  int T;
  cin>>T;
  for(int t=0;t<T;t++)
    {
      reset();

      int n;
      int r,o,y,g,b,v;
      cin>>n;
      cin>>r>>o>>y>>g>>b>>v;
      cout<<"Case #"<<t+1<<": ";
      
      if(b<=o and o)
	{
	  if(n==b+o and b==o)
	    {
	      for(int i=0;i<o;i++)
		cout<<"OB";
	      cout<<endl;
	    }
	  else
	    {
	      cout<<bad<<endl;
	    }
	  continue;
	}
      else
	{
	  b-=o;
	  for(int i=0;i<b;i++)
	    B.pb("B");
	  for(int i=0;i<o;i++)
	    B[0]+="OB";
	}

      if(r<=g and g)
	{
	  if(n==r+g and r==g)
	    {
	      for(int i=0;i<g;i++)
		cout<<"GR";
	      cout<<endl;
	    }
	  else
	    {
	      cout<<bad<<endl;
	    }
	  continue;
	}
      else
	{
	  r-=g;
	  for(int i=0;i<r;i++)
	    R.pb("R");
	  for(int i=0;i<g;i++)
	    R[0]+="GR";
	}

      if(y<=v and v)
	{
	  if(n==y+v and y==v)
	    {
	      for(int i=0;i<v;i++)
		cout<<"VY";
	      cout<<endl;
	    }
	  else
	    {
	      cout<<bad<<endl;
	    }

	  continue;
	}
      else
	{
	  y-=v;
	  for(int i=0;i<y;i++)
	    Y.pb("Y");
	  for(int i=0;i<v;i++)
	    Y[0]+="VY";
	}
	
      int mx=max(max(b,r),y);
      
      if(b==mx)
	{
	  if(y+r<b)
	    {
	      cout<<bad<<endl;
	    }
	  else
	    {
	      for(int i=1;i<=b;i++)
		{
		  blue();
		  if(i<=r)
		    red();
		  if(b-i+1<=y)
		    yellow();
		}
	      cout<<endl;
	    }
	}
      else if(r==mx)
	{
	  if(b+y<r)
	    {
	      cout<<bad<<endl;
	    }
	  else
	    {
	      for(int i=1;i<=r;i++)
		{
		  red();
		  if(i<=b)
		    blue();
		  if(r-i+1<=y)
		    yellow();
		}
	      cout<<endl;
	    }
	}
      else
	{
	  if(b+r<y)
	    cout<<bad<<endl;
	  else
	    {
	      for(int i=1;i<=y;i++)
		{
		  yellow();
		  if(i<=b)
		    blue();
		  if(y-i+1<=r)
		    red();
		}
	      cout<<endl;
	    }
	}
    }
  
  return 0;
}

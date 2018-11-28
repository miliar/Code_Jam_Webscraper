#include <bits/stdc++.h>
using namespace std;
 
#define fr(i,a,b) for(int (i)=(int) a;(i)<=(int)(b);++(i))
#define li list<int>
#define ll long long
#define mp make_pair
#define mod 1000000007
#define pb push_back
#define pi pair<int,int>
#define pr printf
#define vi vector<int>
#define vpi vector< pi > 
char s[30][30];
int r,c,i,j,f,k;
void hh(int x,int y)
{
      for(int i=0;i<r;i++)
      s[i][y]=s[i][x];
}
int main() {
	// your code goes here
      std::ios_base::sync_with_stdio(false);
      freopen("input","r",stdin);
      freopen("output","w",stdout);
      int t,tt;
      cin>>t;tt=t;
      while(t--)
      {
            cout<<"Case #"<<tt-t<<":\n";
            char ch;
            cin>>r>>c;
            for(i=0;i<r;i++)
            {
                  cin>>s[i];
                  
            }
            for(i=0;i<r;i++)
            {f=0;
                  for(j=0;j<c;j++)
                  {f=0;
                        for(k=i;k<r;k++)
                        {
                        if(s[k][j]!='?')
                        {
                              ch=s[k][j];f=1;
                              continue;
                        }
                        if(!f) continue;
                        s[k][j]=ch;
                        
                        }
                  }
            }
            for(i=r-1;i>=0;i--)
            {
                  for(j=0;j<c;j++)
                  {f=0;
                        for(k=i;k>=0;k--)
                        {
                        if(s[k][j]!='?')
                        {
                              ch=s[k][j];f=1;
                              continue;
                        }
                        if(!f) continue;
                        s[k][j]=ch;
                        
                        }
                  }
            }
            //for(i=0;i<r;i++)cout<<s[i]<<"\n";
            for(i=1;i<c;i++)
            {
                 if(s[0][i]=='?')
                 hh(i-1,i);
            }
            for(i=c-2;i>=0;i--)
            {
                  if(s[0][i]=='?')
                  hh(i+1,i);
            }
            for(i=0;i<r;i++)
            cout<<s[i]<<"\n";
      }
      
	return 0;
}


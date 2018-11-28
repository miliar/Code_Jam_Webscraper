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
char s[1010],dp[1010];
int main() {
	// your code goes here
      //std::ios_base::sync_with_stdio(false);
      int t,k,tt;
      cin>>t;tt=t;
      while(t--)
      {
          cin>>s>>k;
          int f=1,r=0,n,p=0;
          cout<<"Case #"<<tt-t<<": ";
          n=strlen(s);
          memset(dp,0,sizeof dp);
          fr(i,0,n-1)
          {
                if((s[i]=='+'&&p%2==0)||(s[i]=='-'&&p%2!=0))
                {
                      p-=dp[i];continue;
                }
                if(i+k-1>=n)
                {
                      f=0;break;
                }
                p++;
                dp[i+k-1]++;
                r++;
                p-=dp[i];
          }
          if(f)
          cout<<r<<"\n";
          else
          cout<<"IMPOSSIBLE\n";
          
      }
      
	return 0;
}


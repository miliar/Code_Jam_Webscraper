#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define mod 1000000007
using namespace std;


main()
{
freopen("B-small.in","r",stdin);
freopen( "tidy.txt", "w", stdout );

int T;
cin>>T;

for(int t=1;t<=T;t++)
{

  string A;
  cin>>A;
  int n = A.size();
  int s=-1,e=n-1;
  for(int i=1;i<n;i++)
  {
      if((A[i]-'0') < (A[i-1]-'0'))
      {
          s=i-1;
          break;
      }
  }

  if(s!=-1)
 {
  int i=e;
  while(i>s)
  {
      A[i]='9';
      i--;
  }

  if(s==0)
  {
      int num = A[s]-'0';
      if(num)
        num--;
      A[s]=num+'0';
  }


    int c=0;
  while(s!=0)
  {
      int curr = A[s]-'0';
      int prev = A[s-1]-'0';
      if( curr - 1 < prev)
      {
          A[s]='9';
          A[s-1]= prev-1 + '0';
      }
      else if(c==0)
      {
          A[s] = curr -1 + '0';
          break;
      }
      c++;
      s--;
  }


    i=0;
  for( i=0;i<n;i++)
  {
      if(A[i]!='0')
        break;
  }

  A.erase(0,i);
 }
  cout<<"Case #"<<t<<": "<<A<<"\n";
}

}

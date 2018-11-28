#include <bits/stdc++.h>
#include <iostream>
#include <bitset>

using namespace std;

#define L(i,n) for(int i=0;i<n;i++)
#define ALL(X) (X).begin(),(x).end()
#define DRC(n)  char n;scanf("%c",&n)
#define DRI(n) int n;scanf("%d",&n)
#define DR2I(n,m) int n,m;scanf("%d%d",&n,&m)
#define RI(n) scanf("%d",&n)
#define ll long long
#define pb(n) push_back(n)
#define pii pair<int,int>
#define mp(i,j) make_pair(i,j)
#define f first
#define s second
#define MAX_INT 100007
#define LEEP(i,n) for(int i=1;i<=n;i++)


int main()
{
  int t;
  ifstream ifile;
  ofstream ofile;
  ifile.open("input");
  ofile.open("Output");
  ifile>>t;
  int n,k;
  string s;
  int cnt=1;
  while(t--)
  {
      bool ans=true;
      ifile>>s>>k;
      int n=s.size();
      int arr[n+1];
      L(i,n)
      {if(s[i]=='+'){arr[i]=1;}
      else{arr[i]=0;}
      }

      int flip=0;

      L(i,n-k+1)
      {
        if(arr[i]==1){continue;}
        L(j,k)
        {
          arr[i+j]=1-arr[i+j];
        }
        flip++;
      }
      // L(i,n)
      // {cout<<arr[i]<<" ";}
      // cout<<endl;

      L(i,n)
      {if(arr[i]!=1){ans=false;break;}}

      ofile<<"Case #"<<cnt<<": ";
      if(!ans){ofile<<"IMPOSSIBLE";}
      else
      {ofile<<flip;}
      ofile<<endl;
      cnt++;
  }
  ofile.close();
  ifile.close();
}

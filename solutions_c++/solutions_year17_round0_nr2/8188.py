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
#define MAX_INT 10000007
#define LEEP(i,n) for(int i=1;i<=n;i++)


int main()
{
  ll t;
  ifstream ifile;
  ofstream ofile;
  ifile.open("input");
  ofile.open("Output");
  ifile>>t;
  ll cnt=1,n;

  while(t--)
  {
      ll num,temp,digits=0;
      ifile>>n;
      temp=n;
      std::vector<int> v;
      stack<int> st;
      while(temp!=0)
      {
        digits++;
        st.push(temp%10);
        temp/=10;
      }

    while(!st.empty()){
      v.pb(st.top());
      st.pop();
    }

    int index=-1;
    int count=1;
    LEEP(i,digits-1)
    {if(v[i]>v[i-1]){count=1;continue;}
    else if(v[i]==v[i-1]){count++;continue;}

    else{
        L(j,count)
        {v[i-1-j]--;}

        index=i-count;
        break;
    }
    }
    if(index!=-1)
    {for(int i=index+1;i<digits;i++)
      {v[i]=9;}}

      ofile<<"Case #"<<cnt<<": ";
      bool start=false;
      L(i,digits){
        if(v[i]!=0){start=true;}
        if(start){ofile<<v[i];}
      }
      ofile<<endl;
      cnt++;
  }
  ofile.close();
  ifile.close();
}

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
      int r,c;
      ifile>>r>>c;
      pair<char,char> mat[r+1][c+1];
      L(i,r)
      {
        string s;
        ifile>>s;
        char temp='?';
        L(j,c)
        {
          mat[i][j].f=s[j];
          if(s[j]!='?')
          {
            mat[i][j].s=s[j];
            temp=s[j];
          }
          else
          {
              mat[i][j].s=temp;
          }
        }
      }

      char first[r+1];
      fill(first,first+r,'?');

      L(i,r)
      {
        L(j,c)
        {
          if(mat[i][j].f=='?'){continue;}
          else
          {
            first[i]=mat[i][j].f;
            break;
          }
        }
      }
      L(i,r)
      {
        L(j,c)
        {
          if(first[i]=='?'){break;}
          else
          {
            if(mat[i][j].s=='?')
              {mat[i][j].s=first[i]; }
          }
        }
      }

      L(j,c)
      {
        char temp='?';
        L(i,r)
        {
          if(mat[i][j].s!='?')
          {
            temp=mat[i][j].s;
          }
          else
          {
            mat[i][j].s=temp;
          }
        }
      }


      char f1[c+1];
      fill(f1,f1+c,'?');
      L(j,c)
      {
        L(i,r)
        {
          if(mat[i][j].s=='?'){continue;}
          else
          {
            f1[j]=mat[i][j].s;
            break;
          }
        }
      }


      L(j,c)
      {
        L(i,r)
        {
          if(mat[i][j].s=='?'){mat[i][j].s=f1[j];}
          else
          {
            break;
          }
        }
      }


      L(i,r)
      {
        L(j,c)
        {
          cout<<mat[i][j].s;
        }
        cout<<endl;
      }


      ofile<<"Case #"<<cnt<<": "<<endl;
      L(i,r)
      {
        L(j,c)
        {
          ofile<<mat[i][j].s;
        }
        ofile<<endl;
      }
      cnt++;
  }
  ofile.close();
  ifile.close();
}

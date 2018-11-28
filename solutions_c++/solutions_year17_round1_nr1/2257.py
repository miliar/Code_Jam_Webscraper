#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define mp make_pair
#define pb push_back
#define x first
#define y second
FILE *fin = freopen("in.txt","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);
int main()
{
ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int r,c;
        cin>>r>>c;
        set<char> s;
        char a[r][c];
        for(int i=0;i<r;i++)
            for(int j=0;j<c;j++)
            {
                cin>>a[i][j];
                s.insert(a[i][j]);
            }
          for(int i=0;i<r;i++)
          {
              for(int j=0;j<c;j++)
                if(a[i][j]!='?')
              {int l=j;
              l++;
                  while(a[i][l]=='?'&&l<c)
                  {
                      a[i][l]=a[i][j];
                      l++;
                  }
                  l=j;
              l--;
                  while(a[i][l]=='?'&&l>=0)
                      {
                          a[i][l]=a[i][j];
                          l--;
                      }
              }
          }
           for(int i=0;i<r;i++)
          {
              for(int j=0;j<c;j++)
                if(a[i][j]!='?')
              {int l=i;
              l++;
                  while(a[l][j]=='?'&&l<r)
                  {
                      a[l][j]=a[i][j];
                      l++;
                  }
                  l=i;
              l--;
                  while(a[l][j]=='?'&&l>=0)
                      {
                          a[l][j]=a[i][j];
                          l--;
                      }
              }
          }

          cout<<"Case #"<<k<<":\n";
          for(int i=0;i<r;i++){
            for(int j=0;j<c;j++)
            {
                cout<<a[i][j];


          }
          cout<<endl;

    }

}


}

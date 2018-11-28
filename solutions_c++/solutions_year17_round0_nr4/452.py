#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef vector<char> vc;
typedef map<char,int> mci;
typedef map<string,int> msi;
typedef map<int,int> mii;

#define ff first
#define ss second

struct edge
{
  int from,to,cost;
};

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

char grid[110][110];

bool ok(int n){
  for(int i=1;i<=n;i++){
    int cnt=0;
    for(int j=1;j<=n;j++){
      if(grid[i][j]=='x'||grid[i][j]=='o')
        cnt++;
    }
    if(cnt>=2)
      return false;
    cnt=0;
    for(int j=1;j<=n;j++){
      if(grid[j][i]=='x'||grid[j][i]=='o')
        cnt++;
    }
    if(cnt>=2)
      return false;
  }
  for(int k=1;k<=n;k++){
    int i=1,j=k,cnt=0;
    while(i>0&&i<=n&&j>0&&j<=n){
      if(grid[i][j]=='+'||grid[i][j]=='o')
        cnt++;
      i++;
      j--;
    }
    if(cnt>=2)
      return false;
  }
  for(int k=2;k<=n;k++){
    int i=k,j=n,cnt=0;
    while(i>0&&i<=n&&j>0&&j<=n){
      if(grid[i][j]=='+'||grid[i][j]=='o')
        cnt++;
      i++;
      j--;
    }
    if(cnt>=2)
      return false;
  }
  for(int k=1;k<=n;k++){
    int i=1,j=k,cnt=0;
    while(i>0&&i<=n&&j>0&&j<=n){
      if(grid[i][j]=='+'||grid[i][j]=='o')
        cnt++;
      i++;
      j++;
    }
    if(cnt>=2)
      return false;
  }
  for(int k=2;k<=n;k++){
    int i=k,j=1,cnt=0;
    while(i>0&&i<=n&&j>0&&j<=n){
      if(grid[i][j]=='+'||grid[i][j]=='o')
        cnt++;
      i++;
      j++;
      if(cnt>=2)
        return false;
    }
  }
  return true;
}

int main()
{
  int T;
  cin>>T;
  for(int ca=1;ca<=T;ca++){
    cout<<"Case #"<<ca<<":";
    int n,m;
    cin>>n>>m;
    for(int i=0;i<=n;i++){
      for(int j=0;j<=n;j++){
        grid[i][j]='.';
      }
    }
    char ch;
    int ri,ci;
    for(int i=0;i<m;i++){
      cin>>ch>>ri>>ci;
      grid[ri][ci]=ch;
    }
    if(!ok(n))
      continue;
    /*bool a=true,b=true;
    for(int i=1;i<=n;i++){
      for(int j=1;j<=n;j++){
        if(grid[i][j]=='.'){
          grid[i][j]='x';
          a=ok(n);
          grid[i][j]='+';
          b=ok(n);
          if(!a&&!b)
            grid[i][j]='n';
          else if(a&&b)
            grid[i][j]='.';
          else if(!a&&b)
            grid[i][j]='b';
          else
            grid[i][j]='a';
        }
      }
      }*/
    char ngrid[n+1][n+1];
    for(int i=0;i<=n;i++){
      for(int j=0;j<=n;j++){
        ngrid[i][j]=grid[i][j];
      }
    }
    int x=0,o=0;
    for(int i=1;i<=n;i++){
      if(grid[1][i]=='x')
        x=i;
      if(grid[1][i]=='o')
        o=i;
    }
    if(x==1){
      for(int i=2;i<=n;i++){
        ngrid[1][i]='+';
      }
      for(int i=2;i<n;i++){
        ngrid[n][i]='+';
      }
      ngrid[n][n]='o';
      for(int i=2;i<n;i++){
        ngrid[i][i]='x';
      }
    }
    if(x==n){
      for(int i=1;i<n;i++){
        ngrid[1][i]='+';
      }
      for(int i=2;i<n;i++){
        ngrid[n][i]='+';
      }
      ngrid[n][1]='o';
      for(int i=2,j=n-1;i<n;i++,j--){
        ngrid[i][j]='x';
      }
    }
    if(x>1&&x<n){
      for(int i=1;i<=n;i++){
        if(ngrid[1][i]!='x')
          ngrid[1][i]='+';
      }
      ngrid[x][1]='+';
      ngrid[1+n-x][n]='+';
      for(int i=2;i<n;i++){
        ngrid[n][i]='+';
      }
      ngrid[n][1+n-x]='.';
      if(n%2==0&&x<=n/2||n%2==1&&x<=n/2+1){
        for(int i=2,j=x+1;j<n;i++,j++){
          ngrid[i][j]='x';
        }
        for(int i=n-1,j=1;j<x;i--,j++){
          ngrid[i][j]='x';
        }
        ngrid[n][n]='x';
      }
      else{
        for(int i=2,j=x-1;j>1;i++,j--){
          ngrid[i][j]='x';
        }
        for(int i=n-1,j=n;j>x;i--,j--){
          ngrid[i][j]='x';
        }
        ngrid[n][1]='x';
      }
    }
    if(o==1){
      for(int i=2;i<=n;i++){
        ngrid[1][i]='+';
      }
      for(int i=2;i<n;i++){
        ngrid[n][i]='+';
      }
      for(int i=2;i<=n;i++){
        ngrid[i][i]='x';
      }
    }
    if(o==n){
      for(int i=1;i<n;i++){
        ngrid[1][i]='+';
      }
      for(int i=2;i<n;i++){
        ngrid[n][i]='+';
        }
      for(int i=2,j=n-1;j>0;i++,j--){
        ngrid[i][j]='x';
      }
    }
    if(o>1&&o<n){
      for(int i=1;i<=n;i++){
        if(ngrid[1][i]!='o')
          ngrid[1][i]='+';
      }
      for(int i=2;i<n;i++){
          ngrid[n][i]='+';
      }
      for(int i=2,j=o+1;j<=n;i++,j++){
        ngrid[i][j]='x';
      }
      for(int i=n,j=1;j<o;i--,j++){
        ngrid[i][j]='x';
      }
    }
    if(x==0&&o==0){
      ngrid[1][1]='o';
      for(int i=2;i<=n;i++){
        ngrid[1][i]='+';
      }
      for(int i=2;i<=n;i++){
        ngrid[i][i]='x';
      }
      for(int i=2;i<n;i++){
        ngrid[n][i]='+';
      }
    }
    int y=0,z=0;
    for(int i=1;i<=n;i++){
      for(int j=1;j<=n;j++){
        if(ngrid[i][j]=='x'||ngrid[i][j]=='+')
          y++;
        if(ngrid[i][j]=='o')
          y+=2;
        if(grid[i][j]!=ngrid[i][j])
          z++;
      }
    }
    cout<<' '<<y<<' '<<z<<endl;
    for(int i=1;i<=n;i++){
      for(int j=1;j<=n;j++){
        if(grid[i][j]!=ngrid[i][j])
            cout<<ngrid[i][j]<<' '<<i<<' '<<j<<endl;
      }
    }
  }
  return 0;
}

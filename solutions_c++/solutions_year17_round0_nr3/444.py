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


int main()
{
  int T;
  cin>>T;
  for(int ca=1;ca<=T;ca++){
    cout<<"Case #"<<ca<<":";
    long long n,k;
    cin>>n>>k;
    long long y,z;
    long long a[63];
    a[0]=1;
    for(int i=1;i<63;i++){
      a[i]=a[i-1]<<1;
    }
    for(int i=0;i<63;i++){
      a[i]--;
    }
    if(k==1){
      if(n%2==0){
        y=n/2;
        z=n/2-1;
      }
      else{
        y=n/2;
        z=n/2;
      }
    }
    else{
      int d=1;
      for(d=1;d<63;d++){
        if(a[d]>=k)
          break;
      }
      long long tmp=(n-k)/(a[d]+1);
      long long dis1=n-k-tmp*(a[d]+1);
      long long dis2=(tmp+1)*(a[d]+1)-(n-k);
      z=tmp;
      y=tmp;
      if(dis1>=dis2)
        y++;
    }
    cout<<' '<<y<<' '<<z<<endl;
  }
  return 0;
}

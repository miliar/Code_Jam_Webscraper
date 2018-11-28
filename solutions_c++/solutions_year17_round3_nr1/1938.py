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

bool cmp(pair<long,long> a,pair<long,long> b)
{
  return a.first<b.first;
}

int main()
{
  int T;
  cin>>T;
  const double pi=3.1415926535897932384626;
  for(int ca=1;ca<=T;ca++){
    cout<<"Case #"<<ca<<": ";
    long long res=0;
    int n,k;
    cin>>n>>k;
    vector<pair<long,long>> vec;
    long long r,h;
    for(int i=0;i<n;i++){
      cin>>r>>h;
      vec.push_back(make_pair(r,h));
    }
    sort(vec.begin(),vec.end(),cmp);
    priority_queue<long long,vector<long long>,greater<long long>> rh;
    for(int i=0;i<k-1;i++){
      res+=2*vec[i].ff*vec[i].ss;
      rh.push(2*vec[i].ff*vec[i].ss);
    }
    r=vec[k-1].ff;
    res+=vec[k-1].ff*vec[k-1].ff+2*vec[k-1].ff*vec[k-1].ss;
    rh.push(2*vec[k-1].ff*vec[k-1].ss);
    for(int i=k;i<n;i++){
      if(vec[i].ff*vec[i].ff-r*r+2*vec[i].ff*vec[i].ss>rh.top()){
        res=res-rh.top()+vec[i].ff*vec[i].ff-r*r+2*vec[i].ff*vec[i].ss;
        rh.pop();
        rh.push(2*vec[i].ff*vec[i].ss);
        r=vec[i].ff;
      }
    }
    cout.precision(9);
    cout<<fixed<<pi*res<<endl;
  }
  return 0;
}

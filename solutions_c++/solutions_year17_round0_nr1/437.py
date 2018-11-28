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
    string cake;
    int s;
    cin>>cake>>s;
    int i=0,len=cake.length(),res=0;
    bool poss=true;
    while(i<len){
      if(cake[i]=='+'){
        i++;
        continue;
      }
      else{
        if(i+s>len){
          poss=false;
          break;
        }
        for(int j=0;j<s;j++){
          if(cake[i+j]=='-')
            cake[i+j]='+';
          else
            cake[i+j]='-';
        }
        res++;
      }
    }
    if(!poss)
      cout<<" IMPOSSIBLE"<<endl;
    else
      cout<<" "<<res<<endl;
  }
  return 0;
}

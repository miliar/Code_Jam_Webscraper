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
    long long n;
    cin>>n;
    string s=to_string(n);
    int i=0,len=s.length();
    while(i<len-1){
      if(s[i]<=s[i+1])
        i++;
      else{
        if(i==0||(i>0&&s[i-1]+1<=s[i])){
          s[i]--;
          for(int j=i+1;j<len;j++){
            s[j]='9';
          }
          break;
        }
        else{
          while(i>0&&s[i-1]+1>s[i]){
            i--;
          }
          s[i]--;
          for(int j=i+1;j<len;j++){
            s[j]='9';
          }
          break;
        }
      }
    }
    cout<<" "<<stoll(s)<<endl;
  }
  return 0;
}

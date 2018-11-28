#include <bits/stdc++.h>

using namespace std;

#define siz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define foreach(it,a) for(__typeof((a).begin()) it=(a).begin();it!=(a).end();it++)
#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
#define per(i,a,b) for (int i=(b)-1,_ed=(a);i>=_ed;i--)

typedef long long ll;
typedef unsigned long long ull;

int T,N;
int s[19];
vector<int>ans;

char ch[10] = {'N','R','O','Y','G','B','V'};
int main()
{
#ifndef ONLINE_JUDGE
  freopen("B-small-attempt1.in","r",stdin);
  freopen("B.out","w",stdout);
#endif
  cin >> T;
  rep(cas, 1, T+1) {
    printf("Case #%d: ", cas);
    for(int i = 0; i <=6;i ++) cin>>s[i];
    bool ok = true;
    for(int i = 1; i <= 6; i++) 
      if(s[i] > s[0]/2) {
        ok = false;
      }
    if(!ok) {
      printf("IMPOSSIBLE\n");
      continue;
    }
    ans.clear();
    ans.push_back(0);
    for(int i = 1; i <= s[0]; i++) {
      int id = -1;
      int sx = 0;
      for(int j = 1; j <= 6; j++) {
        if(j!=ans.back() && s[j] > sx) {
          id = j;
          sx = s[j];
        }
      }
      ans.push_back(id);
      s[id]--;
    }
    if(ans[s[0]] == ans[1]) {
      int t1 = ans.back();
      ans.pop_back();
      int t2 = ans.back();
      ans.pop_back();
      ans.push_back(t1);
      ans.push_back(t2);
    }
    for(int i = 1; i <siz(ans) ; i++) {
      if(ans[i] == ans[i-1]) cout << "---------------------" << endl;
      cout << ch[ans[i]];
    }
    cout << endl;
    if(ans[s[0]] == ans[1]) {
      for(int i = 0; i <=6; i++) {
        cout << s[i] << ' ';
      }
      cout << endl;
    }
  }


  return 0;
}


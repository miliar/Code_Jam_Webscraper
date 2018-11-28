#include <bits/stdc++.h>
#define INF 1000000007
#define in cin.sync_with_stdio(0);cin.tie(0);
#define PI 3.14159265358979323846
#define clr(v,d) memset(v,d,sizeof(v))
#define all(v) v.begin(),v.end()
#define sz(v) (int)v.size()
#define mp make_pair
#define pb push_back
#define a first
#define b second

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;

int T;
string s;

bool isTidy(){
  if(sz(s)==1) return 1;
  for(int i=sz(s)-1; i>0; i--){
    if(s[i]=='0' || s[i-1]>s[i] || s[i-1]==0) return 0;
  }
  return 1;
}

int main ()
{

//  in;
  freopen("B-small-attempt5.in", "r", stdin);
  freopen("output.txt", "w", stdout);

  cin >> T;
  for(int i=1; i<=T; i++){
    cin >> s;
//    cout << s << " ";
    while(!isTidy()){
      for(int i=sz(s)-1; i>0; i--){
        if(s[i]=='0' || s[i-1]>s[i]){
          s[i] = '9';
          s[i-1]-=(s[i-1]>'0');
          int j = i+1;
          while(j<sz(s)){
            s[j] = '9';
            j++;
          }
//          cout << s << endl;
          break;
        }
        else if(s[i-1]=='0' && i-1>0){
          int j = i-2;
          s[i] = s[i-1] = '9';
          while(1){
            if(s[j]>'0'){
              s[j]--;
              break;
            }
            else{
              s[j]='9';
              j--;
            }
          }
        }
      }
    }
    cout << "Case #" << i << ": ";
    for(int i=(s[0]=='0'); i<sz(s); i++) cout << s[i];
    cout << endl;
  }

  return 0;
}

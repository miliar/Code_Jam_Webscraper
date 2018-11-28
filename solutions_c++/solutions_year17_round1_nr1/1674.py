#include <bits/stdc++.h>

using namespace std;

const int inf = 2e9 + 20;
typedef long long ll;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii;
typedef priority_queue<int> pqmax;
typedef priority_queue<int, vector<int>, greater<int> > pqmin; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(auto i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

int main(){

  ios_base::sync_with_stdio(false);

  int t;
  cin >> t;

  int caseno = 0;
  while(t--){
    caseno++;

    int r,c;
    cin >> r >> c;

    vector<vector<char> > v(r, vector<char>(c)); 
    for(int i=0; i<r; i++){
      for(int j=0; j<c; j++)
        cin >> v[i][j];
    }

    for(int i=0; i<r; i++){
      for(int j=0; j<c; j++){
        if(v[i][j] != '?'){
          int k = j-1;
          int l = j+1;
          while(k >= 0 && v[i][k] == '?'){
            v[i][k] = v[i][j];
            k--;
          }
          while(l < c && v[i][l] == '?'){
            v[i][l] = v[i][j];
            l++;
          }
        }
      }
    }

    int recent = -1;
    for(int i=0; i<r; i++){
      if(v[i][0] != '?')
        recent = i;
      else
      if(recent != -1){
        for(int j=0; j<c; j++)
          v[i][j] = v[recent][j];
      }
    }

    recent = -1;
    for(int i=r-1; i>=0; i--){
      if(v[i][0] != '?')
        recent = i;
      else
      if(recent != -1){
        for(int j=0; j<c; j++)
          v[i][j] = v[recent][j];
      }
    }

    cout << "Case #" << caseno << ":"<< endl;

    for(int i=0; i<r; i++){
      for(int j=0; j<c; j++){
        cout << v[i][j];
      }
      cout << endl;
    }
  }

  return 0;
}
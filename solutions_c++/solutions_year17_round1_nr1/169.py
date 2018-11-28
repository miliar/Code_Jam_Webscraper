#include <bits/stdc++.h>

#define ft first
#define sd second
#define mp make_pair
#define pb push_back

using namespace std;

vector<pair<int, int> > letras;
string g[30];

bool preenchida[30];

main(){
  int t;
  scanf("%d", &t);

  for(int c=1;c<=t;c++){
    printf("Case #%d:\n", c);

    int n, m;
    scanf("%d %d", &n, &m);

    letras.clear();
    for(int i=0;i<n;i++){
      preenchida[i] = 0;
      cin >> g[i];

      for(int j=0;j<g[i].size();j++)
        if(g[i][j] >= 'A' && g[i][j] <= 'Z')
          letras.pb(mp(i, j));
    }

    for(int k=0;k<letras.size();k++){
      int i = letras[k].ft;
      int j = letras[k].sd;

      for(int j2=j-1;j2>=0 && g[i][j2] == '?';j2--)
        g[i][j2] = g[i][j];

      for(int j2=j+1;j2<m && g[i][j2] == '?';j2++)
        g[i][j2] = g[i][j];
      
      preenchida[i] = true;
    }

    string ult = g[0];

    if(preenchida[0] == false){
      for(int i=1;i<n;i++){
        if(preenchida[i]){
          ult = g[i];
          break;
        }
      }
    }

    cout << ult << '\n';
    for(int i=1;i<n;i++){
      if(preenchida[i])
        ult = g[i];
      cout << ult << '\n';
    }
  }
}
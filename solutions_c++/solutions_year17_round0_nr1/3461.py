#include <bits/stdc++.h>

using namespace std;

const int N = 2010;
const int BASE = 1005;

int n, k;
int f[N];
vector < int > adj[N];

int main(){
freopen("1.inp", "r", stdin);
  freopen("1.out", "w", stdout);
  ifstream fi("correct.out");
  int tt;
  scanf("%d", &tt);
  for(int iTest = 1; iTest <= tt; ++iTest){
    char a[N];
    scanf("%s%d", a + 1, &k);
    n = strlen(a + 1);
    int answer = 0;
   /*for(answer = 0; answer <= n;){
      bool stop = true;
      for(int i = 1; i <= n; ++i){
        if(a[i] == '-'){
          stop = false;
        }
      }
      if(stop == true){
        break;
      }
      for(int i = 1; i <= n; ++i){
        f[i] = f[i - 1] + (a[i] == '-');
      }
      int pos = -1;
      for(int i = k; i <= n; ++i){
        if(f[i] - f[i - k] == k){
          pos = i;
          break;
        }
      }
      if(pos == -1){
        break;
      }
            ++answer;

      for(int i = pos - k + 1; i <= pos; ++i){
        a[i] = (a[i] == '-' ? '+' : '-');
      }
    }
    for(int i = 0; i < k; ++i){
      adj[i].clear();
    }
    for(int i = 1; i <= n; ++i){
        adj[i % k].push_back(i);
    }
    bool stop = false;
    for(int i = 0; i < k; ++i){
        int change = 0;
        for(int x = 0; x < adj[i].size(); ++x){
            if(change == 1){
                ++answer;
                change = 0;
                a[adj[i][x]] = (a[adj[i][x]] == '-' ? '+' : '-');
            }
            if(x < adj[i].size() - 1&& a[adj[i][x]] == '-'){
                a[adj[i][x]] = '+';
                change = 1;
                ++answer;
            }
        }
    }
    for(; answer <= n;){
      bool stop = true;
      for(int i = 1; i <= n; ++i){
        if(a[i] == '-'){
          stop = false;
        }
      }
      if(stop == true){
        break;
      }
      for(int i = 1; i <= n; ++i){
        f[i] = f[i - 1] + (a[i] == '-');
      }
      int pos = -1;
      for(int i = k; i <= n; ++i){
        if(f[i] - f[i - k] == k){
          pos = i;
          break;
        }
      }
      if(pos == -1){
        break;
      }
        ++answer;

      for(int i = pos - k + 1; i <= pos; ++i){
        a[i] = (a[i] == '-' ? '+' : '-');
      }
    }*/
    for(int i = 1; i <= n; ++i){
        if(i <= n - k + 1 && a[i] == '-'){
        ++answer;
            for(int j = i; j < i + k; ++j){
                a[j] = (a[j] == '-' ? '+' : '-');
            }
        }
    }
    bool ok = false;
    for(int i = 1; i <= n; ++i){
        if(a[i] == '-'){
            ok = true;
            break;
        }
    }
    printf("Case #%d: ", iTest);

    /*string x, y, z;
    fi >> x >> y >> z;*/
    if(ok == 1){
      puts("IMPOSSIBLE");
        /*if(z != "IMPOSSIBLE"){
            cerr << "Wrng " << endl;
        }*/
    }
    else{
    /*if(z == "IMPOSSIBLE"){
        cerr << iTest << endl;
    }*/
      printf("%d\n", answer);
    }
  }
  return 0;
}

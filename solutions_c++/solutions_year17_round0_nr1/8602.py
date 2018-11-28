#include <cstdio>
#include <vector>
#include <iostream>
#include <cstring>
#include <queue>
#include <map>

using namespace std;

typedef pair<string, int> si;

char chapa[1001]; int K;
map<string, int> visited;

bool isAns(string u){
  bool hasMinus = false;
  for(int i = 0; i < (int) u.size(); i++){
    if(u[i] == '-') return false;
  }
  return true;
}

int solve(string s_chapa){
  visited.clear();
  int ans = 0;
  queue<si> q;
  q.push(si(s_chapa, 0));
  visited[s_chapa] = 0;
  while(!q.empty()){
    si top = q.front(); q.pop();
    string u = top.first; int d = top.second;
    if(isAns(u)){
      return d;
    }
    
    for(int i = 0; i <= ((int) u.size()) - K; i++){
      string aux(u);
      for(int j = i; j < i + K; j++){
        if(aux[j] == '-') aux[j] = '+';
        else aux[j] = '-';
      }
      if(visited.find(aux) == visited.end()){
        visited[aux] = d;
        q.push(si(aux, d + 1));
      }
    }
  }
  return -1;
}

int main(){
  int T; scanf("%d", &T);
  for(int cs = 1; cs <= T; cs++){\
    printf("Case #%d: ", cs);
    bool ans = true, hasMinus = false;
    scanf("%s %d", chapa, &K);
    int size = (int) strlen(chapa);
    //cout << chapa << " " << K << endl;
    for(int i = 0; i < size && !hasMinus; i++){
      if(chapa[i] == '-'){
        hasMinus = true;
      }
    }
    if(!hasMinus){
      puts("0");
      continue;
    }else{
      int xx = solve(string(chapa));
      if(xx == -1) puts("IMPOSSIBLE");
      else printf("%d\n", xx);
    }
    
  }
  return 0;
}

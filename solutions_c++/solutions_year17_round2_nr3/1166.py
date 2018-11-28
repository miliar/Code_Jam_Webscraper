#include<iostream>
#include<iomanip>
#include<vector>
#include<queue>

struct Horse {
  int maxDist;
  double speed;
};
struct State {
  int current;
  int horse;
  int dist;
  double time;
  bool operator > (const State &e) const {
    return time == e.time ? dist > e.dist : time > e.time;
  }
};

void proc(){
  int n,q;
  std::cin >> n >> q;
  std::vector<Horse> hs(n);
  for(int i=0;i<n;i++){
    int e,s;
    std::cin >> e >> s;
    hs[i].maxDist = e;
    hs[i].speed = s;
  }
  std::vector<std::vector<int> > dist;
  for(int i=0;i<n;i++){
    std::vector<int> d;
    for(int j=0;j<n;j++){
      int p;
      std::cin >> p;
      d.push_back(p);
    }
    dist.push_back(d);
  }
  for(int i=0;i<q;i++){
    int u,v;
    std::cin >> u >> v;
    u--,v--;
    std::priority_queue<State,std::vector<State>,std::greater<State>> Qu;
    std::vector<std::vector<bool>> went(n,std::vector<bool>(n));
    Qu.push(State{u,-1,0,0});
    double result;
    while(!Qu.empty()){
      State s = Qu.top();
      Qu.pop();
      if(s.horse!=-1 && went[s.current][s.horse])continue;
      if(s.horse!=-1)went[s.current][s.horse] = true;
      //std::cerr << "{" << s.current << "/" << s.horse << " | " << s.time << "}\n";
      if(s.current == v){
        result = s.time;
        break;
      }
      for(int i=0;i<n;i++){
        int dd = dist[s.current][i];
        if(dd!=-1){
          if(s.horse==-1){
            Qu.push(State{i,s.current,dd,dd/hs[s.current].speed});
          }else{
            int nd = s.dist + dd;
            if(nd <= hs[s.horse].maxDist){
              Qu.push(State{i,s.horse,nd,s.time+dd/hs[s.horse].speed});
            }
            if(dd <= hs[s.current].maxDist){
              Qu.push(State{i,s.current,dd,s.time+dd/hs[s.current].speed});
            }
          }
        }
      }
    }
    std::cout << result;
    if(i!=q-1)std::cout << " ";
  }
}

int main(){
  std::cout << std::setprecision(10);
  int T;
  std::cin >> T;
  for(int i=1;i<=T;i++){
    std::cout << "Case #" << i << ": ";
    proc();
    std::cout << std::endl;
  }
  return 0;
}

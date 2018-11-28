#include <iostream>
#include <vector>
#include <queue>
#include <stdint.h>
#include <cassert>
#include <iomanip>

int64_t limit[100],speed[100];

int64_t dist[100][100];

double shortest[100];

void solve(){
  int64_t N,Q;
  std::cin>>N>>Q;
  for(int64_t i=0;i<N;i++){
    std::cin>>limit[i]>>speed[i];
    assert(speed[i]!=0);
  }
  for(int64_t i=0;i<N;i++){
    for(int64_t j=0;j<N;j++){
      std::cin>>dist[i][j];
      if(dist[i][j]==-1){
	dist[i][j]=1e15;
      }
    }
  }
  for(int64_t k=0;k<N;k++){
    for(int64_t i=0;i<N;i++){
      for(int64_t j=0;j<N;j++){
	dist[i][j]=std::min(dist[i][j],dist[i][k]+dist[k][j]);
      }
    }
  }
  for(int64_t i=0;i<Q;i++){
    for(int64_t i=0;i<N;i++){
      shortest[i]=1e15;
    }
    int64_t U,V;
    std::cin>>U>>V;
    U--,V--;
    std::priority_queue<std::pair<double,int64_t> > frontier;
    frontier.push(std::make_pair(0,V));
    while(!frontier.empty()){
      double len=-frontier.top().first;
      int64_t node=frontier.top().second;
      frontier.pop();
      if(shortest[node]<len){
	continue;
      }
      shortest[node]=len;
      for(int64_t i=0;i<N;i++){
	if(dist[i][node]<=limit[i]){
	  frontier.push(std::make_pair(-(dist[i][node]/double(speed[i])+len),i));
	}
      }
    }
    std::cout<<" "<<std::fixed<<std::setprecision(10)<<shortest[U];
  }
}

int main(){
  int64_t T;
  std::cin>>T;
  for(int64_t i=1;i<=T;i++){
    std::cout<<"Case #"<<i<<":";
    solve();
    std::cout<<std::endl;
  }
  return 0;
}

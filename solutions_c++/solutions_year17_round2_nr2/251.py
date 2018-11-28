#include <iostream>
#include <sstream>
#include <vector>

const std::string impossible="IMPOSSIBLE";

int graph[6][6];
//graph must also be symmetric
enum{
  l_R=0,
  l_O=1,
  l_Y=2,
  l_G=3,
  l_B=4,
  l_V=5,
};

void dfs(int node,std::vector<int>& out){
  for(int i=0;i<6;i++){
    while(graph[node][i]>0){
      graph[node][i]--;
      graph[i][node]--;
      dfs(i,out);
      out.push_back(node);
    }
  }
}

std::string solve(){
  int N,R,O,Y,G,B,V;
  int as[6];
  std::cin>>N;
  for(int i=0;i<6;i++){
    std::cin>>as[i];
  }
  R=as[l_R];
  O=as[l_O];
  Y=as[l_Y];
  G=as[l_G];
  B=as[l_B];
  V=as[l_V];
  int RG=G*2,YV=V*2,BO=O*2;
  int RYB=R+Y+B-V-G-O;
  int RY=RYB-B*2+O*2;
  int RB=RYB-Y*2+V*2;
  int BY=RYB-R*2+G*2;
  /*Auto clears previous round*/
  graph[l_R][l_G]=graph[l_G][l_R]=RG;
  graph[l_Y][l_V]=graph[l_V][l_Y]=YV;
  graph[l_B][l_O]=graph[l_O][l_B]=BO;
  graph[l_R][l_Y]=graph[l_Y][l_R]=RY;
  graph[l_R][l_B]=graph[l_B][l_R]=RB;
  graph[l_B][l_Y]=graph[l_Y][l_B]=BY;
  for(int i=0;i<6;i++){
    for(int j=0;j<6;j++){
      if(graph[i][j]<0){
	return impossible;
      }
    }
  }
  std::vector<int> out;
  for(int i=0;i<6;i++){
    if(as[i]>0){
      dfs(i,out);
      break;
    }
  }
  for(int i=0;i<out.size();i++){
    as[out[i]]--;
  }
  for(int i=0;i<6;i++){
    if(as[i]>0){
      return impossible;
    }
  }
  std::string ret;
  for(int i=0;i<out.size();i++){
    ret+="ROYGBV"[out[i]];
  }
  return ret;
}

int main(){
  int T;
  std::cin>>T;
  for(int i=1;i<=T;i++){
    std::cout<<"Case #"<<i<<": "<<solve()<<std::endl;
  }
  return 0;
}

#include <iostream>
#include <vector>

int dp2[101];
int dp3[101][101];
int dp4[101][101][101];

void precompute(){
  for(int i=0;i<=100;i++){
    dp2[i]=0;
    if(i>0){
      dp2[i]=std::max(dp2[i],dp2[i-1]);
    }
    if(i%2==0){
      dp2[i]++;
    }
  }
  for(int i=0;i<=100;i++){
    if(i%2==0){
      dp2[i]--;
    }
  }
  for(int i=0;i<=100;i++){
    for(int j=0;j<=100;j++){
      dp3[i][j]=0;
      if(i>0){
	dp3[i][j]=std::max(dp3[i][j],dp3[i-1][j]);
      }
      if(j>0){
	dp3[i][j]=std::max(dp3[i][j],dp3[i][j-1]);
      }
      if((i+j*2)%3==0){
	dp3[i][j]++;
      }
    }
  }
  for(int i=0;i<=100;i++){
    for(int j=0;j<=100;j++){
      if((i+j*2)%3==0){
	dp3[i][j]--;
      }
    }
  }
  for(int i=0;i<=100;i++){
    for(int j=0;j<=100;j++){
      for(int k=0;k<=100;k++){
	dp4[i][j][k]=0;
	if(i>0){
	  dp4[i][j][k]=std::max(dp4[i][j][k],dp4[i-1][j][k]);
	}
	if(j>0){
	  dp4[i][j][k]=std::max(dp4[i][j][k],dp4[i][j-1][k]);
	}
	if(k>0){
	  dp4[i][j][k]=std::max(dp4[i][j][k],dp4[i][j][k-1]);
	}
	if((i+j*2+k*3)%4==0){
	  dp4[i][j][k]++;
	}
      }
    }
  }
  for(int i=0;i<=100;i++){
    for(int j=0;j<=100;j++){
      for(int k=0;k<=100;k++){
	if((i+j*2+k*3)%4==0){
	  dp4[i][j][k]--;
	}
      }
    }
  }
}

int compute(const std::vector<int>& count){
  switch(count.size()){
  case 2:
    return count[0]+dp2[count[1]];
  case 3:
    return count[0]+dp3[count[1]][count[2]];
  case 4:
    return count[0]+dp4[count[1]][count[2]][count[3]];
  }
}

int main(){
  precompute();
  int T;
  std::cin>>T;
  for(int t=1;t<=T;t++){
    int N,P;
    std::cin>>N>>P;
    std::vector<int> count(P);
    for(int i=0;i<N;i++){
      int G;
      std::cin>>G;
      count[G%P]++;
    }
    std::cout<<"Case #"<<t<<": "<<compute(count)<<std::endl;
  }
  return 0;
}

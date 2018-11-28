#include <bits/stdc++.h>
using namespace std;
int T, Q;
long long N, K;
//vector<long long> arr; //1 base
map<long long, long long> ma;
void ini(void){
  cin>>N>>K;
  ma.clear();
  ma[N] = 1;
  /*
  for(auto i: ma) printf("(%lld, %d) ", i.first, i.second);
  cout<<endl;
  
  arr.assign(1, N);
  for(auto i: arr) cout<<i<<" ";
  cout<<endl;
  */
}

void sol(void){
  long long sum = 0, total = 1, M, v;
  while(sum + total < K){
    sum += total;
    //sum += size;
    long long tmp = 0;
    map<long long, long long> ma1;
    for(auto i : ma){
      v = i.first;
      M = (v + 1) >> 1ll;
      if(v & 1){
        ma1[v - M] += i.second;
        ma1[M - 1] += i.second;
      }else{
        if(v != 2) ma1[v - M - 1] += i.second;
        ma1[M] += i.second;
      }
      if(v != 2) tmp += i.second << 1;
      else tmp += i.second;
    }
    ma = ma1;
    total = tmp;
    
  /* 
  for(auto i: ma) printf("(%lld, %lld) ", i.first, i.second);
  cout<<endl;
  printf("total = %lld, sum = %lld\n", total, sum);
  long long zz;
  cin>>zz;
  zz+= 5;
    
    for(int i = 0; i < size; i++){
      v = arr[i];
      M = (v + 1) >> 1ll;
      if(v & 1){
        arr.push_back(v - M);
        arr[i] = M - 1;
      }else{
        arr.push_back(v - M - 1);
        arr[i] = M;
      }
    }
    size = arr.size();
    for(auto i: arr) cout<<i<<" ";
    cout<<endl;
    */
  }
  if(sum + (*(ma.rbegin())).second >= K) v = (*(ma.rbegin())).first;
  else v = (*(ma.begin())).first;
  M = (v + 1) >> 1ll;
  //printf("v = %lld, M = %lld => ", v, M);
  if(!(v & 1)) M++;
  cout<<M - 1<<" "<<v - M<<endl;
  /*
  v = arr[0];
  M = (v + 1) >> 1ll;
  if(!(v & 1)) M++;
  cout<<M - 1<<" "<<v - M<<endl;
  */
}

int main(void){
  int i, j;
  cin>>T;
  for(int i = 1; i <= T; i++){
    ini();
    cout<<"Case #"<<i<<": ";
    sol();
  }
}

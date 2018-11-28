#include<iostream>
#include<queue>
#include<vector>
using namespace std;
struct compara{
  bool operator()(long long a, long long b){
    return a<b;
  }
};
int main(){
  freopen("input.txt", "r", stdin);
  freopen("outputcodeC.txt", "w", stdout);
  int t;
  scanf("%d", &t);
  for(int i=0;i<t;i++){
    long long n, k;
    scanf("%lld %lld", &n, &k);
    priority_queue<long long, vector<long long>, compara> q;
    q.push(n);
    for(int j=0;j<k-1;j++){
      //cout<<q.top()<<endl;
      long long temp=q.top();
      q.pop();
      if(temp%2==0){
        q.push(temp/2);
        q.push((temp-1)/2);
      }else{
        q.push((temp-1)/2);
        q.push((temp-1)/2);
      }
    }
    cout<<"Case #"<<i+1<<": "<<q.top()/2<<" "<<(q.top()-1)/2<<endl;
  }
}

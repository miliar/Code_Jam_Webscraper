#include <iostream>
#include <vector>
#include <set>
#include <cmath>
#include <queue>
#include <map>
using namespace std;

 
int main(){
	int nb;
	cin >>nb;
	for(int cases=0; cases<nb; cases++){
    cout << "Case #"<<cases+1<<": ";
    long long K, N;
    cin >>N>>K; 
    priority_queue<long long> q;
    q.push(N);
    map<long long,long long>rows;
    rows[N]=1;
    while(K>0){
      long long i =q.top();
      q.pop();
      if(rows[i]==0) continue;
      if(rows[i] <K){
        long long a = i/2;
        q.push(a);
        rows[a]+=rows[i];
        a = (i-1)/2;
        q.push(a);
        rows[a]+=rows[i];
        K-= rows[i];
        rows[i]=0;
      }else{
        K=0;
        cout <<(i/2)<<" "<<(i-1)/2<<endl;
        break;
      }
    }
  }
	return 0;
}

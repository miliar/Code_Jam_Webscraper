#include"iostream"
#include"string"
#include"queue"

using namespace std;

int main(){
    int times,t=0;
    cin >> times;
    while(times--){
      t++;
      int N,K,tmp;
      cin >> N >> K;
      K--;
      priority_queue<int> pq;
      pq.push(N);
      while(K--){
        tmp=pq.top();
        pq.pop();
        tmp--;
        if(tmp%2==0){
          pq.push(tmp/2);
          pq.push(tmp/2);
        }else{
          pq.push(tmp/2);
          pq.push((tmp/2)+1);
        }
      }
      int max,min;
      int out = pq.top();
      cout << "Case #" << t << ": ";
      if(out%2==0){
        max=(out/2);
        min=(out/2)-1;
      }else{
        max=min=(out/2);
      }
      cout << max << " " << min << endl;
    }
    return 0;
}

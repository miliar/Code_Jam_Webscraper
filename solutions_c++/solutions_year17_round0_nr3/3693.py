#include <bits/stdc++.h>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n, k;
    cin >> n >> k;

    priority_queue<int> mq; 

    int p = 0, left = 0, right = n-1;
    int curLeft, curRight;
    while(p < k) {
      int mid = (left + right) / 2;
      curLeft = mid - left;
      curRight = right - mid;
      if ((left + right) % 2 == 0){
	mq.push(mid-left);
	mq.push(right-mid);
      }
      else{
	mq.push(right-mid);
	mq.push(mid-left);
      }
      p += 1;
      int tmp =  mq.top();
      mq.pop();
      left = 0;
      right = tmp-1;
    }

    cout << "Case #" << i+1 << ": " << max(curLeft, curRight) << " " << min(curLeft, curRight) << endl;
  }
  
  return 0;
}

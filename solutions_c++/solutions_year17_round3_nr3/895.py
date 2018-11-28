#include <bits/stdc++.h>
#define PI 3.141592653589793238462
using namespace std;
double arr[1004];
int n,k;
double lol;
int main() {
  freopen("inp.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int T;
  cout << fixed << setprecision(20);
  cin >> T;
  for(int t = 1 ; t <= T ; t ++){
    cout << "Case #"<<t<<": ";
    cin >> n >> k >> lol;

    priority_queue<pair<double, int>>pq;
    for(int i = 0 ; i < n ; i ++){
        cin >> arr[i];
    }
    sort(arr, arr+n);
    for(int i = 0 ; i < n ; i ++){
        int cnt = 0;
        for(int j = i ; j < n ; j ++){
            if(arr[i] == arr[j]){
                cnt++;
            }
        }
        pq.push({-arr[i], cnt});
        i += cnt-1;
    }
    while(lol > 0 && -pq.top().first < 1.0){
        double val = -pq.top().first;
        double cnt = pq.top().second;
        pq.pop();
        if(pq.empty()){
            val += lol/cnt;
            lol = 0;
            pq.push({-min(1.0,val), cnt});
        }else{
            double val2 = -pq.top().first;
            double cnt2 = pq.top().second;
            double dval = val2-val;
            pq.pop();
            if(lol >= dval*cnt){
                cnt2 += cnt;
                lol -= dval*cnt;
                pq.push({-min(1.0,val2), cnt2});
            }else{
                val += lol/cnt;
                lol = 0;
                pq.push({-min(1.0,val), cnt});
                pq.push({-min(1.0,val2), cnt2});
            }
        }
    }
    double ans = 1.0;
    while(!pq.empty()){
        int cnt = pq.top().second;
        while(cnt--)
            ans *= -pq.top().first;
        pq.pop();
    }
    cout << ans;
    cout << endl;
  }
  return 0;
}

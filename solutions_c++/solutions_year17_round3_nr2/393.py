#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int T;

int main () {

  cin >> T;

  for(int tc=1;tc<=T;tc++) {

    int ret = 0;
    int ac, aj;
    vector<pair<pair<int,int>, bool> > ts;
    cin >> ac >> aj;
    for(int i=0;i<ac;i++) {
      int t1,t2;
      cin >> t1 >> t2;
      ts.push_back(make_pair(make_pair(t1,t2), false));
    }
    for(int i=0;i<aj;i++) {
      int t1,t2;
      cin >> t1 >> t2;
      ts.push_back(make_pair(make_pair(t1,t2), true));
    }
    sort(ts.begin(), ts.end());

    int csum=0, jsum=0;
    priority_queue<int> cgap, jgap;
    if(ts[0].second) {
      jsum += ts[0].first.second - ts[0].first.first;
    } else {
      csum += ts[0].first.second - ts[0].first.first;
    }
    for(int i=1;i<ts.size();i++) {
      int t1 = ts[i].first.first;
      int t2 = ts[i].first.second;
      bool isJamie = ts[i].second;
      bool preIsJamie = ts[i-1].second;
      int gap;
      if(isJamie == preIsJamie) {
        gap = t1 - ts[i-1].first.second;
      } else {
        ret ++;
        gap = 0;
      }
      if(isJamie) {
        jgap.push(gap);
        jsum += t2-t1 + gap;
      } else {
        cgap.push(gap);
        csum += t2-t1 + gap;
      }
    }

    if(ts[ts.size()-1].second == ts[0].second) {
      bool isJamie = ts[ts.size()-1].second;
      int gap = ts[0].first.first+ 1440 - ts[ts.size()-1].first.second;
      if(isJamie) {
        jsum += gap;
        jgap.push(gap);
      } else {
        csum += gap;
        cgap.push(gap);
      }
    } else {
      ret ++;
    }

    while(jsum > 720) {
      jsum -= jgap.top();
      jgap.pop();
      ret +=2;
    }
    while(csum > 720) {
      csum -= cgap.top();
      cgap.pop();
      ret +=2;
    }

    printf("Case #%d: ",tc);
    printf("%d", ret);
    printf("\n");
  }

  return 0;
}
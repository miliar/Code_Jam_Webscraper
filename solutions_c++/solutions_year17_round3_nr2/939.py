#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<pair<int, int>, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
typedef pair<int, pair<int, pair<int, int> > > i_ii;

#define I18F 1000000000000000000 // 10^18
#define INF 2139062143
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B

int N, _T;

int main(){
  scanf("%d", &_T);
  for(int _t = 0; _t < _T; ++_t){
    printf("Case #%d: ", _t + 1);
    int A, B;
    priority_queue<ii, vector<ii> > a, b, c;
    priority_queue<i_ii, vector<i_ii>, greater<i_ii> > swaps;
    vector<iii> sched;
    scanf("%d %d", &A, &B);
    int time[2];
    time[0] = time[1] = 0;
    int at = 0;
    int bt = 0;
    for(int i = 0; i < A; ++i){
      int s, e;
      scanf("%d %d", &s, &e);
      time[1] += e-s;
      //at += e - s;

      sched.push_back(make_pair(make_pair(s, e), 1));
    }
    for(int i = 0; i < B; ++i){
      int s, e;
      scanf("%d %d", &s, &e);
      time[0] += e-s;
      //bt += e - s;
      sched.push_back(make_pair(make_pair(s, e), 0));
    }
    sort(sched.begin(), sched.end());
    //a.push(make_pair(sched[0].first.first, sched[0].second));
    //b.push(make_pair(sched[0].first.first, 1 - sched[0].second));
    if(sched[0].second == sched[A+B-1].second){ // MATCH!
      swaps.push(make_pair(0, make_pair(sched[0].first.first + 1440 - sched[A+B-1].first.second, make_pair(0, sched[0].second))));
      swaps.push(make_pair(2, make_pair(sched[0].first.first + 1440 - sched[A+B-1].first.second, make_pair(0, 1 - sched[0].second))));
    }else{
      swaps.push(make_pair(1, make_pair(sched[0].first.first + 1440 - sched[A+B-1].first.second, make_pair(0, 1 - sched[0].second))));
    }
    for(int i = 0; i < sched.size() - 1; ++i){
      if(sched[i].second == sched[i+1].second){ // MATCH!
        //a.push(make_pair(sched[i+1].first.first - sched[i].first.second, sched[i].second));
        //c.push(make_pair(sched[i+1].first.first - sched[i].first.second, sched[i].second));
        swaps.push(make_pair(0, make_pair(sched[i+1].first.first - sched[i].first.second, make_pair(i+1, sched[i].second))));
        swaps.push(make_pair(2, make_pair(sched[i+1].first.first - sched[i].first.second, make_pair(i+1, sched[i].second))));
      }else{
        swaps.push(make_pair(1, make_pair(sched[i+1].first.first - sched[i].first.second, make_pair(i+1, 1 - sched[i].second))));
        //b.push(make_pair(sched[i+1].first.first - sched[i].first.second, sched[i].second));
      }
    }
    //a.push(make_pair(1440 - sched[A+B-1].first.second, sched[A+B-1].second));
    //b.push(make_pair(1440 - sched[A+B-1].first.second, sched[A+B-1].second));
    //swaps.push(make_pair(0, make_pair(1440 - sched[A+B-1].first.second, make_pair(A+B, sched[A+B-1].second))));
    //swaps.push(make_pair(1, make_pair(1440 - sched[A+B-1].first.second, make_pair(A+B, 1 - sched[A+B-1].second))));
/*
    if(sched[0].second == sched[A+B-1].second){ // MATCH!
      swaps.push(make_pair(0, make_pair(1440 - sched[A+B-1].first.second, make_pair(A+B, sched[A+B-1].second))));
      swaps.push(make_pair(1, make_pair(1440 - sched[A+B-1].first.second, make_pair(A+B, 1 - sched[A+B-1].second))));
      //swaps.push(make_pair(0, make_pair(sched[0].first.first, make_pair(0, sched[0].second))));
      //swaps.push(make_pair(1, make_pair(sched[0].first.first, make_pair(0, 1 - sched[0].second))));
    }else{
      swaps.push(make_pair(1, make_pair(sched[0].first.first, make_pair(0, 1 - sched[i].second))));
    }
    */

    int total = 0;
    bool taken[A+B+1];
    for(int i = 0; i < A+B+1; ++i) taken[i] = false;
    while(!swaps.empty() && time[0] + time[1] < 1440){
      i_ii top = swaps.top(); swaps.pop();
      if(taken[top.second.second.first]) continue;
      if(top.first == 0){
        if(time[top.second.second.second] + top.second.first <= 720){
          time[top.second.second.second] += top.second.first;
          taken[top.second.second.first] = true;
        }
        //printf("1:assign %d, %d to %d, %d\n", top.second.second.first, top.second.first, top.second.second.second, total);
      }else{
        total += top.first;
        taken[top.second.second.first] = true;
        if(time[0] + top.second.first > 720){
          //printf("2:assign %d, %d to %d, %d\n", top.second.second.first, top.second.first - (720 - time[0]), 1, total);
          //printf("2:assign %d, %d to %d, %d\n", top.second.second.first, 720-time[0], 0, total);
          time[1] += top.second.first - (720 - time[0]);
          time[0] = 720;
        }else{
          //printf("3:assign %d, %d to %d, %d\n", top.second.second.first, top.second.first, 0, total);
          time[0] += top.second.first;
        }
      }
    }
    printf("%d\n", total);
  }
}

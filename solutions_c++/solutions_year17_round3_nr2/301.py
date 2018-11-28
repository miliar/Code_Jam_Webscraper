#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int T;
int AJ, AC;
typedef pair<int, int> PII;
typedef pair<PII, int> PPIII;
vector<PPIII> schedule;
vector<int> gaps_jamie;
vector<int> gaps_cameron;



int main(){
  scanf("%d ", &T);
  for (int cas = 1; cas <= T; cas++){
    schedule.clear();
    gaps_jamie.clear();
    gaps_cameron.clear();
    int time_jamie = 720;
    int time_cameron = 720;

    scanf("%d %d ", &AJ, &AC);
    for(int i=0; i < AJ; i++){
      int a, b;
      scanf("%d %d ", &a, &b);
      schedule.push_back(make_pair(make_pair(a, b), 1));
      time_jamie -= (b - a);
    }

    for(int i=0; i < AC; i++){
      int a, b;
      scanf("%d %d ", &a, &b);
      schedule.push_back(make_pair(make_pair(a, b), 2));
      time_cameron -= (b - a);
    }

    sort(schedule.begin(), schedule.end());
    int switchovers = 0;
    if (AC + AJ > 0){
      int N = AC + AJ;
      for (int i=0; i < schedule.size(); i++){
        switchovers += 1;
        if (schedule[i].second == schedule[(i+1) % N].second){
          switchovers += 1;
          int duration = (1440 + schedule[(i+1)%N].first.first - schedule[i].first.second) % 1440;
          if (schedule[i].second == 1){
            gaps_jamie.push_back(duration);
          }else{
            gaps_cameron.push_back(duration);
          }
        }
      }
      
      sort(gaps_jamie.begin(), gaps_jamie.end());
      sort(gaps_cameron.begin(), gaps_cameron.end());
      for (int i=0 ; i < gaps_jamie.size(); i++){
        if (gaps_jamie[i] <= time_jamie){
          switchovers -= 2;
          time_jamie -= gaps_jamie[i];
        }else break;
      }

      for (int i=0 ; i < gaps_cameron.size(); i++){
        if (gaps_cameron[i] <= time_cameron){
          switchovers -= 2;
          time_cameron -= gaps_cameron[i];
        }else break;
      }
      printf("Case #%d: %d\n", cas, switchovers);
    }else{
      printf("Case #%d: %d\n", cas, 2);
    }

  }
  return 0;
}

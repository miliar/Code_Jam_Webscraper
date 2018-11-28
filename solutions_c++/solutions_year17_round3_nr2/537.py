#include <cassert>
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

class ActivitySlot {
  public:
  int start;
  int end;
  bool isHusband;
    ActivitySlot(int s, int e, bool iH) {
      start = s;
      end = e;
      isHusband = iH;
    };
};

struct less_than_key
{
    inline bool operator() (const ActivitySlot& struct1, const ActivitySlot& struct2)
    {
        return (struct1.start < struct2.start);
    }
};

class Solver {
 public:
  void Solve() {
    int hAC, wAC;
    vector<ActivitySlot> hA;
    vector<ActivitySlot> wA;
    vector<ActivitySlot> activities;
    vector<int> hHoles;
    vector<int> wHoles;
    bool didHusbandStart = false;
    bool isHusbandOnDuty = false;
    int switches = 0, husbandTime = 0, wifeTime = 0;

    cin >> hAC >> wAC;
    if (hAC == 0 && wAC == 0) {
      cout<<"1"<<endl;
      return;
    }
    for(int i=0; i < hAC; ++i) {
      int start, end;
      cin>>start>>end;
      activities.push_back(ActivitySlot(start, end, true));
    }
    for(int i=0; i < wAC; ++i) {
      int start, end;
      cin>>start>>end;
      activities.push_back(ActivitySlot(start, end, false));
    }
    
    std::sort(activities.begin(), activities.end(), less_than_key());
    
    isHusbandOnDuty = activities[0].isHusband;
    didHusbandStart = activities[0].isHusband;
    int currentStart = activities[0].start;
    for (int i = 0; i < activities.size(); i++) {
      while(i+1 < activities.size() && activities[i].isHusband == activities[i+1].isHusband) {
        int gap = activities[i+1].start - activities[i].end;
        if (activities[i].isHusband) {
          hHoles.push_back(gap);
        } else {
          wHoles.push_back(gap);
        }
        i++;
      }
      int slotTime = activities[i].end - currentStart;
      if (activities[i].isHusband) {
        husbandTime += slotTime;
      } else {
        wifeTime += slotTime;
      }
     
      if (i < activities.size() - 1) {
        if (activities[i].isHusband != activities[i+1].isHusband) {
          switches++;
        }
        currentStart = activities[i+1].start;
      }
    }
    if (activities[0].isHusband == activities[activities.size() -1].isHusband) {
      int gap = activities[0].start;
      gap += (24*60 - activities[activities.size() - 1].end);
      if (didHusbandStart) {
        husbandTime += gap;
        hHoles.push_back(gap);
      } else {
        wifeTime += gap;
        wHoles.push_back(gap);
      }
    } else {
      switches++;
    }
     
    if (husbandTime > 720) {
      std::sort(hHoles.begin(), hHoles.end());
      int holesUsed = hHoles.size()-1;
      while(husbandTime > 720) {
        husbandTime -= hHoles[holesUsed];
        switches += 2;
        holesUsed--;
      }
    }
    
    if (wifeTime > 720) {
      std::sort(wHoles.begin(), wHoles.end());
      int holesUsed = wHoles.size()-1;
        //cout<<wHoles.size()<<endl;
      while(wifeTime > 720) {
        //cout<<holesUsed<<endl;
        wifeTime -= wHoles[holesUsed];
        switches += 2;
        holesUsed--;
      }
    }
    cout<<switches<<endl;
  }
};

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; ++t) {
    Solver solver;
    cout << "Case #" << t + 1 << ": ";
    solver.Solve();
  }
}

#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<iomanip>

using namespace std;

class Act {
public:
  int start;
  int end;
  char type;
  int position;
  char nextType;
  int timeToNext;
  bool filled;

  Act() {

  }

  Act(int s, int e, char t) {
    this->start = s;
    this->end = e;
    this->type = t;
    // this->position = -1;
    this->nextType  = 'x';
    this->timeToNext  = -1;
    this->filled  = false;
  }

  void print(int i) {
    cout << "-Activity " << i << "-" << endl;
    cout << "start: " << this->start << endl;
    cout << "end: " << this->end << endl;
    cout << "type: " << this->type << endl;
    // cout << "position: " << this->position << endl;
    cout << "nextType: " << this->nextType << endl;
    cout << "timeToNext: " << this->timeToNext << endl;
    cout << "filled: " << this->filled << endl;
  }
};

bool comp(Act a, Act b) {
  return a.start < b.start;
}


bool comp2(Act a, Act b) {
  return a.timeToNext < b.timeToNext;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    int Ac, Aj;
    cin >> Ac >> Aj;
    int N = Ac + Aj;
    vector<Act> act = vector<Act>(N);
    for (int i = 0; i < Ac; ++i) {
      int s, e;
      cin >> s >> e;
      Act a = Act(s, e, 'c');
      act[i] = a;
    }
    for (int i = Ac; i < Aj + Ac; ++i) {
      int s, e;
      cin >> s >> e;
      Act a = Act(s, e, 'j');
      act[i] = a;
    }


    sort (act.begin(), act.end(), comp);



    int remainingCTime = 720;
    int remainingJTime = 720;
    for (int i = 0; i < N; ++i) {
      if (act[i].type == 'c') remainingCTime -= act[i].end - act[i].start;
      if (act[i].type == 'j') remainingJTime -= act[i].end - act[i].start;
      act[i].nextType = act[(i + 1)%N].type;
      // act[i].position = i;
      if (i == N - 1) {
        int ttn = 24*60 - act[i].end;
        ttn += act[0].start;
        act[i].timeToNext = ttn;
      } else {
        act[i].timeToNext = act[i + 1].start - act[i].end;
      }
    }


    sort (act.begin(), act.end(), comp2);

    for (int i = 0; i < N; ++i) {
      if (act[i].type == 'c' && act[i].nextType == 'c') {
        if (act[i].timeToNext <= remainingCTime) {
          remainingCTime -= act[i].timeToNext;
          act[i].filled = true;
        }
      }
      if (act[i].type == 'j' && act[i].nextType == 'j') {
        if (act[i].timeToNext <= remainingJTime) {
          remainingJTime -= act[i].timeToNext;
          act[i].filled = true;
        }
      }
    }

    int sol = 0;
    for (int i = 0; i < N; ++i) {
      Act a = act[i];
      if (a.type != a.nextType) sol++;
      if (a.type == a.nextType and not a.filled) sol += 2;
    }


    // for (int i = 0; i < N; ++i) {
    //   act[i].print(i);
    // }

    cout << "Case #" << t << ": " << sol << endl;
  }
  return 0;
}

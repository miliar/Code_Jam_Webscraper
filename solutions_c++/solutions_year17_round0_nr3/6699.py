#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
#include <queue>

using namespace std;

void stalls(int &y, int &z)
{
 int N, K;
  int num_stalls = N+2;
  vector<bool> stalls;
  vector<int> min_s;
  vector<int> max_s;

  // setup
  stalls.resize(num_stalls, false);
  stalls[0] = true;
  stalls[num_stalls-1] = true;
  min_s.resize(num_stalls, INT_MIN);
  max_s.resize(num_stalls, INT_MIN);

  for (int person = 0; person < K; person++) {
    fill(min_s.begin(), min_s.end(), INT_MIN);
    fill(max_s.begin(), max_s.end(), INT_MIN);

    int left_stall = 0;
    int starting = 1;
    for (; starting < num_stalls; starting++) {
      if (!stalls[starting]) {
        left_stall = starting - 1;
        break;
      }
    }

    int right_stall = num_stalls -1;
    for (int i = starting; i < num_stalls; i++) {
      if (stalls[i]) {
        right_stall = i;
        break;
      }
    }

    for (int i = starting; i < num_stalls; i++) {
      //cout << "iter " << i << " " << starting << " " << left_stall << " " << right_stall << endl;
      if (stalls[i]) {
        left_stall = i;
        for (int j = i+1; j < num_stalls; j++) {
          if (stalls[j]) {
            right_stall = j;
            break;
          }
        }      
      } else {
        min_s[i] = std::min(i - left_stall - 1, right_stall - i - 1);
        max_s[i] = std::max(i - left_stall - 1, right_stall - i - 1);
      }
    }
    
    /*
    for (int i = 0; i < num_stalls; i++) {
      if (stalls[i]) {
        cout << "[" << min_s[i] << "," << max_s[i] << "]";
      } else {
        cout << "(" << min_s[i] << "," << max_s[i] << ")";
      }
    }
    cout << endl;

    for (int i = 0; i < num_stalls; i++) {
      if (stalls[i]) {
        cout << "X";
      } else {
        cout << "O";
      }
    }
    cout << endl;
    */

    int best_min_s = *max_element(min_s.begin(), min_s.end());
    vector<int>farthest_closest;
    for (int i = starting; i < num_stalls; i++) {
      if (min_s[i] == best_min_s) {
        farthest_closest.push_back(i);
      }
    }
  
    int final_location = -1;
    if (farthest_closest.size() == 1) {
      final_location = farthest_closest[0];
    } else {
      int best_max_s = INT_MIN;
      for (int i : farthest_closest) {
        if (max_s[i] > best_max_s) {
          best_max_s = max_s[i];
        }
      }

      vector<int>farthest_farthest;
      for (int i : farthest_closest) {
        if (!stalls[i] && max_s[i] == best_max_s) {
          farthest_farthest.push_back(i);
        }
      }

      final_location = farthest_farthest[0];
    }

    stalls[final_location] = true;
    //cout << "location " << final_location << endl;
    if (person == K -1) {
      y = max_s[final_location];
      z = min_s[final_location];
    }
  }
}

class Compare
{
public:
  // a < b
  bool operator()(pair<int,int> &a, pair<int,int> &b) 
  {
    int a_w = get<1>(a);
    int b_w = get<1>(b);
    if (a_w < b_w) {
      return true;
    } else if (a_w == b_w && get<0>(a) > get<0>(b)) {
      return true;
    }

    return false;
  }
};
void place(int &y, int &z) {
  int N;
  cin >> N;
  int K;
  cin >> K;

  if (N == K) {
    y = 0;
    z = 0;
    return;
  }

  vector<bool>stalls;
  int num_stalls = N +2;
  stalls.resize(num_stalls, false);
  stalls[0] = true;
  stalls[N+1] = true;

  // index of left boundary, and the size
  priority_queue<pair<int,int>, vector<pair<int,int>>, Compare> gaps;
  gaps.push(make_pair(0, N));

  int last_place_i = 0;
  for (int person = 0; person < K; person++) {
    auto &best_gap = gaps.top();
    int best_gap_st = get<0>(best_gap);
    int best_gap_w = get<1>(best_gap);

    int middle, gap_left, gap_right;
    
    int total_w = best_gap_w + 2;
    if (total_w % 2 == 0) {
      middle = total_w / 2 - 1 + best_gap_st;
    } else {
      middle = total_w / 2 + best_gap_st;
    }

    gap_left = middle - 1 - best_gap_st;
    gap_right = total_w - (middle - best_gap_st) - 2;
    stalls[middle] = true;

    gaps.pop();
    gaps.push(make_pair(middle, gap_right));
    gaps.push(make_pair(best_gap_st, gap_left));
    last_place_i = middle;
    /*
    for (auto &gap : gaps) {
      cout << get<0>(gap) << " " << get<1>(gap) << endl;
    }
    cout << endl;
    */
  }

  int ls = 0;
  int rs = 0;
  for (int l = last_place_i - 1; l >=0; l--) {
    if (stalls[l]) {
      break;
    }
    ls++;
  }

  for (int r = last_place_i + 1; r < num_stalls; r++) {
    if (stalls[r]) {
      break;
    }
    rs++;
  }

  y = max(ls, rs);
  z = min(ls, rs);
  /*
  for (int i = 0; i < num_stalls; i++) {
    cout << stalls[i] ? "X" : "O";
  }
  cout << endl;
  */
}

int main()
{
  //build_matrix(10);

  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    int y,z;
    //stalls(y,z);
    place(y,z);
    cout << "Case #" << i << ": ";
    cout << y << " " << z << endl;
  }

  return 0;
}


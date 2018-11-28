#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>
#include <queue>
#include <unordered_set>

using namespace std;

int convert(const string& s) {
  int n = static_cast<int>(s.length());
  int ans = 0;

  for (int i = 0; i < n; ++i) {
    if (s[i] == '-') {
      ans = ans * 2;
    } else {
      ans = ans * 2 + 1;
    }
  }

  return ans;
}

int main () {
  int t;
  cin >> t;
  int count = 0;

  string temp;
  getline(cin, temp);

  while (t > 0) {
    --t;
    ++count;
    string str;
    getline(cin, str);
    auto pos = str.find(' ');
    string s = str.substr(0, pos);
    temp = str.substr(pos + 1);
    int k = atoi(temp.c_str());

    int x = convert(s);
    int target = static_cast<int>(pow(2, static_cast<int>(s.length()))) - 1;

    bool found = false;

    queue<pair<int, int>> mq;  // first number is config, second is distance
    unordered_set<int> ms;
    mq.emplace(make_pair(x, 0));
    ms.emplace(x);

    while (!mq.empty()) {
      auto pair = mq.front();
      mq.pop();
      int val = pair.first;
      int dist = pair.second;
      // cout << "val = " << val << ", dist = " << dist << endl;

      if (val == target) {
        cout << "Case #" << count << ": " << dist << endl;
        found = true;
        break;
      } else {
        int key = static_cast<int>(pow(2, k)) - 1;
        // cout << "key = " << key << endl;
        do {
          int num = val ^ key;
          // cout << "num = " << num << endl;
          if (ms.find(num) == ms.end()) {
            // Add into queue + set
            ms.emplace(num);
            mq.emplace(num, dist + 1);
          }
          key = (key << 1);
        } while (key <= target);
        // Start flipping bits and make sure it's not on the set before adding to the queue
      }
    }

    if (!found) {
      cout << "Case #" << count << ": IMPOSSIBLE" << endl; 
    }
    // cout << s << "|" << temp << "|" << endl;
  }

  return 0;
}

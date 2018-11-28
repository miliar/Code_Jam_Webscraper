#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <map>

int T;
typedef long long int dulong;

dulong N, K;
std::map<dulong, dulong> count;
dulong maxLR, minLR;


int main(int argc, const char* argv[]) {

  std::cin >> T;
  for (int i = 1; i <= T; i++) {
     std::cin >> N >> K;
     count.clear();
     count.insert(std::pair<dulong, dulong>(0 - N, 1));
     while (1) {
        std::map<dulong,dulong>::iterator it = count.begin();
        dulong cur = 0 - (it->first);
        dulong cur_count = it->second;
        count.erase(it);
        if (cur_count >= K) {
           minLR = (cur - 1) / 2;
           maxLR = cur / 2;
           break;
        }
        else {
           K = K - cur_count;
           dulong minTmp = (cur - 1) / 2;
           dulong maxTmp = cur / 2;
           if (minTmp > 0)
              count[0 - minTmp] += cur_count;
           if (maxTmp > 0)
              count[0 - maxTmp] += cur_count;
        }
     }
           
     std::cout << "Case #" << i << ": " << maxLR << " " << minLR << std::endl;
  }
  return 0;
}


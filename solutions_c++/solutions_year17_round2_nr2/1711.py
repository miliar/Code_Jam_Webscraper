#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <vector>
#include <map>

int T;
typedef unsigned long long int ullong;
std::map<int, char> mymap;
int N, R, O, Y, G, B, V;

int main(int argc, const char* argv[]) {

  std::cin >> T;
  for (int i = 1; i <= T; i++) {
     std::cin >> N >> R >> O >> Y >> G >> B >> V;
     std::cout << "Case #" << i << ": ";
     mymap.clear();
     mymap[R] = 'R';
     //mymap[O] = 'O';
     mymap[Y] = 'Y';
     //mymap[G] = 'G';
     mymap[B] = 'B';
     //mymap[V] = 'V';
     int mynum[3];
     char mychar[3];

     mynum[0] = R;
     mynum[1] = Y;
     mynum[2] = B;

     mychar[0] = 'R';
     mychar[1] = 'Y';
     mychar[2] = 'B';

     for (int j = 0; j <= 1; j++)
        for (int k = j + 1; k <= 2; k++)
           if (mynum[j] > mynum[k]) {
              int tmp = mynum[j];
              mynum[j] = mynum[k];
              mynum[k] = tmp;
              char tm = mychar[j];
              mychar[j] = mychar[k];
              mychar[k] = tm;
           }


     
     int max, min, medium;
     char max_char, min_char, medium_char;
     min = mynum[0];
     min_char = mychar[0];
     medium = mynum[1];
     medium_char = mychar[1];
     max = mynum[2];
     max_char = mychar[2];

     int num = min;
     if ((num == 0) && (max - medium >= 1)) {
        std::cout << "IMPOSSIBLE" << std::endl;
        continue;
     }
     if (max - medium > 1) {
        int diff = max - (medium + 1);
        if (diff >= min) {
           std::cout << "IMPOSSIBLE" << std::endl;
           continue;
        }
        for (int j = 0; j < diff; j++)
           std::cout << min_char << max_char;
        max = max - diff;
        min = min - diff;
        num = min;
     }

     max -= num;
     medium -= num;
     
     if (max - medium > 1) {
        std::cout << "IMPOSSIBLE" << std::endl;
        continue;
     }
     
     for (int j = 0; j < num; j++)
        std::cout << min_char << max_char << medium_char;
     for (int j = 0; j < medium; j++)
        std::cout << max_char << medium_char;
     max = max - medium;
     if (max > 0)
        std::cout << max_char;
     std::cout << std::endl;
  }
  return 0;
}


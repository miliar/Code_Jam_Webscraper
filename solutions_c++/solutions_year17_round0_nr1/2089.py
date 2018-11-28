#include <iostream>
#include <algorithm>
#include <string>
#include <queue>

int T;
int K;
std::string S;
int a[10001];

bool compute();
void preprocess();

int main(int argc, const char* argv[]) {

  std::cin >> T;
  for (int i = 1; i <= T; i++) {
     std::cin >> S >> K;
     for (int j = 0; j < S.size(); j++) {
        if (S[j] == '-')
           a[j] = 0;
        else
           a[j] = 1;
     }
     int num = 0;
     int N = S.size();
     for (int j = 0; j < N; j++) {
        if (a[j] == 0) {
           ++num;
           if (N - j < K) {
              for (int l = j; l < N; l++)
                 if (a[l] == 0) {
                    num = -1;
                    break;
                 }
           }
           else
           for (int l = j; l < j + K; l++) 
              a[l] = 1 - a[l];
        }
        if (num == -1)
           break;
     }
     if (num == -1)
       std::cout << "Case #" << i << ": IMPOSSIBLE" << std::endl;
     else
       std::cout << "Case #" << i << ": " << num << std::endl;
  }
  return 0;
}


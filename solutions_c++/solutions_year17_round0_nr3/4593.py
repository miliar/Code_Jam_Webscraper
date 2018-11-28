#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <queue>


int main(int argc, char* argv[])
{
  int ncases = 0;
  std::cin >> ncases;

  std::ofstream out;
  out.open("result.txt");
  for(int kase = 0; kase < ncases; kase++)
  {
    int N = 0;
    int K = 0;
    std::cin >> N >> K;
    std::cout << "N: " << N << " K: " << K << std::endl;
    std::priority_queue<int> q;
    q.push(N);
    int max_last_segment = 0;
    int min_last_segment = 0;
    for(int people = 0; people < K; people++)
    {
      int max_segment = q.top();
      q.pop();
      int segment1 = (max_segment -1) / 2;
      int segment2 = max_segment - 1 - segment1;
      max_last_segment = std::max(segment1, segment2);
      min_last_segment = std::min(segment1, segment2);
      q.push(segment1);
      q.push(segment2);
    }

    std::cout << "Case #" << (kase + 1) << ": " << max_last_segment << " " << min_last_segment << std::endl;
    out << "Case #" << (kase + 1) << ": " << max_last_segment << " " << min_last_segment << std::endl;
  }

  out.close();
  return 0;
}

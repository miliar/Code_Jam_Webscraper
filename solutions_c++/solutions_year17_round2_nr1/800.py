#include <iostream>
#include <iomanip>

#include <vector>
#include <map>
#include <unordered_map>

using namespace std;

int main()
{
  int T;
  cin >> T;


  for (int i = 0; i < T; i++)
  {
    int64_t D, N;
    cin >> D >> N;
    double speed = 0.0;
    for (int j = 0; j < N; j++)
    {
      int64_t Ki, Si;
      cin >> Ki >> Si;
      double v = D * 1.0 / (D - Ki) * Si;
      if (j == 0) {
        speed = v;
      } else {
        speed = std::min(speed, v);
      }
    }

    cout << "Case #" << i+1 << ": " << setprecision(8) << speed << endl;
  }

  return 0;
}

#pragma GCC optimize ("O2")

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include <iomanip> 

//#define small 
#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;


int main()
{
#if defined(small)
  freopen("A-small-attempt1.in", "r", stdin);
#elif defined(large)
  freopen("A-large.in", "r", stdin);
#endif
  freopen("out.out", "w", stdout);

  int T;
  scanf("%d", &T);
  std::cerr << T << " testcases\n";

  for (int i = 1; i <= T; i++) {
    std::cout << "Case #" << i << ": ";
    std::cerr << "Case #" << i << ": ";

    double D;
    int N;
    scanf("%lf %d", &D, &N);

    double maxTime = 0;
    for (int j = 0; j < N; j++) {
      double K, S;
      scanf("%lf %lf", &K, &S);
      double ETA = (D-K)/S;
      //std::cerr << "\n" << D << " " << K << " " << S << " ETA: " << ETA << " |" << (0==ETA) << "|";
      maxTime = std::max(maxTime, ETA);
    }

    std::cout << std::setprecision(6) << std::fixed << D/maxTime << "\n";
    std::cerr << std::setprecision(6) << std::fixed << D/maxTime << "\n";
  

  }



  printf("\n");
  fprintf(stderr, " \n");

  return 0;
}

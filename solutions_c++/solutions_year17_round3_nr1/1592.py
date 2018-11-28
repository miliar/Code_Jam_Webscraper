#pragma GCC optimize ("O2")

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<iomanip>
#include <utility>

//#define small 
#define large

typedef std::vector<bool> vb;
typedef std::vector<double> vd;
typedef std::vector<int> vi;
typedef std::vector<vi> vvi;
typedef long long ll;

#ifndef M_PI 
#define M_PI    3.14159265358979323846f 
#endif

bool pairCompareFirstSmallFirst(const std::pair<double, double>& firstElem, const std::pair<double, double>& secondElem) {
  return firstElem.first < secondElem.first;
}

bool pairCompareSecondGreatFirst(const std::pair<double, double>& firstElem, const std::pair<double, double>& secondElem) {
  return firstElem.second > secondElem.second;
}

int main()
{
#if defined(small)
  freopen("A-small-attempt0.in", "r", stdin);
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


    int N, K;
    std::scanf("%d %d", &N, &K);
    
    std::vector<std::pair<double, double> > pans(N);
    for (int i = 0; i < N; i++) {
      std::pair<double, double> panTS;
      double R, H;
      scanf("%lf %lf", &R, &H);
      panTS.first = M_PI*R;
      panTS.second = 2*H*panTS.first;
      panTS.first *= R;
      pans[i] = panTS;
    }

    //debug
    //for (auto &pan : pans)
    //std::cerr << pan.first << " | " << pan.second << "\n";
    
    std::sort(pans.begin(), pans.end(), pairCompareFirstSmallFirst);

    //debug
    //for (auto &pan : pans)
    //std::cerr << std::setprecision(9) << std::fixed << pan.first << " | " << pan.second << "\n";
    
    double maxSurface = 0;
    //std::cerr << "\n";
    for (int i = K; i <= N; ++i){
      double thisMax = 0;
      std::vector<std::pair<double, double> > thisPans(pans.begin(), pans.begin()+i);
      //std::cerr << "analyzing " << thisPans.size() << "\n";
      //std::cerr << "bottom : " << thisPans.back().first << " " << thisPans.back().second << "\nsides:\n"; 
      thisMax += thisPans.back().first;
      thisMax += thisPans.back().second;
      thisPans.erase(thisPans.end()-1);
      std::sort(thisPans.begin(), thisPans.end(), pairCompareSecondGreatFirst);
      for (int j = 0; j < K-1; ++j){
	thisMax += thisPans[j].second;
	//std::cerr << thisPans[j].second << "(" << j << ")\n";
      }	
      maxSurface = std::max(maxSurface, thisMax);
    }
    

    

    std::cout << std::setprecision(9) << std::fixed << maxSurface << "\n";
    std::cerr << std::setprecision(9) << std::fixed << maxSurface << "\n";
    //printf("\n");
    //fprintf(stderr, " \n");
  }
  
  return 0;
}

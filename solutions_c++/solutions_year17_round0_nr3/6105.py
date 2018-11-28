#pragma GCC optimize ("O2")

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include <functional>
#include <queue>

#define small 
//#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;

int main()
{
#if defined(small)
  freopen("C-small-2-attempt1.in", "r", stdin);
#elif defined(large)
  freopen("C-large.in", "r", stdin);
#endif
  freopen("out.out", "w", stdout);

  int T;
  scanf("%d", &T);
  
  std::cerr << T << " testcases\n";
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    fprintf(stderr, "Case #%d: ", t);
    
    int N, K;
    scanf("%d %d", &N, &K);
    
    std::priority_queue<int> empt;
    empt.push(N);
    
    for (int i = 0; i < K-1; i++) {
      int maxEmpt = empt.top();
      empt.pop();
      //std::cerr << "max empt " << maxEmpt << "\n";
      empt.push(maxEmpt/2);
      empt.push((maxEmpt-1)/2);
    }

    int maxEmpt = empt.top();
    //std::cerr << "max empt (final) " << maxEmpt << "\n";

    printf("%d %d", maxEmpt/2, (maxEmpt-1)/2);
    printf("\n");

    fprintf(stderr, "%d %d", maxEmpt/2, (maxEmpt-1)/2);
    fprintf(stderr, " \n");

    /*
    vi empt;
    empt.push_back(N);

    for (int i = 0; i < K-1; i++) {
      int maxEmpt = 0, del;
      for (int j = 0; j < empt.size(); ++j){
	if (empt[j] > maxEmpt){
	  maxEmpt = empt[j];
	  del = j;
	}
      }
      //std::cerr << "max empt " << maxEmpt << "\n";
      empt.erase(empt.begin()+del);
      empt.push_back(maxEmpt/2);
      empt.push_back((maxEmpt-1)/2);
    }

    int maxEmpt = 0;
    for (int j = 0; j < empt.size(); ++j){
      if (empt[j] > maxEmpt){
	  maxEmpt = empt[j];
      }
    }
    //std::cerr << "max empt (final) " << maxEmpt << "\n";

    printf("%d %d", maxEmpt/2, (maxEmpt-1)/2);
    printf("\n");

    fprintf(stderr, "%d %d", maxEmpt/2, (maxEmpt-1)/2);
    fprintf(stderr, " \n");
    */
  }
  return 0;
}

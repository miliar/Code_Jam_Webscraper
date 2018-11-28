#pragma GCC optimize ("O2")

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>

//#define small 
#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;


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
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    fprintf(stderr, "Case #%d: ", t);

    std::string pancakes;
    std::cin >> pancakes;
    //std::cerr << "pancakes: |" << pancakes << "|\n";
    int flip;
    scanf("%d", &flip);

    int moves = 0;
    for (int i = 0; i < pancakes.size(); ++i){
      if (pancakes[i] == '-'){
	//std::cerr << "flipping at " << i << "\n";
	++moves;
	if (i+flip > pancakes.size()){
	  moves = -1;
	  break;
	}
	for (int j = i; j < i+flip; ++j){
	  if (pancakes[j] == '-')
	    pancakes[j] = '+';
	  else
	    pancakes[j] = '-';
	}
	//std::cerr << "pancakes: |" << pancakes << "|\n";
      }
    }

    if (moves != -1){
      printf("%d", moves);
      fprintf(stderr, "%d", moves);
    } else {
      printf("IMPOSSIBLE");
      fprintf(stderr, "IMPOSSIBLE");
    }
    
    printf("\n");
    fprintf(stderr, " \n");
  }
  return 0;
}

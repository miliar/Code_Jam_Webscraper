#pragma GCC optimize ("O2")

#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<string>

#define small 
//#define large

typedef std::vector<bool> vb;
typedef std::vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;

bool tidy(int &num){
  std::string str = std::to_string(num);
  int maxDigit = 0;
  for (int i = 0; i < str.size(); ++i){
    if (str[i] < maxDigit)
      return false;
    maxDigit = str[i];
  }
  return true;
}


int main()
{
#if defined(small)
  freopen("B-small-attempt0.in", "r", stdin);
#elif defined(large)
  freopen("B-large.in", "r", stdin);
#endif
  freopen("out.out", "w", stdout);

  int T;
  scanf("%d", &T);
  
  std::cerr << T << " testcases\n";
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    fprintf(stderr, "Case #%d: ", t);

    int N;
    scanf("%d", &N);

    int maxNum;
    for (int i = 1; i <= N; i++) {
      if (tidy(i))
	maxNum = i;
    }

    printf("%d", maxNum);
    fprintf(stderr, "%d", maxNum);

    /*
    std::string num;
    std::cin >> num;

    for (int i = 0; i < str.size(); i++) {
      if (overflowing){
	std::printf("9");
	std::fprintf("9");
	continue;
      }
      char maxDigitToCome = '0';
      for (int j = i; j < str.size(); j++)
	maxDigitToCome = std::max(str[j], maxDigitToCome);
      if (maxDigitToCome == '0')
	overflowing = true;
      else {
	printf("%d", std::max(str[i], maxDigitToCome));
	fprintf(stderr, "%d", std::max(str[i], maxDigitToCome));
      }
      
    }
    */

    printf("\n");
    fprintf(stderr, " \n");
  }
  return 0;
}

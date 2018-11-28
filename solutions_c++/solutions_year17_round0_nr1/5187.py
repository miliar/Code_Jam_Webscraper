#include <stdio.h>

#include <vector>

using namespace std;

int process(char * line, int k) {
  
  int flips = 0;

  int s = strlen(line);
  
  vector<int> limits;

  int lp = -1;
  int sign = 1;
  int limit = -1;
  
  for (int pos = 0; pos < s; pos++) {

    //    printf("Pos = %d limit = %d sign = %d\n",1+pos,1+limit, sign);
    
    if (((line[pos] == '-') && (sign == 1)) ||
	((line[pos] == '+') && (sign == -1))) {
      // need to flip;
      // printf("Flip at pos %d\n",pos+1);
      flips++;
      sign *= -1;
      limits.push_back(pos + k-1);
      if (limit == -1) {
	limit = pos + k -1;
	lp = limits.size() - 1;
      }
    }
    
    if (pos == limit) {
      sign *= -1;
      lp++;      
      if (limits.size() == lp) {
	sign = 1;
	limit = -1;
      }
      else {
	limit = limits[lp];
      }
    }    
  }
  
  if ((limits.size()> 0) && (limits.back() >= s)) {
    
    // printf("Limits size = %lu - %d\n",limits.size(),(lp+1));
    return -1;
  }
  
  return flips;
}

int main() {

  int T;

  scanf("%d",&T);
  
  for (int t = 1; t <= T; t++) {

    int flips = 0;
    char line[1010];
    int k = 0;
    
    scanf("%s %d",line,&k);
    
    flips = process(line,k);
    
    if (flips >= 0) {
      printf("Case #%d: %d\n",t,flips);
    }
    else {
      printf("Case #%d: IMPOSSIBLE\n",t);
    }
  }
    
  


}

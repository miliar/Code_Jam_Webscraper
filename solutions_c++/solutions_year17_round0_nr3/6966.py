#include <iostream>
#include <vector>
#include <algorithm>

struct st {
  int l;
  int r;
  int min;
  int max;
};

int main() {
  int tc;
  std::cin>>tc;
  int ca = 1;

  while (tc) {
    int N, K;
    std::cin >> N >>  K;

    std::vector<bool> stalls(N + 2, true);

    stalls[0] = stalls[N+1] = false;

    for (int k = 0;  k < K; ++k) {
      std::vector<st> status(N + 2, st());

      int l_c = 0;
      for (int n = 0; n < N + 2; ++n) {
	if (stalls[n]) {
	  l_c++;
	  status[n].l = l_c;
	} else {
	  l_c = 0;
	}
      }
      l_c = 0;
      for (int n = N + 2 - 1; n >= 0; --n) {
	if (stalls[n]){
	  l_c++;
	  status[n].r = l_c;
	} else {
	  l_c = 0;
	}
      }
      int desired = -1;
      int max_min = -1;
      int max_max = -1;
      for (int n = 0; n < N + 2; ++n) {
	status[n].max = std::max(status[n].l, status[n].r);
	status[n].min = std::min(status[n].l, status[n].r);

	if (max_min == -1 || status[n].min > max_min ||
	    (status[n].min == max_min && status[n].max > max_max)) {
	  max_min = status[n].min;
	  max_max = status[n].max;
	  desired = n;
	}
       
      }

      stalls[desired] = false;
      if (k==K-1) {
	std::cout << "Case #" << ca << ": " << max_max - 1 << " " << max_min - 1 << std::endl;
      }
      
    }

    
    --tc;
    ca++;
  }
}

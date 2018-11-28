#include <algorithm>
#include <cstring>
#include <vector>
#include <cmath>

const double PI = acos(-1.0);

struct Pan {
	double suf1, suf2;
	Pan(){}
	Pan(double s1, double s2):suf1(s1), suf2(s2) {}
	bool operator < (const Pan& rhs) const {
	  return suf1 > rhs.suf1;
	}
};

bool cmp(const Pan& a, const Pan& b) {
	return a.suf2 > b.suf2;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
  int T, cas = 1;
  scanf("%d", &T);
  while (T --) {
    int n, k;
    scanf("%d%d", &n, &k);
    std::vector<Pan> v1_, v2_;
    for (int i = 0; i < n; i ++) {
      double r, h; scanf("%lf%lf", &r, &h);
      v1_.push_back(Pan(PI * r * r, 2 * PI * r * h));
    }
    sort(v1_.begin(), v1_.end());
    double ans = 0;
    for (int i = 0; i < n; i ++) {
      v2_.clear();
      for (int j = i + 1; j < n; j ++) {
      	v2_.push_back(v1_[j]);
      }
      sort(v2_.begin(), v2_.end(), cmp);
      double tmp = v1_[i].suf1 + v1_[i].suf2;
      for (int j = i + 1; j < i + k; j ++) {
        tmp += v2_[j - i - 1].suf2;
      }
      ans = std::max(ans, tmp);
    }
    printf("Case #%d: %.15f\n", cas ++, ans);
  }
	return 0; 
}
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <queue>

using namespace std;

typedef struct
{
  int li;
  int dim;
} fs;

class mycomparison
{
  bool reverse;

public:
  mycomparison(const bool &revparam = false)
  {
    reverse = revparam;
  }
  bool operator()(const fs &lhs, const fs &rhs) const
  {
    if (reverse)
      return lhs.dim > rhs.dim;
    else
      return lhs.dim < rhs.dim;
  }
};

int main()
{
  int n = 0;
  cin >> n >> ws;
  for (int i = 0; i < n; i++)
  {
    vector<fs> stack;
    int s, p, ma = 0, mi = 0;
    cin >> s >> ws >> p >> ws;

    // Using lambda to compare elements.
    typedef std::priority_queue<fs, std::vector<fs>, mycomparison> myq;

    myq oc;

    fs in;
    in.li = 0;
    in.dim = s;
    oc.push(in);

    for (int y = 0; y < p; y++)
    {
      fs t = oc.top();
      oc.pop();

      fs re, le;
      le.li = t.li;
      le.dim = (t.dim % 2) == 0 ? (t.dim / 2) - 1 : round(t.dim / 2);

      re.li = t.li + le.dim + 1;
      re.dim = t.dim - le.dim - 1;

      oc.push(le);
      oc.push(re);

      ma = max(le.dim, re.dim);
      mi = min(le.dim, re.dim); 
    }

    cout << "Case #" << i + 1 << ": " << ma << " " << mi << endl;
  }
  return 0;
}
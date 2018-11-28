#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int N; cin >> N;
  for (int ii = 1; ii <= N; ii++)
  {
    unsigned long long n, k; cin >> n >> k;
    unsigned long long s = 1;
    unsigned long long v_even = (n & 1) ? n-1 : n;
    unsigned long long v_odd = (n & 1) ? n : n-1;
    unsigned long long k_even = (n & 1) ? 0 : 1;
    unsigned long long k_odd = (n & 1) ? 1 : 0;
    
    while (s < k)
    {
      unsigned long long v_temp1 = (v_even - 1) / 2;
      unsigned long long v_temp2 = v_temp1 + 1;
      unsigned long long k_temp1 = k_even;
      unsigned long long k_temp2 = k_even;
      if (v_odd < v_even)
        k_temp1 += 2 * k_odd;
      else
        k_temp2 += 2 * k_odd;
      
      if (v_temp1 & 1)
      {
        v_odd = v_temp1;
        k_odd = k_temp1;
        v_even = v_temp2;
        k_even = k_temp2;
      }
      else
      {
        v_odd = v_temp2;
        k_odd = k_temp2;
        v_even = v_temp1;
        k_even = k_temp1;
      }
      k -= s;
      s *= 2;
      //cout << "v_even: " << v_even << ",  v_odd: " << v_odd << endl;
    }
    
    unsigned long long v_min, v_max;
    v_min = v_max = (v_odd - 1) / 2;
    
    if (v_even > v_odd)
    {
      if (k <= k_even)
      {
        v_max ++;
      }
    }
    else
    {
      if (k > k_odd)
      {
        v_min --;
      }
    }
      
    cout << "Case #" << ii << ": ";
    cout << v_max << " " << v_min << endl;
  }
  return 0;
}
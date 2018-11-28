#include <iostream>
#include <math.h>
#include <string.h>
#include <stdio.h>
#include <assert.h>


int main(int argc, char **argv)
{
  int c, T;

  std::cin >> T;
  for(c=1; c<=T; c++)
    {
      int f, l;
      long long N, K, s1, s2;
      long long n[300], m[300];
      std::cin >> N >> K;
      f = 0;
      l = 1;
      n[0] = 1;
      m[0] = N;
      while(K>0)
        {
          int i;
          long long p, q;
          assert(l<295);
          p = m[f];
          q = n[f];
          s1 = p>>1;
          s2 = (p-1)>>1;
          m[f] = n[f] = 0;
          K -= q;
          for(i=++f; i<l && m[i]>s1; i++)
              ;
          if(i==l)
            {
              n[l] = 0;
              m[l++] = s1;
            }
          n[i] += q;
          while(i<l && m[i]>s2)
              i++;
          if(i==l)
            {
              n[l] = 0;
              m[l++] = s2;
            }
          n[i] += q;
        }
      std::cout << "Case #" << c << ": " << s1 << " " << s2 << "\n";
    }
}

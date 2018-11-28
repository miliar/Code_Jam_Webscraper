#include <stdafx.h>
#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <queue>
#include <set>
#include <map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>


using namespace std;

uint64_t find_last_tidy(int * decom, int num_digits)
{
    uint64_t last_tidy = 0;

    for (int m = 0; m < num_digits-1; m++)
    {
        if (decom[m + 1] > decom[m])
        {
            decom[m + 1] = decom[m + 1] - 1;
            for (int p = m; p >= 0; p--)
            {
                decom[p] = 9;
            }
        }
    }

        for (int q = num_digits - 1; q >= 0; q--)
        {
            last_tidy += decom[q];
            last_tidy = last_tidy * 10;

        }
 
    return  last_tidy/10;
}
int calc_num_digits(uint64_t in)
{
    int num_digits = 0;
    while (in > 0)
    {
        in /= 10;
        num_digits++;
    }
    return num_digits;
}
int main() {
    
    int T;
    cin >> T;
   int decom[18];
        for (int i = 1; i <= (int)T; ++i) 
        {
            
            uint64_t last_tidy=0;
            int N = 0;
            uint64_t n;
            cin >> n;
            if (n >= 0 && n < 10)
            {
                last_tidy = n;
            }
            else
            {
                N=calc_num_digits(n);

                for (int m = 0; m < N; m++)
                {
                    decom[m] = n % 10;
                    n /= 10;
                }

                last_tidy = find_last_tidy(decom, N);
            }
           
            
        cout << "Case #" << i << ": " << last_tidy << '\n';
  
 
    }
    return 0;
}

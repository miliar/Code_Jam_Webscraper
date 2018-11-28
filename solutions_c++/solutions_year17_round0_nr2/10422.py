// prob_b.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <stdio.h>
#include <climits>
#include <cassert>
using namespace std;
#define _CRT_SECURE_NO_WARNINGS

bool check_tidy(unsigned long long num)
{
  bool is_tidy = true;
  unsigned long long temp = num;
  unsigned long long curr = temp%10;
  unsigned long long next = ULLONG_MAX;
  
  while(temp)
  {
    temp /= 10;
    next = temp%10;
    if(curr < next)
    {
      is_tidy = false;
      break;
    }
    curr = next;
  }
  return is_tidy;
}

int _tmain(int argc, _TCHAR* argv[])
{
	FILE* in = NULL;
	FILE* out = NULL;
	errno_t fin = freopen_s(&in, "B-small-attempt0.in", "r", stdin);
	assert(0x0 == fin);
	errno_t fout = freopen_s(&out, "B-small.out", "w", stdout);
	assert(0x0 == fout);
	int T;
  cin >> T;
  
  unsigned long long *N = new unsigned long long[T];
  unsigned long long i;
	for (int t = 0; t < T; t++)
	{
    cin >> N[t];
    for(i = N[t];i > 0;--i)
    {
      if(check_tidy(i))
      {
        break;
      }
    }

		cout << "Case #" << t+1 << ": " << i << endl;
	}
	return 0;
}




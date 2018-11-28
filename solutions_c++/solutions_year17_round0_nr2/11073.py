//
//  main.cpp
//  tidy_number
//
//  Created by Quentin Lee on 2017/4/8.
//  Copyright (c) 2017年 Quentin Lee. All rights reserved.
//

#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;


bool IsTidyNum(long long aInput)
{
  int prevDigit = 10, remain = 0;
  while (aInput)
  {
      remain = aInput % 10;
      if (remain > prevDigit)
      {
          return false;
      }
      prevDigit = remain;
      aInput /= 10;
  }
  return true;
}

long long GetTidyNum(long long aInput)
{
    long long index = aInput;
    for (; index >= 0; --index)
    {
      if (IsTidyNum(index))
      {
          break;
      }
    }
    return index;
}

int main(int argc, const char * argv[]) {
    int testNum;
    cin >> testNum;
    
    for (int i = 1; i <= testNum; ++i)
    {
        long long N;
        cin >> N;
        cout << "Case #" << i << ": " << GetTidyNum(N) << endl;
    }
    
}


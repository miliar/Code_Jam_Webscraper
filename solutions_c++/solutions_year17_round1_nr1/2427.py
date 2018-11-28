
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <stdlib.h>
#include <numeric>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main(int argc, const char * argv[])
{
        if (argc > 1)
        {
            FILE * fp = freopen(argv[1], "r", stdin);
            if (fp == NULL)
            {
                perror(argv[1]);
                exit(1);
            }
        }
     
  int num, numRows, numCols;
  std::string numS;
  getline(cin, numS);
  num = atoi(numS.c_str());

  for (int i = 1; i <= num; ++i)
  {
      cout << "Case #" << i << ":" << endl;
    cin >> numRows >> numCols;
    //getline(cin, firstLineS);
      
      
      std::vector<char> row(numCols);
      std::vector<char> outputRow(numCols);
      int returnR0 = 0;
      
      for (int r = 0; r < numRows; r++)
      {
          //read new line
          cin.get();
          int numQ = 0;
      
          for (int c = 0; c < numCols; c++)
          {
              cin.get(row[c]);
          
              if (row[c] == '?')
                  numQ++;
          }
      
          if (numQ == numCols)
          {
              if (r == 0 || returnR0 > 0) returnR0++;
              else
              {
                  for (int index = 0; index < numCols; index++)
                      cout << outputRow[index];
                  cout << endl;
              }
          }
          
          else
          {
              int start = 0;
              int end = 0;
              char initial = row[0];
              do
              {
                  while (row[start] != '?' && start < numCols)
                  {
                      outputRow[start] = row[start];
                      initial = row[start];
                      start++;
                  }
                  end = start;
                  while (row[end] == '?' && end < numCols) end++;
              
                  for (int pos = start; pos < end; pos++)
                  {
                      if (end != numCols) initial = row[end];
                      outputRow[pos] = initial;
                  }
                  start = end;
               } while (end < numCols);
            
          
              for (int count = returnR0; count > 0; count--)
              {
                  for (int index = 0; index < numCols; index++)
                      cout << outputRow[index];
                  cout << endl;
              }
          
              returnR0 = 0;
              for (int index = 0; index < numCols; index++)
                  cout << outputRow[index];
              cout << endl;
          }
          
          
      }
      
//
//
//    unsigned * numbersV = new unsigned[numDigits];
//
//    for (unsigned index = 0; index < numDigits; index++)
//    {
//      numbersV[index] = largestS[index] - '0';
//    }
//
//    for (signed index = numDigits - 1; index > 0; index--)
//    {
//      unsigned maxDigit = 0;
//      for (unsigned index2 = 0; index2 < index; index2++)
//      {
//        if (numbersV[index2] > maxDigit)
//          maxDigit = numbersV[index2];
//      }
//
//      if (numbersV[index] < maxDigit)
//      {
//        signed tempI = index-1;
//        while (tempI >= 0)
//        {
//          if (numbersV[tempI] == 0)
//          {
//            numbersV[tempI] = 9;
//            tempI--;
//          }
//          else
//          {
//            numbersV[tempI]--;
//            break;
//          }
//        }
//        if (tempI < 0) return -1;
//
//        for (unsigned index2 = index; index2 < numDigits; index2++)
//          numbersV[index2] = 9;
//      }
//    }
//    // Check if possible and output
//    cout << "Case #" << i << ": ";
//    for (int index = 0; index < numDigits; index++)
//    {
//      if (numbersV[index] > 0)
//        cout << numbersV[index];
//    }
//
//    cout << endl;
//
//    delete[] numbersV;
//    int * vec = new int[length];
//    for(unsigned index = 0; index < length; index++)
//    {
//      if (line[index] == '+')
//        vec[index] = 1;
//      else
//        vec[index] = 0;
//    }
//
//    int front = -1, back = length, flips = 0;
//
//    while (true)
//    {
//      // flip at front
//      do ++front;
//      while ((vec[front] == 1) && (front < back));
//
//      if (back - front < width) break;
//
//      flips++;
//      for (int c = 0; c < width; c++)
//        vec[front+c] = !vec[front+c];
//
//      // flip at back
//      do --back;
//      while ((vec[back] == 1) && (back > front));
//
//      if (back - front < width) break;
//
//      flips++;
//      for (int c = 0; c < width; c++)
//        vec[back-c] = !vec[back-c];
//    }
//
//    // Check if possible and output
//    cout << "Case #" << i << ": ";
//    unsigned sum = 0;
//    for (int index = 0; index < length; index++)
//      sum += vec[index];
//
//    if (sum == length)
//      cout << flips << endl;
//    else
//      cout << "IMPOSSIBLE" << endl;
//
//    delete vec;

    //cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

  return 0;
}

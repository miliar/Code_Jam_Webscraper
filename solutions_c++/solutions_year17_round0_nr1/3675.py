
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <stdlib.h>
#include <numeric>

using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main()
{
  int num, width;
  std::string widthS, line, numS;
  getline(cin, numS);
  num = atoi(numS.c_str());

  for (int i = 1; i <= num; ++i)
  {
    //cin >> order >> width;
    getline(cin, line, ' ');
    getline(cin, widthS);
    width = atoi(widthS.c_str());
    int length = line.size();

    int * vec = new int[length];
    for(unsigned index = 0; index < length; index++)
    {
      if (line[index] == '+')
        vec[index] = 1;
      else
        vec[index] = 0;
    }

    int front = -1, back = length, flips = 0;

    while (true)
    {
      // flip at front
      do ++front;
      while ((vec[front] == 1) && (front < back));

      if (back - front < width) break;

      flips++;
      for (int c = 0; c < width; c++)
        vec[front+c] = !vec[front+c];

      // flip at back
      do --back;
      while ((vec[back] == 1) && (back > front));

      if (back - front < width) break;

      flips++;
      for (int c = 0; c < width; c++)
        vec[back-c] = !vec[back-c];
    }

    // Check if possible and output
    cout << "Case #" << i << ": ";
    unsigned sum = 0;
    for (int index = 0; index < length; index++)
      sum += vec[index];

    if (sum == length)
      cout << flips << endl;
    else
      cout << "IMPOSSIBLE" << endl;

    delete vec;

    //cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

  return 0;
}

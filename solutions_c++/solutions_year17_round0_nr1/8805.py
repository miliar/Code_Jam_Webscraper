#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int K;
unordered_map<string,int> cache;
int num_flips(string input)
{
     bool done = true;
     for(int i=0; i<input.length(); i++)
          if(input[i]!='+')
          {
               done = false;
               break;
          }
     if(done)
          return 0;

     if(cache.count(input))
          return cache[input];

     int min_flips = -1;
     cache[input] = -1;
     for(int i=0; i<input.length()-K+1; i++)
     {
          string flipped = input;
          for(int j=i; j<i+K; j++)
               flipped[j] = (flipped[j]=='+' ? '-' : '+');
          int future_flips = num_flips(flipped);
          if(future_flips!=-1)
               if(future_flips < min_flips || min_flips==-1)
                    min_flips = future_flips;
     }

     if(min_flips==-1)
          cache[input] = -1;
     else
          cache[input] = min_flips + 1;
     return cache[input];
}

int main()
{
     int cases;
     cin >> cases;

     for(int z=0; z<cases; z++)
     {
          cache.clear();
          string input;
          cin >> input >> K;
          int flips = num_flips(input);
          cout << "Case #" << z+1 << ": " << (flips==-1 ? "IMPOSSIBLE" : to_string(flips)) << endl;
     }
          
     return 0;
}

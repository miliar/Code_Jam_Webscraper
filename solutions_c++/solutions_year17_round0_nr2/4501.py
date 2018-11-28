#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  int n = 0;
  cin >> n >> ws;
  for (int i = 0; i < n; i++)
  {
    string c;
    cin >> c >> ws;
    int min = 0;
    for (int j = 0; j < c.size() - 1; j++)
    {
      if(c[j] > c[j+1]){
        c[j]--;
        for(int k = j + 1; k < c.size() ; k ++){
          c[k]='9';
        }
        break;
      } 
    }
    for( int j = c.size() - 1; j > 0; j--){
      if(c[j] < c[j - 1]) {
        c[j]='9';
        c[j-1]--;
      }
    }
    cout << "Case #" << i + 1 << ": " << stol(c) << endl;
  }
  return 0;
}
#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int n,m,count=0,i;
  string cake;
  cin >> n;

  for (int k = 0; k < n; k++) {
    i = 0;
    cin >> cake;
    cin >> m;
    count = 0;
    while (i <= cake.length()-m) {
      if (cake[i] == '-') {
        for (int j = 0; j < m; j++) {
          if (cake[i+j] == '-') {
            cake[i+j] = '+';
          }else cake[i+j]= '-';
        }
        count = count + 1;
      }
      i++;
    }

    for (int j = 0; j < cake.length(); j++) {
      if (cake[j] == '-') {
        cout << "Case #" << k+1 << ": "<< "IMPOSSIBLE"<<endl;
        break;
      }
      if (j == cake.length()-1) {
        cout << "Case #" << k+1 << ": "<< count << endl;
      }
    }

  }
  return 0;
}

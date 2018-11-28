#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <stdio.h>

using namespace std;

int T;
FILE * result;

string convertInt(int number);
int func(int x);
void quickSort(string &arr, int left, int right);

int main()
{
    cin >> T;

    result = fopen("outSmallB.txt", "w");

    for(int i = 1; i <= T; i++){
      func(i);
    }

    return 0;
}

int func(int x){
    int N;
    cin >> N;
    while(true){
      string n = convertInt(N);
      quickSort(n, 0,n.size()-1);
      if(atoi(n.c_str()) == N) break;
      N -= 1;
    }

    //cout << "Case #" << x << ": " << N << endl;
    fprintf(result, "Case #%d: %d\n", x, N);
}

string convertInt(int number){
   stringstream ss;
   ss << number;
   return ss.str();
}

void quickSort(string &arr, int left, int right) {
      int i = left, j = right;
      char tmp;
      char pivot = arr[(left + right) / 2];

      /* partition */
      while (i <= j) {
            while (arr[i] < pivot)
                  i++;
            while (arr[j] > pivot)
                  j--;
            if (i <= j) {
                  tmp = arr[i];
                  arr[i] = arr[j];
                  arr[j] = tmp;
                  i++;
                  j--;
            }
      };
      /* recursion */
      if (left < j)
            quickSort(arr, left, j);
      if (i < right)
            quickSort(arr, i, right);
}

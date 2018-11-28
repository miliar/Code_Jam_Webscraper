#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>\
#include<algorithm>
using namespace std;
int N;
int first[100010];
int second[100010];
int main() {
   int T;
   cin>> T;
   while (T--) {
      cin >> N;
      for (int i = 0; i < N; i++) {
         cin >> first[i]; //부호 개수
         total += abs(first[i]);
      }

      for (int i = 0; i < N; i++) {
         cin >> second[i];
         total -= abs(second[i]);
      }


//

      half = N/2;

      cout <<"Case #1:"<<endl;
      for (int i = 0; i < half; i++)
         digit[i] = '0';
      flag = false;
      digit[0] = '1';
      makeDigit(1, 1);
   }
   return 0;
}

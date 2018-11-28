#include<iostream>
#include<string>
using namespace std;

void reverse(string& S, int l, int r);
void output(int x, int y) ;
int solve(string S, int K) ;

int main() {
   int T;
   cin >> T;

   for (int i = 1; i <= T; i++) {
      string S;
      int K;
      cin >> S >> K;
      int count = solve(S, K);
      output(i, count);
   }

   return 0;
}

void output(int x, int y) {
   cout << "Case #" << x << ": ";
   
   switch (y) {
      case -1:
         cout << "IMPOSSIBLE";
         break;
      default:
         cout << y;
   }
   cout << endl;
}

int solve(string S, int K) {
   int length = S.size();
   int count = 0;
   int i;
   
   for (i = 0; i < (length-K+1); i++) {
      if (S[i] == '+') {
         continue;
      } else {
         reverse(S, i, i+K);
         count++;      }
   }
   if (i == length) {
      return count;
   }
   for (;i < length; i++) {
      if (S[i] == '-') {
         return -1;
      }
   }
   return count;
}

void reverse(string& S, int l, int r) {
   for (int i = l; i < r; i++) {
      if (S[i] == '-') {
         S[i] = '+';
      } else {
         S[i] = '-';
      }
   }
}

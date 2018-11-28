#include<iostream>
#include<string>
using namespace std;

void check(string& N, int length, int l, int r) ;
void output(int x, string y);
void solve(string& N);
void nine(string& N, int length, int r);

int main() {
   int T;
   cin >> T;
   for (int i = 1; i <= T; i++) {
      string N;
      cin >> N;
      solve(N);
      output(i, N);
   }
   return 0;
}

void output(int x, string y) {
   cout << "Case #" << x << ": " << y << endl;
}

void solve(string& N) {
   int length = N.size();
   
   for (int i = length-1; i > -1; i--) {
      if (i == 0) {
         if (N[i] == '0') {
            N = N.substr(1);
         }
      } else {
         check(N, length, i-1, i);
      }
   }    
}

void check(string& N, int length, int l, int r) {
   if (N[l] == N[r]) {
      return;
   }
   if (N[l] > N[r]) {
      N[l] = N[l] - 1;
      nine(N, length, r);
   }
}

void nine(string& N, int length, int r) {
   for (int i = r; i < length; i++) {
      N[i] = '9';
   }
}

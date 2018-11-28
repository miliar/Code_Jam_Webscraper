#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int floor(int n, int d) {
  return n/d;
}
int ceil(int n, int d) {
  return (n+d-1)/d;
}

int diff(int a, int b) {
  if (a > b) return a-b;
  else return b-a;
}

int solve_for_2(int n, vector<int>&v) {
  int n_0=0, n_1=0;
  for (auto x : v) {
    if (x%2==1) n_1++;
    else n_0++;
  }
  return n_0 + ceil(n_1,2);
}

int solve_for_3(int n, vector<int>&v) {
  int n0=0, n1=0, n2=0;
  for (auto x : v) {
    if (x%3==0) n0++;
    else if(x%3 == 1) n1++;
    else n2++;
  }
  return n0 + min(n1,n2) + ceil(diff(n1,n2), 3);
  
}

int solve_for_4(int n, vector<int>&v) {
  int n0=0, n1=0, n2=0, n3=0;
  for (auto x : v) {
    if (x%4==0) n0++;
    else if(x%4 == 1) n1++;
    else if(x%4 == 2) n2++;
    else n3++;
  }
  int m = min(n1, n3);
  int rem = n2%2;
  int d = diff(n1, n3);
  int sum = 0;
  sum += n0;
  sum += m;
  sum += floor(n2, 2);
  if (rem == 0) {
    sum += ceil(d, 4);
  } else {
    if (d >= 2) {
      sum += 1;
      sum += ceil(d-2, 4);      
    } else {
      sum += 1;
    }
  }
  return sum;
}


int main(){
  ios_base::sync_with_stdio(false);
  int T;
  int n, p;
  cin >> T;
  for(int ind=0; ind<T; ind++){
    cin >> n >> p;
    vector<int>v(n, 0);
    for(int i=0; i<n; i++) {
      cin >> v[i];
    }
    int answer = -1;
    if (p==2) answer = solve_for_2(n, v);
    else if (p == 3) answer = solve_for_3(n, v);
    else if (p == 4) answer = solve_for_4(n, v);
    
    cout << "Case #" << (ind+1) << ": " << answer << endl; 
  }
  return 0;
}
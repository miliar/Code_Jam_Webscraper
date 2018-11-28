#include <iomanip>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <limits>
#include <cmath>

using namespace std;

struct Pancake {
  int radius;
  int height;
  
  long double exposed() {
    return cyl() + base();
  }
  
  long double cyl() {
    return ((2.0 * (long double)M_PI) * radius) * height;
  }
  
  long double base() {
    return ((radius * (long double)M_PI) * radius);
  }
  
};

struct MyPancakeSorter {
  bool operator() (const Pancake& a, const Pancake& b) { 
    return (a.radius < b.radius);
  }
};


const int MAX_PANCAKES = 1000;

int pancakes, requested;
Pancake pk[MAX_PANCAKES];

void read_input() {
  cin >> pancakes >> requested;
  for (int i = 0; i < pancakes; i++) {
    cin >> pk[i].radius >> pk[i].height;
  }
  
  sort(pk, pk + pancakes, MyPancakeSorter());
  
}

long double memory[MAX_PANCAKES+1][MAX_PANCAKES+1];

long double solve(int i, int k) {
//  cout << "solve(" << i << ", " << k << "): " << memory[i][k] << "\n";
  if (memory[i][k] > 0) return memory[i][k];
  long double best = 0;
  long double current = 0;
  
  if (k == 1) {
    while (i < pancakes) {
      current = pk[i].exposed();
      if (current > best) {
        best = current;
      }
      i++;
    }
  } else {
    while (pancakes-i >= k) {
//      cout << "checking: " << i << endl;
      current = pk[i].cyl() + solve(i+1, k-1);
      
      if (current > best) {
        best = current;
      }
      i++;
    }
     
  }
  
  return memory[i][k] = best;
}

long double solution;

void solve() {
  memset(memory, 0, sizeof(memory));
  /*
  for (int i = 0; i < pancakes; i++) {
    cout << pk[i].radius << " " << pk[i].height << endl;;
    
  }
  cout << endl << endl;
  */
  solution = solve(0, requested);
  
}

void write_output(int tc) {
  cout << "Case #" << tc << ": ";
  cout << setprecision(14) << solution;
  cout << endl;
  
}

int main() {
  int test_cases;
  cin >> test_cases;
  
  for (int tc = 1; tc <= test_cases; tc++) {
    
    read_input();
    
    solve();
    
    write_output(tc);
    
  }
  
  return 0;
}

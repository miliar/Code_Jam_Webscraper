#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cmath>
#include <climits>

using namespace std;

const int MAX_CITIES = 100;
long long int horseCapacity[MAX_CITIES];
long long int hourseSpeed[MAX_CITIES];
long long int adj[MAX_CITIES][MAX_CITIES];
int cities;

void preCompute() {
  long long int d;
  for (int k = 0; k < cities; k++) {
    for (int i = 0; i < cities; i++) {
      for (int j = 0; j < cities; j++) {
        if (adj[i][k] == -1 || adj[k][j] == -1) continue;
        d = adj[i][k] + adj[k][j];
        if (adj[i][j] == -1 || adj[i][j] > d) {
          adj[i][j] = d;
        }
      }
    }
  }
}

int horseCutter[MAX_CITIES];

inline bool canHorseMakeTravel(int h, int from, int to) {
  return adj[from][to] != -1 
            && horseCutter[to] == 0
            && horseCapacity[h] >= adj[from][to];
}

inline long double computeTimeOfTravel(int h, int from, int to) {
  return ((long double)adj[from][to]) / hourseSpeed[h];
}

long double solve(int from, int to) {
  if (from == to) return 0;
  
  horseCutter[from] = 1; // You are using h_from
  long double minTimeOfTravel = numeric_limits<long double>::infinity();
  for (int k = 0; k < cities; k++) {
    if (canHorseMakeTravel(from, from, k)) {
      minTimeOfTravel = min(minTimeOfTravel, 
        computeTimeOfTravel(from, from, k) + solve(k, to));
    }
  }
  horseCutter[from] = 0;
  return minTimeOfTravel;
}

int main() {
  int tcases, queries;
  cin >> tcases;
  
  for (int c = 1; c <= tcases; c++) {
    cin >> cities >> queries;
    
    for (int h = 0; h < cities; h++) {
      cin >> horseCapacity[h] >> hourseSpeed[h];
    }
    for (int i = 0; i < cities; i++) {
      for (int j = 0; j < cities; j++) {
        cin >> adj[i][j];
        if (i == j) adj[i][j] = 0;
      }
    }
    
    preCompute();
    
    /*
    for (int i = 0; i < cities; i++) {
      for (int j = 0; j < cities; j++) {
        cout << adj[i][j] << " ";
      }
      cout << endl;
    }
    */
    
    int from, to;
    cout << "Case #" << c << ":";
    for (int q = 0; q < queries; q++) {
      cin >> from >> to;
      
      cout << " " << setprecision(8) << solve(from-1, to-1);
    }
    cout << endl;
  }
  return 0;
}

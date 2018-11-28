#include <iostream>
#include <sstream>
#include <climits>
#include <stdio.h>
#include <iomanip>
#include <list>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <cmath>
#include <string>
#include <gmpxx.h>

using namespace std;

int T;
int N;
int K;
double U;
double p[100];

double bin_search(double min, double max) {
  double mean = (max + min)/2;
  if(min == max || max - min < 0.000000001 || (max - min)/mean < 0.000000001) {
    return mean;
  }
  double need = 0.0;
  for(int i=0; i<K; i++) {
    if(p[i] < mean) {
      need += mean - p[i];
    }
  }
  if(need > U) {
    return bin_search(min, mean);
  } else {
    return bin_search(mean, max);
  }
}



void solve(int t) {
  cerr << "test " << t << endl;
  cin >> N >> K;
  cin >> U;
  double probs1[101];
  double probs2[101];
  double *point;
  double *point_other;
  for(int i=0; i<101; i++) {
    p[i] = 0.0;
  }
  for(int i=0; i<N; i++) {
    cin >> p[i];
  }
  sort(begin(p), end(p), greater<double>());
  double boost = bin_search(0.0, 1.0);
  cerr << "boost to: " << boost << endl;
  for(int i=0; i<101; i++) {
    probs1[i] = 0.0;
    probs2[i] = 0.0;
  }
  probs1[0] = 1.0;
  point = probs1;
  point_other = probs2;
  for(int i=0; i<N; i++) {
    for(int j=0; j<N; j++) {
      point_other[j] = 0.0;
    }
    double prob { p[i] };
    if(i < K) {
      prob = max(prob, boost);
    }
    for(int j=0; j<N; j++) {
      point_other[j] += point[j] * (1.0-prob);
      point_other[j+1] += point[j] * prob;
    }
    for(int j=0; j<N; j++) {
      //cerr << point[j] << " ";
    }
    //cerr << endl;
    double *point_swap = point;
    point = point_other;
    point_other = point_swap;
  }
  cout << setprecision(9);
  double sum = 0.0;
  for(int i=K; i<=N; i++) {
    sum += point[i];
  }
  cout << "Case #" << t << ": " << sum << endl;
}

int main() {
  cin >> T;
  for(int t=0; t<T; t++) {
    solve(t+1);
  }
}

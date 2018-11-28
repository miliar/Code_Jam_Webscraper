////////////////////////////////////////////////////////////////////////////////
/**
 * @file p3.cpp
 * @date 2017-04-08
 * @author Tiago Lobato Gimenes    (tlgimenes@gmail.com)
 *
 * @copyright Tiago Lobato Gimenes 2016. All rights reserved.
 *
 * @brief
 *
 * This file contains implementation of the correspoding header file, i.e. .hpp,
 * .hh or .h
 */
////////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <cstdlib>
#include <string>
#include <queue>
#include <cmath>

////////////////////////////////////////////////////////////////////////////////

void up_last(std::vector<int>& q) {
  int it = q.size()-1, last = q[it];

  while(it > 0 && q[it-1] <= q[it]) {
    q[it] = q[it-1];
    it--;
  }
  q[it] = last;
}


////////////////////////////////////////////////////////////////////////////////

void solve(int nn, int k) {
  std::vector<int> q, v;
  int front=0;
  int size, y, z;

  q.push_back(nn);
  for(int i=0; i < k; i++) {
    size = q[front]; front++;

    y = (size  )/2;
    z = (size-1)/2;

    v.push_back(size);

    int s2 = (size-1)/2;
    int s1 = size - 1 - s2;

    if(s1 > 0) {q.push_back(s1); up_last(q);};
    if(s2 > 0) {q.push_back(s2); up_last(q);};
  }

  for(int i=1; i < v.size(); i++) {
    if(v[i-1] < v[i])
      std::cout << "Error: " << v[i-1] << " " << v[i] << std::endl;
  }

  std::cout << y << " " << z << std::endl;
}

////////////////////////////////////////////////////////////////////////////////

int main() {
  int cases, n, k;

  std::cin >> cases;
  for(int i=0; i < cases; i++) {
    std::cin >> n >> k;

    std::cout << "Case #" << i+1 << ": ";
    solve(n,k);
  }
    
  return 0;
}

////////////////////////////////////////////////////////////////////////////////

#include <stdio.h>
#include <iostream>
#include <map>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;


void print_vector(vector<string> v) {
  for (int i=0; i < v.size(); i++) {
    cout << v[i] << ' ';
  } cout << endl;
}

bool is_sorted(int n) {
  int last_digit = n%10;
  n /= 10;
  while (n && last_digit >= n%10) {
    last_digit = n%10;
    n /= 10;
  }
  return n == 0;
}

vector<long long> numbers;

void generate() {
  queue<long long> q;
  q.push(0);

  while(q.size()) {
    long long u = q.front();
    numbers.push_back(u);
    q.pop();
    for (int i=1; i <= 9; i++) {
      if (i >= u%10 && (u * 10 + i) <= 1e18) {
        q.push(u * 10 + i);
      }
    }
  }

  numbers.pop_back();
}

int main(){
#ifndef ONLINE_JUDGE
	freopen("B-large.in","r", stdin);
	freopen("code.out","w", stdout);
#endif
  generate();
  int t; cin >> t;
  for (int i=1; i <= t; i++) {
    long long n; scanf("%lld", &n);
    printf("Case #%d: ", i);
    if (is_sorted(n)) {
      printf("%lld\n", n);
    } else {
      vector<long long>::iterator pos;
      pos = upper_bound(numbers.begin(), numbers.end(), n);
      printf("%lld\n", numbers[((pos - numbers.begin()) - 1)]);
    }
  }
	return 0;
}

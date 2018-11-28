
#include <cstdio>
#include <iostream>
#include <string>
#define toDigit(c) (c-'0')
using namespace std;
typedef long long ll;
int main() {
  int t; scanf("%d", &t);
  for (int tc = 1; tc <= t; tc++) {
    string str; cin >> str;
	int id; 
	id = atoi(str.c_str());
	ll n = ll(id);
	int flag = 1;
	while(flag == 1 && str.length() != 1 ) {
		for(int i = 1; i < str.length(); i++) {
		  if(toDigit(str[i]) < toDigit(str[i - 1])) {
			  n = n - 1;
			  str = to_string(n);
			  flag = 1;
			  break;
			}else flag = 0; 
		}
	}
    printf("Case #%d: %lld\n", tc, n);
  }
  return 0;
}
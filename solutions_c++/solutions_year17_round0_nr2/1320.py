#include <cstdio>
#include <climits>

using namespace std;
typedef unsigned long long int ll;

int n;
ll in;

int main()
{
  scanf("%d", &n);
  for(int i = 0; i < n; ++i) {
    scanf("%lld", &in);
    for(ll j = 1; in/j and j < LONG_MAX/5;j*=10) {
      if((in%(j*10))/j < (in%(j*100))/(j*10)) in -= (in%(j*10))+1;
    }
    printf("Case #%d: %lld\n", i+1, in);
  }
  return 0;
}

#include <iostream>
#include <string.h>
#include<algorithm>
#include<stdio.h>
#include<math.h>
using namespace std;
double pai = acos(-1);
double s[1011];
double e[1011];
int main() {
  int t,n,k;
  freopen("a.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  cin >> t;
  for (int ii = 1; ii <= t; ++ii) {

    cin >> n>>k;
    for(int i=0;i<n+k;i++)
    {
        scanf("%lf%lf",&s[i],&e[i]);
    }

    int ans = 0;
    if(n == 2 || k==2)
    {
        if(s[1] < s[0])
        {
            swap(s[0],s[1]);
            swap(e[0],e[1]);
        }
        if(e[1]-s[0]<=720 || s[1]+720 >= e[0] +1440)
            ans =2;
        else ans =4;
    }
    else
        ans =2;
    printf("Case #%d: %d\n",ii,ans);
  }
}

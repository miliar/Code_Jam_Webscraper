#include<iostream>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int t = 1;t <= T;t ++)
  {
    long long n;
    cin >> n;

    int num[100];

    int len = 0;
    while(n)
    {
      num[len ++] = n % 10;
      n /= 10;
    }
    reverse(num , num + len);

    long long ans = 0;
    long long prev = 0;

    for(int i = 0;i < len;i ++)
    {
      if(prev % 10 <= num[i] - 1)
      {
        long long t = prev * 10 + (num[i] - 1);
        for(int j = 0;j < len - i - 1;j ++)
          t = t * 10 + 9;
        ans = max(ans , t);
      }
      if(prev % 10 > num[i])
        break;
      prev = prev * 10 + num[i];
    }
    ans = max(ans , prev);
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}

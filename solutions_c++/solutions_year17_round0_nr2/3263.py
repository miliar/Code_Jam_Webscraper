#include <iostream>

using namespace std;

typedef long long ll;

int digit(ll n)
{
  int ans = 0;
  while(n > 0)
  {
	n /= 10;
	ans++;
  }
  return ans;
}

ll pow10(int d)
{
  ll ans = 1;
  for(int i = 0; i < d; i++)
  {
	ans *= 10;
  }
  return ans;
}

int get(ll n, int d)
{
  return (n / pow10(d)) % 10;
}

void set(ll &n, int d, int v)
{
  ll pos = pow10(d);
  n -= get(n, d) * pos;
  n += v * pos;
}

int main()
{
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++)
  {
	ll n;
	cin >> n;

	for(int i = 0; i < digit(n) - 1; i++)
	{
	  if(get(n, i) < get(n, i + 1))
	  {
	  	n -= pow10(i + 1);
	  	for(int j = 0; j <= i; j++)
	  	{
	  	  set(n, j, 9);
	  	}
	  }
	}
	cout << "Case #" << t << ": " << n << endl;
  }  
}

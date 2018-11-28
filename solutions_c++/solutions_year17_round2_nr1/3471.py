#include <iostream>
#include <iomanip>

using namespace std;


double solve()
{
  long double d, n, k, s, slower;
  cin >> d >> n;
  slower = -1.00;


  for(long double i = 0; i < n; i++){
    cin >> k >> s;

    //cout << "caballo " << k << " speed " << s << endl;
    long double dist = d - k;
    long double time = dist / s;
    //cout << "Dist " << dist << " time " << time << endl;
    slower = max(slower, time);
    //cout << "slower " << slower << endl;
  }

  return d/slower;
}

int main()
{
  int T;
  scanf("%d",&T);
  std::cout << std::setprecision(10) << std::fixed;
//  std::setprecision(10)
  for(int test = 1; test <= T; test++){
    cout << "Case #"<< test << ": " << solve() << endl;
  }
  return 0;
}
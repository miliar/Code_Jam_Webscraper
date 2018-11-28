#include <iostream>
using namespace std;

void tick()
{
  long length, nHorse;
  cin >> length >> nHorse;

  double lastTime = 0;

  for (int i=0; i < nHorse; i++)
  {
    long start, speed;
    cin >> start >> speed;
    double g = float(length - start) / speed;
    if (g > lastTime)  {lastTime = g;}
  }

  cout.precision(17);
  cout << length / lastTime << endl;
}

int main()
{
  int bigT;
  cin >> bigT;
  for (int i=0; i < bigT; i++)
  {
    cout << "Case #" << i + 1 << ": ";
    tick();
  }
}

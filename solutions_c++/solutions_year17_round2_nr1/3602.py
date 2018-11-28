#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using namespace std;

bool compFunc(pair<long, int> i, pair<long, int> j)
{
  return i.first < j.first;
}

double calcSpeed(vector< pair<long, int> > *horses, long dest)
{
  bool first = true;
  double speed;
  for(vector<pair<long, int> >::iterator itr = horses->begin();
      itr != horses->end(); ++itr)
    {
      double arrItr = (dest - itr->first)/(double)(itr->second);
      if(first)
	{
	  speed = dest/arrItr;
	  first = false;
	}
      else
	{
	  double curArr = dest/speed;
	  if(curArr < arrItr)
	    {
	      speed = dest/arrItr;
	    }
	}
    }
  return speed;
}


int main() {

  int t;
  cin >> t;  
  for (int i = 1; i <= t; i++) {
    long d;
    int h;
    cin >> d >> h;
    vector< pair<long, int> > horses;
    for(int j = 1; j <= h; j++) {
      long di;
      int si;
      cin >> di >> si;
      horses.push_back(pair<long, int>(di,si));
    }
    sort(horses.begin(), horses.end(), compFunc);
    cout << "Case #" << i << ": " << fixed << setprecision(6) << calcSpeed(&horses, d) << endl;
  }

  return 0;
}

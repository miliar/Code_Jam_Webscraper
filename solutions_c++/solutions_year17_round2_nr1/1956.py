#include<iostream>

using namespace std;

const int MAX_N = 1000;

int starts[MAX_N];
int speeds[MAX_N];
int dists[MAX_N];
double times[MAX_N];

int main(){

  cout.precision(17);
  
  int c;
  cin >> c;
  for(int cur = 1; cur <= c; cur++){
    cin.ignore();
    int D, N;
    cin >> D >> N;

    double max_time = -1;
    
    for(int i = 0; i < N; i++){
      cin.ignore();
      cin >> starts[i] >> speeds[i];
      dists[i] = D - starts[i];
      times[i] = ((double)dists[i])/((double)speeds[i]);
      if(times[i] > max_time)
	max_time = times[i];
    }

    cout << "Case #" << cur << ": " << (((double)D)/max_time) << endl;
  
  }

}

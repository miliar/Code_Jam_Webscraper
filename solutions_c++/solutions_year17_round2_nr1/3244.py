#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <math.h>
#include <iomanip>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, D, n;
  cin >> t;  
  for (int i = 1; i <= t; ++i) {
    cin >> D >> n; 
    int *dis = new int[n];
    int *spd = new int[n];
    int swapped = 1;
    int dis_temp;
    for(int j = 0;j < n;j++) {
        cin >> dis_temp >> spd[j];
        dis[j] = D-dis_temp;
    }    
    /*for(int j=0;j<n && swapped != 0;j++) {
        swapped = 0;
        for(int k=n-1;k>j;k--) {
            if(dis[k] > dis[k-1]) {
                int temp;
                temp = dis[k];
                dis[k] = dis[k-1];
                dis[k-1] = temp;
                temp = spd[k];
                spd[k] = spd[k-1];
                spd[k-1] = temp;
                swapped = 1;
            }
        }
    }*/
    int min_spd = n-1;
    for(int j = n-2;j >=0;j--) {
        if((float)dis[j]/(float)spd[j] > (float)dis[min_spd]/(float)spd[min_spd]) {
            min_spd = j;
        }
    }
    float time_taken = (float)dis[min_spd]/(float)spd[min_spd];
    cout << "Case #" << i << ": "<<fixed<<(float)D/time_taken<< endl;
    delete [] dis;
    dis = NULL;
    delete [] spd;
    spd = NULL;
  }
  return 0;
}
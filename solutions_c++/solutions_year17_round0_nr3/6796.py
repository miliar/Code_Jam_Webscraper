#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
  uint64_t t, n,m;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;
    cin >> m;
    bool stall[n+1];
    fill_n(stall, n+1, 0);
    uint64_t take_stall = 0;
    uint64_t min[n+1];
    uint64_t max[n+1];
    for (uint64_t j=0; j<m; j++) {
      //cout << "Enter person = " << j << endl;
      uint64_t ls[n+1];
      uint64_t rs[n+1];
      fill_n(ls, n+1, 0);
      fill_n(rs, n+1, 0);
      fill_n(min, n+1, 0);
      fill_n(max, n+1, 0);
      take_stall = 1;
      for (uint64_t k=1; k<n+1 ; k++) {
        //cout << "Checking stall = " << k << endl;
        //cout << "ls value = " << ls[k] << endl;
        if (stall[k] == 1) {
	  continue;
	}
	for (uint64_t l=k-1; l>0; l--) {
	  if (stall[l] == 1) {
	    break;
	  }
	  ls[k]++;
        }
        //cout << "ls value = " << ls[k] << endl;
	for (uint64_t l=k+1; l<n+1; l++) {
	  if (stall[l] == 1) {
	    break;
	  }
	  rs[k]++;
        }
        //cout << "rs value = " << rs[k] << endl;
      }
      for (uint64_t k=1; k<n+1 ; k++) {
	if (stall[k] == 1) {
	  continue;
	}
	min[k] = (ls[k] < rs[k]) ? ls[k] : rs[k]; 
	max[k] = (ls[k] > rs[k]) ? ls[k] : rs[k];
	//cout << "Min for stall " << k << " = " << min[k] << endl; 
	//cout << "Max for stall " << k << " = " << max[k] << endl; 
      }
      //cout << "stall taken = " << take_stall << endl;
      for (uint64_t k=2; k<n+1 ; k++) {
        //cout << "Checking stall = " << k << endl;
	if (stall[k] == 1) {
	  continue;
	}
 	if (min[k] > min[take_stall]) take_stall = k;
        //cout << "stall taken = " << take_stall << endl;
 	if ((min[k] == min[take_stall]) && (max[k] > max[take_stall] )) {
           //cout << "min[k] = " << min[k] << " max[k] = " << max[k] <<  endl;
           //cout << "min[k-1] = " << min[k-1] << " max[k-1] = " << max[k-1] <<  endl;
	   take_stall = k;
        }
       // cout << "stall taken = " << take_stall << endl;
      }
      stall[take_stall] = 1;
      //cout << "stall taken = " << take_stall << endl;
    }
    cout << "Case #" << i << ": " << max[take_stall] << " " << min[take_stall] <<  endl;
  }
  return 0;
}

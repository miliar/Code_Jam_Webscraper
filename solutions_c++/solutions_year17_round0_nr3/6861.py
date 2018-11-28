#include <iostream>
#include <string>

using namespace std;

int main() {
  int numTrials;
  cin >> numTrials;
  for (int i=0; i < numTrials; i++) {
    int N;
    cin >> N;
    bool stalls[N+2];
    stalls[0] = true;
    stalls[N+1] = true;
    for (int j=0; j < N; j++) {
      stalls[j+1] = false;
    }
    int stallmax[N+2];
    for (int j=0; j < N+2; j++) {
      stallmax[j] = 0;
    }
    int stallmin[N+2];
    for (int j=0; j < N+2; j++) {
      stallmin[j] = 0;
    }
    int max, min;
    int K;
    cin >> K;
    for (int k=0; k < K; k++) {
      for (int j=0; j < N+2; j++) {
	if (stalls[j] == true) {
	  stallmax[j] = -1;
	  stallmin[j] = -1;
	  continue;
	}
	int left = 0;
	int right = 0;
	while (stalls[j-left-1] == false) {
	  left++;
	}
	while (stalls[j+right+1] == false) {
	  right++;
	}
	if (left>right){
	  stallmin[j] = right;
	  stallmax[j] = left;
	}
	else {
	  stallmin[j] = left;
	  stallmax[j] = right;
	}
      }
    
      int location = 0;
      int cMax = -1;
      int cMin = -1;
      for (int z=N; z > 0; z--) {
	if (stallmin[z] > cMin) {
	  cMin = stallmin[z];
	  cMax = stallmax[z];
	  location = z;
	}
	if (stallmin[z] >= cMin && stallmax[z] >= cMax) {
	  cMin = stallmin[z];
	  cMax = stallmax[z];
	  location = z;
	}
      }
      max = stallmax[location];
      min = stallmin[location];
      stalls[location] = true;
    }
    cout << "Case #" << i+1 << ": " << max << " " << min << endl;
  }
  return 0;
}

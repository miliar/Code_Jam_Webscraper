#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;



double each[100];
double packets[100][100];
int lowest[100];

double eps=0.0000000000001;

int main() {
  int T,N,P;
  cin >> T;
  for(int t=1; t<=T; t++) {
    cin >> N >> P;

    for(int i=0; i<N; i++) {
      cin >> each[i];
    }

    for(int i=0; i<N; i++) {
      for(int j=0; j<P; j++) {
	cin >> packets[i][j];
      }
      lowest[i]=0;
      sort(packets[i],packets[i]+P);
    }
    int best=0;
    bool finished=false;
    bool changed=true;
    while (!finished) {
      int high=0;
      changed=false;
      high=0;
      for(int i=0; i<N; i++) {
	int c=ceil(packets[i][lowest[i]]/each[i]/1.1-eps);
	high=max(high,c);
      }
      //cout << high << " " << best << endl;
      for(int i=0; i<N; i++) {
	while (packets[i][lowest[i]]/each[i]/.9< high-eps) {
	  changed=true;
	  lowest[i]++;
	  if (lowest[i]==P) {
	    finished=true;
	    i==N;
	    break;
	  }
	} 
      }
    
      if (!changed) {
	best++;
	int top=0;
	for(int i=0; i<N; i++) {
	  lowest[i]++;
	  if (lowest[i]==P) {
	    finished=true;
	    i==N;
	    break;
	  }
	}
      }
    }
    cout << "Case #" << t << ": " << best << endl;
  }
  return 0;
}

    
  

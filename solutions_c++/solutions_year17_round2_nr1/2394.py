#include<iostream>
#include<fstream>
#include <iomanip>
using namespace std;

int main() {
  ifstream myInput;
  ofstream myOutput;
  myInput.open("A-large.in");
  myOutput.open("outputa.txt");
  int T;
  myInput >> T;
  for(int testCase=1; testCase<T+1; testCase++) {
    int N;
    double D;
    myInput>>D>>N;
    double maxTime = 0;
    for(int i=0; i<N;i++) {
      double pos, speed;
      myInput>>pos>>speed;
      double temp = (D-pos)/speed;
      if(temp > maxTime) maxTime = temp;
    }
    double ans = D/maxTime;
    myOutput<<"Case #"<<testCase<<": ";
    myOutput << fixed;
    myOutput << setprecision(6) <<ans<<endl;
  }
}

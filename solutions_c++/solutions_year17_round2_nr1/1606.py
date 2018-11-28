#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iomanip>
using namespace std;

vector <int> v;

int main () {
  ofstream myfile;
  ifstream input;
  input.open("input.txt");
  myfile.open ("output.txt");
  int t;
  input>>t;
  for(int i=1; i<=t; i++){
    int d, n;
		input>>d>>n;
    int ki, si;
    double timeToFinish;
    double longestTime = -1.0;
    for (int j=0; j<n; j++){
      input>>ki>>si;
      timeToFinish = (double)(d-ki)/si;
      longestTime = max(longestTime, timeToFinish);
    }
    myfile<< fixed;
    myfile<<"Case #"<<i<<": "<<setprecision(6)<<(double)d/longestTime<<endl;
  }
  myfile.close();
  input.close();
  return 0;
}

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

int main(){

  int num_cases;
  double desti;
  double numh;
  double maxtime;
  double timet;
  double hspeed;
  double hposition;

  ifstream infile("A-large.in", ifstream::binary);
  ofstream outfile ("A-large.out.txt",ofstream::binary);
  infile>>num_cases;


  for(int i=0;i<num_cases;i++){
    infile>>desti;
    infile>>numh;
    maxtime = 0;
    for(int j=0;j<numh;j++){
      infile>>hposition;
      infile>>hspeed;
      timet = (desti-hposition)/hspeed;
      maxtime = timet > maxtime ? timet : maxtime;
    }
    outfile<<"Case #"<<i+1<<": "<<fixed<<setprecision(6)<<desti/maxtime<<endl;
  }

  infile.close();
  outfile.close();
  return 0;
}

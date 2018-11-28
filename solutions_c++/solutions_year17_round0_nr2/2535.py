#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <time.h>       /* time */
#include <algorithm>
#include <list>
#include <utility>
#include <stack>
#include <math.h>
#include <iomanip>

using namespace std;



int main()
{
  ofstream outfile;
  outfile.open ("solution.out");
  std::ifstream infile;
  infile.open ("data.in", std::ifstream::in);
  std::string   line;
  getline(infile, line);
  std::stringstream  lineStream(line);
  int T;
  lineStream>>T;
  for(int caseNr=0;caseNr<T;caseNr++){
	long long int N;
	getline(infile, line);
	std::stringstream  Stream1(line);
	Stream1>>N;
	vector<long long int> dec;
      while(N>0){
          dec.push_back(N%10);
          N/=10;
      }
      bool finished=false;
      while(finished==false) {
          int i=dec.size()-1;
          while (i > 0 && dec[i] <= dec[i - 1])
              i--;
          if (i > 0) dec[i]--;
          else finished = true;
          while (i > 0) {
              dec[i - 1] = 9;
              i--;
          }
      }
      long long int res=0;
      for(int i=dec.size()-1;i>=0;i--){
          res*=10;
          res+=dec[i];
      }

		outfile<<"Case #"<<caseNr+1<<": "<<res<<endl;
  }

  infile.close();
  outfile.close();
  return 0;
}



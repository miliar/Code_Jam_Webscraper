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
	int K;
	string s;
	getline(infile, line);
	std::stringstream  Stream1(line);
	Stream1>>s>>K;
      vector<int> v;
      for(int i=0;i<s.size();i++){
            if(s[i]=='+'){
                v.push_back(1);
            } else
                v.push_back(-1);
      }
      int counter=0;
	for(int i=0;i<v.size()-K+1;i++){
	    if(v[i]<0){
            counter++;
            for(int j=0;j<K;j++){
                v[i+j]*=-1;
            }
        }
	}
      bool hom=true;
      for(int i=0;i<v.size();i++){
          if(v[i]<0) hom=false;
      }
      if(hom==false)	outfile<<"Case #"<<caseNr+1<<": IMPOSSIBLE"<<endl;
      else outfile<<"Case #"<<caseNr+1<<": "<<counter<<endl;
  }

  infile.close();
  outfile.close();
  return 0;
}



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
      cout<<"Solving case number "<<caseNr+1<<endl;
	long long int N, K;
	getline(infile, line);
	std::stringstream  Stream1(line);
	Stream1>>N>>K;
      cout<<N<<" "<<K<<endl;
      vector<pair<long long int, long long int> > stalls;
      stalls.push_back(make_pair(N,1));
      long long int moves=0;
      long long int left, right, occ_number;
    while(moves<K) {
       /* for(int i=0;i<stalls.size();i++){
            cout<<"Printing states "<<endl;
            cout<<stalls[i].first<<"\t"<<stalls[i].second<<endl;
        }*/
        occ_number = stalls[0].second;
        moves += occ_number;
        left = (stalls[0].first-1) / 2;
        right = stalls[0].first -1 - left;
        if (stalls.back().first == right) {
            stalls.back().second += occ_number;
        } else {
            stalls.push_back(make_pair(right, occ_number));
        }
        if (stalls.back().first == left) {
            stalls.back().second += occ_number;
        } else {
            stalls.push_back(make_pair(left, occ_number));
        }
        stalls.erase(stalls.begin(),stalls.begin()+1);
    }
      outfile<<"Case #"<<caseNr+1<<": "<<right<<" "<<left<<endl;
  }

  infile.close();
  outfile.close();
  return 0;
}



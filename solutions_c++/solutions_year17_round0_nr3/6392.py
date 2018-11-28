#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <math.h>       /* ceil */
using namespace std;  // since cin and cout are both in namespace std, this saves some text

std::ifstream infile("C-small-2-attempt0.in");
std::ofstream outfile("C-small-2-attempt0.out");

//std::ifstream infile("input.txt");
//std::ofstream outfile("output.txt");

int main() {
  int t;
  long long N, k, p, p2, temp, res1, res2, n, v;

  infile>>t;// read t. cin knows that t is an int, so it reads it as such.
  //std::getline (infile, line);

  for (int i = 1; i <= t; ++i) {

  	infile>>N; infile>>k;
  	p = floor(log2(k));
    p2 = p + 1;
  	temp = pow(2,p2);
  	n = floor((N+1)/(double)temp);
    v = (N+1)%temp;
    
    if((k-temp/2)<v)
      res2 = n;
    else
      res2 = n-1;

    if(k<v)
      res1 = n;
    else
      res1 = n-1;

  	outfile<<"Case #" << i << ": " << res2 << " " << res1 << endl;
  	//cout<<"Case #" << i << ": " << res2 << " " << res1 << endl;
  	
  }

  return 0;
}
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <map>
using namespace std;

ofstream out;
ifstream in;

int casei=1;
#define OUTPUT(type)\
void output(type i) { out << "Case #" << casei << ": " << i << endl; casei++; }

OUTPUT(int);
OUTPUT(long long);
OUTPUT(unsigned long long);
OUTPUT(const char*);
OUTPUT(string);

void worker();
int main()
{
  in.open("input");
  out.open("output");
  int cnt;
  in >> cnt;
  for (int i=0; i<cnt; i++) {
    worker();
  }
  in.close();
  out.close();
  return 0;
}







long long n,k;
map<unsigned long long, unsigned long long> b; // blank, count

void worker()
{
  b.clear();
  in >> n >> k;;

  // kind of optimization
  /*
  if (n == k) {
    output("0 0");
    return;
  }*/

  b[n] = 1;
  unsigned long long bmax;
  unsigned long long left, right;
  while (k > 0) {
    // find max block & count
    auto p = b.rbegin();
    unsigned long long c = p->second; // block count duplicated
    bmax = p->first;
    k -= c;
    b.erase(bmax);

    // divide max place into 2 and append
    left = (bmax) / 2;
    right = (bmax-1)/2;
    if (left) b[left] += c;
    if (right) b[right] += c;
    // kind of optimization
    //if (left == 1 && right == 0) break;
  }



  stringstream ss;
  ss << left << " " << right;
  output(ss.str());
}

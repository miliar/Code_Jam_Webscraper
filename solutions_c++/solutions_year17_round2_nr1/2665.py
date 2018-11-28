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
void output(double d) {
  out.precision(6);
  out << "Case #" << casei << ": " << fixed << d << endl; casei++;
}

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






//int k[10000], s[10000];

void worker()
{
  long long d,n;
  in >> d >> n;
  double rs = -1;
  double curs = 0;
  long long k,s;
  for (int i=0; i<n; i++) {
    in >> k >> s;
    double hrs = (d-k)/(double)s;
    curs = d / hrs;
    if (rs < 0) rs = curs;
    else rs = min(rs,curs);
  }
  output(rs);
}

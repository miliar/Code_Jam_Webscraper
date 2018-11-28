#include <iostream>
#include <fstream>
#include <string>
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







unsigned long long n;

void worker()
{
  unsigned long long k=10, r=0;
  in >> n;
  r=n;
  while (k <= r) {
    if (r/k%10 > r/(k/10)%10) {
      r -= r%k + 1;
    }
    k *= 10;
  }
  cout << r << endl;
  output(r);
}

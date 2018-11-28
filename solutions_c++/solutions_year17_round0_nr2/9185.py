//tidy number

#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

bool tidy (string& n)
{
  int i;
  bool changed = false;
  for (i = 0; i<n.length()-1; i++) {
    if (n[i]>n[i+1]) {
      changed = true;
      n[i]--;
      for (int j = i+1; j<n.length(); j++)
        n[j] = '9';
    }
  }

  if (changed == true)
    tidy (n);
}

void clear (string &s)
{
  if (s[0] == '0') {
    s.erase (s.begin());
    clear (s);
  }
}

int main ()
{

  ifstream in ("input.txt");
  ofstream out ("output.txt");
  int test;
  in>> test;
  for (int i = 0; i< test; i++) {
    string numero;
    in>>numero;

    tidy(numero);

    clear (numero);

    out << "Case #" << i+1 << ": " << numero << endl;
  }

  return 0;
}

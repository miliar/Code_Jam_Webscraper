/*
  Task: tidy numbers
  Category: 
  Sources:
file:///Volumes/ELIAS/SOI/Aufgaben_Sammlung/Tasks/template_de.pdf
file:///Volumes/ELIAS/SOI/Aufgaben_Sammlung/Tasks/template_en.pdf
file:///Volumes/ELIAS/SOI/Aufgaben_Sammlung/Tasks_Samples/template_samples.zip
*/

#include <iostream>

#ifdef DEBUG
#  define DEB(x) cerr << "DEB: " << x << '\n'
#else
#  define DEB(x)
#endif

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);

  long long T;

  cin >> T;

  for (long long t = 0; t < T; ++t) {
    string N;

    cin >> N;

    bool op = false;
    long long b = -1;
    
    for (long long i = 0; i < N.length(); ++i) {
      if (op) {
	N.at(i) = '9';
      } else if (i != N.length()-1) {
	if (N.at(i) > N.at(i+1)) {
	  op = true;
	  N.at(i) = N.at(i)!='0'?N.at(i)-1:'9';
	  if (i != 0 && N.at(i) < N.at(i-1)) {
	    b = i;
	  }
	}
      }
    }

    for (; b > 0; --b) {
      if (N.at(b) < N.at(b-1)) {
	N.at(b) = '9';
	N.at(b-1) = N.at(b-1)!='0'?N.at(b-1)-1:'9';
      } else {
	break;
      }
    }

    cout << "Case #" << t + 1 << ": " << stoll(N) << "\n";
  }
  
  return 0;
}

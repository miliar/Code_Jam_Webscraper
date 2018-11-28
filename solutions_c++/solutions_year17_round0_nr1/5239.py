#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream infile;
	ofstream outfile;
	infile.open("input.txt");
	outfile.open("output.txt");
	int T, S, K, Scomplete, Slength, possible;
  char c;
	infile >> T;
	for (int j = 0; j<T; j++) {
    infile.get(c);  infile.get(c);
    S=0; Slength=0; possible=0;
		while (infile.get(c), c != ' '){
      cout << c << endl;
      S <<= 1;
      S += (c == '+') ? 1 : 0;
      Slength++;
    }
    Scomplete = (1<<(Slength))-1;
    infile >> K;
    possible = Scomplete == S;
    int i = 0, flips = 0;
    cout << j+1 << " " << Scomplete << " " << S << endl;
    for (; !possible && i<=Slength-K; i++) {
      if ( !( S & (1 << i ) ) ) {
        for (int k = 0, l = i; k < K; k++, l++) {
          S ^= (1 << l);
          cout << " _ " << S << endl;
        }
        cout << j+1 << " " << Scomplete << " " << S << endl;
        flips++;
      }
      possible = Scomplete == S;
    }
		outfile << "Case #" << j+1 <<": ";
    if (possible) outfile << flips << endl;
    else outfile << "IMPOSSIBLE" <<endl;
	}
	infile.close();
	outfile.close();
}

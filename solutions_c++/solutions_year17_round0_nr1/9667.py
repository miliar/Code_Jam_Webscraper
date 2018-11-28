#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;


int main() {
  string line, cakes;
  int pSep = 0, flipper, n = 0, i, tests;
  ifstream inputFile ("input.in");
  ofstream outFile ("outputs.txt");
  int k = 0, counter = 0, j, h;
  char cFace;
  bool nextLine = false;
  if (inputFile.is_open())
  {
  	if (getline (inputFile,line)){
        tests = atoi(line.c_str());
  	}
  	for (i = 1; i <= tests; i++){
        if (getline (inputFile,line)){
            nextLine = false;
            pSep = line.find(' ');
            cakes = line.substr(0, pSep);
            flipper = atoi(line.substr(pSep,line.size()).c_str());
            k = 0;
            counter = 0;
            while (k < cakes.size() - flipper) {
                cFace = cakes[k];
                if (cFace == '-') {
                    for (j = k; j < k + flipper; j++) {
                        if (cakes[j] == '-') cakes[j] = '+';
                        else cakes[j] = '-';
                    }
                    counter++;
                }
                k++;
            }
            cFace = cakes[cakes.size() - flipper];
            for (h = cakes.size() - flipper +1; h < cakes.size(); h++){
                if (cakes[h] != cFace){
                    nextLine = true;
                    outFile << "Case #" << i << ": IMPOSSIBLE\n";
                    break;
                }
            }
            if (cFace == '-') counter++;
            if (!nextLine){
                outFile << "Case #" << i << ": " << counter << "\n";
            }
        }
  	}
  	outFile.close();
    inputFile.close();
  }

  else cout << "Unable to open file";

  return 0;
}

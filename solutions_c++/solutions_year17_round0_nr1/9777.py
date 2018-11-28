#include <iostream>
#include <fstream>
#include <stdio.h>

void flip(int index, int num);
char pancake[1500];
using namespace std;

int main() {
  ofstream ofile;
  ofile.open("output.txt");
  int inputs;
  ifstream file;
  file.open("data.txt");
  file >> inputs;
  for (int z = 0; z <= inputs; z++) {
    for (int i = 0; i <= 1500; i++) {
      pancake[i] = '/';
    }
    int m = 0, numb, counter = 0, length;
    bool error = false, exit = true;
    file >> pancake >> numb;
    for (int i = 0; i <= 1500; i++) {
      if (pancake[i] == '/') {
        length = i - 1;
        break;
      }
    }
    pancake[length] = '/';
    while (exit) {
      switch (pancake[m]) {
        case '+':
          m++;
          break;
        case '-':
          if (pancake[m + numb - 1] == '/') {
            error = false;
            exit = false;
          }
          else flip(m, numb);
          m = 0;
          counter++;
          break;
      }
      if (m == length) {
        error = true;
        break;
      }
    }
    ofile << "Case #" << z+1 << ": ";
    if (error) ofile << counter << endl;
    else ofile << "IMPOSSIBLE" << endl;
  }
  cout << "best of luck!";
  return 0;
}

void flip(int index, int num) {
  int total = index + num;
  while (index < total) {
    switch (pancake[index]) {
      case '+':
        pancake[index] = '-';
        break;
      case '-':
        pancake[index] = '+';
        break;
    }
    index++;
  }
}

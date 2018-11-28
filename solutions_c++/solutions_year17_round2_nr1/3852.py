#include <iostream>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <math.h>
#include <algorithm>
#include <iomanip>

#include "armadillo"

using namespace std;
using namespace arma;


bool parse_inputs(const char* const fileName,
                  unsigned int& num_cases,
                  vector<vector<vector<unsigned long long> > >& N,
                  vector<unsigned long long>& D)
{
  fstream inputFile;

  inputFile.open(fileName, ios::in);
  if(!inputFile.is_open())
  {
    cerr << endl << "ERROR: Cannot open input file: "<< fileName  << endl << endl;
    exit(1);
  }

  unsigned long long n;
  unsigned long long d;

  unsigned long long k;
  unsigned long long s;

  inputFile >> num_cases;

  for(unsigned int c = 1; c <= num_cases; c++)
  {
    vector<vector<unsigned long long> > C;
    inputFile >> d;
    D.push_back(d);

    inputFile >> n;
    for(unsigned int i=0; i<n; i++)
    {
      vector<unsigned long long> h;
      inputFile >> k;
      inputFile >> s;

      h.push_back(k);
      h.push_back(s);
      C.push_back(h);
    }
    N.push_back(C);
  }

  inputFile.close();
  return true;
}


bool create_output(unsigned int& num_cases, vector<double>& A)
{
  fstream outputFile;

  outputFile.open("../Output", ios::out);
  if(!outputFile.is_open())
  {
    cerr << endl << "ERROR: Cannot open output file" << endl << endl;
    exit(1);
  }

  for(unsigned int c = 0; c < num_cases; c++)
  {
    outputFile << "Case #" << c+1 << ": " << fixed << setprecision(6) << A[c] << endl;
  }

  outputFile.close();
}

//double slowest_horse


int main(int argc, char* argv[])
{
  char* inputFileName;

  if(argc == 2)
  {
    inputFileName = argv[1];
  }
  else
  {
    cerr << endl << "ERROR: No input file provided." << endl << endl;
    exit(1);
  }

  unsigned int num_cases = 0;
  //--Inputs--//
  vector<vector<vector<unsigned long long> > > N;
  vector<unsigned long long> D;

  //--Outputs--//
  vector<double> A;
  //vector<unsigned long long> B;

  parse_inputs(inputFileName, num_cases, N, D);

  //--Kernal--//
  //vec input = conv_to< vec >::from(N);
  //vector<unsigned long long> output = conv_to< vector<unsigned long long> >::from(X);

  double slowest_time;
  for(unsigned int c=0; c<num_cases; c++)
  {
    unsigned long long k=N[c][0][0];
    unsigned long long s=N[c][0][1];
    slowest_time = double(double(D[c] - k) / double(s));
    for(unsigned int h=0; h<N[c].size(); h++)
    {
      k = N[c][h][0];
      s = N[c][h][1];

      if(double(double(D[c] - k) / double(s)) > slowest_time)
      {
        slowest_time = double(double(D[c] - k) / double(s));
      }
    }
    //slowest_time = double(double(D[c] - k) / double(s));
    A.push_back(double(D[c])/slowest_time);
  }

  create_output(num_cases, A);

  cout << endl << "COMPLETED SUCCESSFULLY!" << endl << endl;

  return 0;
}

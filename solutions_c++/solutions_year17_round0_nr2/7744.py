#include <iostream>
#include <stdlib.h>
//#include <sstream>
#include <vector>
#include <fstream>
#include <math.h>

using namespace std;

bool parse_inputs(const char* const fileName, unsigned int& num_cases, vector<unsigned long long>& inputs)
{
  fstream inputFile;

  inputFile.open(fileName, ios::in);
  if(!inputFile.is_open())
  {
    cerr << endl << "ERROR: Cannot open input file: "<< fileName  << endl << endl;
    exit(1);
  }

  unsigned long long test_case;

  inputFile >> num_cases;

  for(unsigned int c = 1; c <= num_cases; c++)
  {
    inputFile >> test_case;
    inputs.push_back(test_case);
  }

  inputFile.close();
  return true;
}


bool create_output(unsigned int& num_cases, vector<unsigned long long>& outputs)
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
    outputFile << "Case #" << c+1 << ": " << outputs[c] << endl;
  }

  outputFile.close();
}


vector<unsigned int> convert_to_vector(unsigned long long value)
{
  vector<unsigned int> num_vec;

  if(value == 0)
  {
    num_vec.push_back(0);
    return num_vec;
  }

  while(value)
  {
    num_vec.insert(num_vec.begin(), (value % int(10)));
    value = value / int(10);
  }
  return num_vec;
}


unsigned int tidy(vector<unsigned int> num_vec)
{
  /*for(unsigned int i=0; i<num_vec.size()-1; i++)
  {
    cout << num_vec[i] << " ";
  }
  cout << endl;*/

  for(unsigned int i=0; i<num_vec.size()-1; i++)
  {
    if(num_vec[i] > num_vec[i+1])
    {
      return (i+1);
    }
  }
  return 0;
}


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
  vector<unsigned long long> inputs;
  vector<unsigned long long> outputs;

  parse_inputs(inputFileName, num_cases, inputs);

  for(unsigned int c = 0; c < num_cases; c++)
  {
    unsigned long long number = inputs[c];

    while(number >= 0)
    {
      vector<unsigned int> num_vec = convert_to_vector(number);

      unsigned int position = tidy(num_vec);
      if(position == 0)
      {
        outputs.push_back(number);
        break;
      }
      else
      {
        number = number - (number % (unsigned long long)(pow(10, num_vec.size() - position))) - 1;
      }
    }
  }

  create_output(num_cases, outputs);

  cout << endl << "COMPLETED SUCCESSFULLY!" << endl << endl;

  return 0;
}

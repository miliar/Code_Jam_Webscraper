#include <iostream>
#include <stdlib.h>
#include <vector>
#include <fstream>
#include <math.h>
#include <algorithm>

using namespace std;

bool parse_inputs(const char* const fileName, unsigned int& num_cases, vector<unsigned long long>& N, vector<unsigned long long>& K)
{
  fstream inputFile;

  inputFile.open(fileName, ios::in);
  if(!inputFile.is_open())
  {
    cerr << endl << "ERROR: Cannot open input file: "<< fileName  << endl << endl;
    exit(1);
  }

  unsigned long long n;
  unsigned long long k;

  inputFile >> num_cases;

  for(unsigned int c = 1; c <= num_cases; c++)
  {
    inputFile >> n;
    N.push_back(n);

    inputFile >> k;
    K.push_back(k);
  }

  inputFile.close();
  return true;
}


bool create_output(unsigned int& num_cases, vector<unsigned long long>& max, vector<unsigned long long>& min)
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
    outputFile << "Case #" << c+1 << ": " << max[c] << " " << min[c] << endl;
  }

  outputFile.close();
}


unsigned int find_level(unsigned long long k)
{
  unsigned int level = 0;
  unsigned long long cumulative_total = 1;

  while(k > cumulative_total)
  {
    level += 1;
    cumulative_total += (unsigned long long)pow(2, level);
  }

  return level;
}


vector<unsigned long long> split(vector<unsigned long long>& empty_slots)
{
  vector<unsigned long long> split_slots;

  for(unsigned int i=0; i<empty_slots.size(); i++)
  {
    if(empty_slots[i] > 1)
    {
      if(empty_slots[i] % 2 == 0)
      {
        split_slots.push_back(empty_slots[i] / 2);
        split_slots.push_back((empty_slots[i] / 2) - 1);
      }
      else
      {
        split_slots.push_back((empty_slots[i] - 1) / 2);
        split_slots.push_back((empty_slots[i] - 1) / 2);
      }
    }
  }

  return split_slots;
}


unsigned long long cumulative_total(unsigned int level)
{
  unsigned int l=0;
  unsigned long long cumul_total = 0;

  while(l <= level)
  {
    cumul_total += (unsigned long long)pow(2, l);
    l += 1;
  }

  return cumul_total;
}


void allocate(vector<unsigned long long>& empty_slots,
              unsigned long long remaining_ppl,
              vector<unsigned long long>& max,
              vector<unsigned long long>& min)
{
  sort(empty_slots.begin(), empty_slots.end());

  unsigned int num_slots = empty_slots.size();
  unsigned long long slot_space = empty_slots[num_slots - remaining_ppl];

  unsigned long long calc_max;
  unsigned long long calc_min;

  if(slot_space % 2 == 0)
  {
    calc_max = slot_space / 2;
    calc_min = (slot_space / 2) - 1;
  }
  else
  {
    calc_max = calc_min = (slot_space - 1) / 2;
  }

  max.push_back(calc_max);
  min.push_back(calc_min);

  return;
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
  //--Inputs--//
  vector<unsigned long long> N;
  vector<unsigned long long> K;

  //--Outputs--//
  vector<unsigned long long> max;
  vector<unsigned long long> min;

  parse_inputs(inputFileName, num_cases, N, K);

  for(unsigned int c = 0; c < num_cases; c++)
  {
    unsigned long long level = find_level(K[c]);

    //cout << endl << "N: " << N[c] << "  K: " << K[c] << "  Level: " << level << endl;

    unsigned int l = 0;
    vector<unsigned long long> empty_slots;
    empty_slots.push_back(N[c]);

    while(l < level)
    {
      empty_slots = split(empty_slots);
      //cout << " l: " << l;
      l++;
    }
    //cout << endl;

    /*for(unsigned int i=0; i<empty_slots.size(); i++)
    {
      cout << empty_slots[i] << " ";
    }
    cout << endl;*/

    unsigned long long remaining_ppl;

    if(level == 0)
    {
      remaining_ppl = 1;
    }
    else
    {
      remaining_ppl = K[c] - cumulative_total(level-1);
    }

    //cout << "remaining_ppl: " << remaining_ppl << endl;

    allocate(empty_slots, remaining_ppl, max, min);

    //cout << "max: " << max[c] << "  min: " << min[c] << endl;
  }


  create_output(num_cases, max, min);

  //cout << endl << "COMPLETED SUCCESSFULLY!" << endl << endl;

  return 0;
}

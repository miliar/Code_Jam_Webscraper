#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <functional>
#include <unordered_map>

using namespace std;

void read(vector<pair<unsigned long long, unsigned long long> > &testValues) {
  ifstream fin("C-small-2-attempt0.in");
  int numTests;
  fin >> numTests;
  unsigned long long n, k;
  while(fin >> n >> k) {
    testValues.push_back(make_pair(n,k));
  }
  fin.close();
      
}

void write(vector<pair<unsigned long long, unsigned long long> > &solutions) {
  ofstream fout("bathroom_stall_solution.txt");
  for(int i = 0; i < solutions.size(); ++i) {
    fout << "Case #" << (i + 1) << ": " << solutions[i].first << " "
	 << solutions[i].second << "\n";
    cout << "Case #" << (i + 1) << ": " << solutions[i].first << " "
	 << solutions[i].second << "\n";  
  }
  fout.close();
}

void solver() {
  vector<pair <unsigned long long, unsigned long long> > testValues;
  read(testValues);
  vector<pair <unsigned long long, unsigned long long> > results;
  for (int i = 0; i < testValues.size(); ++i) {
    priority_queue<unsigned long long, vector <unsigned long long>, less<unsigned long long> > processing;
    unsigned long long people = testValues[i].second;
    unordered_map<unsigned long long, int> mapping;
    unsigned long long current = 0;
    mapping[testValues[i].first] = 1;
    processing.push(testValues[i].first);
    while(!processing.empty()) {
      unsigned long long temp = processing.top();
      processing.pop();
      current += mapping[temp];
      if (current >= people)
	{
	  results.push_back(make_pair(temp/2, (temp % 2 == 0 ? temp/2 - 1 :
					       temp/2)));
	  break;
	}
      if (temp % 2 != 0)
	{
	  unsigned long long value = temp/2;
	  if(mapping.find(value) == mapping.end())
	    processing.push(value);
	  mapping[value] += 2 * mapping[temp];
	}
      else
	{
	  unsigned long long value = temp/2;
	  if(mapping.find(value) == mapping.end())
	    processing.push(value);
	  if(mapping.find(value - 1) == mapping.end())
	    processing.push(value - 1);
	  mapping[value] += mapping[temp];
	  mapping[value - 1] += mapping[temp];
	}
    }

  }

  write(results);
}
  

int main() {
  solver();
  return 0;
}

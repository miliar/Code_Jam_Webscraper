#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

const uint64_t MAX_VALUE = 1000000000000000000;

void solve(unsigned test_id, uint64_t max_count);
unsigned debug = 0;

int main (int argc, char *argv[])
{
  //debug
  std::string arg = "";
  if(argc > 1)
  {
    arg = argv[1];
  }
  if(arg == "debug")
  {
    debug = 1;
  }

  //temp vars
  std::string input;
  std::stringstream ss;

  //get the number of test cases
  unsigned num_tests;
  std::getline (std::cin, input);
  ss.str(std::string()); ss.clear();
  ss.str(input);
  ss>>num_tests;  //1 <= num_tests <= 100
  
  if(num_tests < 1 || num_tests > 100)
  {
    cout<<"Number of testcases should be at least 1 and at most 100, input value ="<<num_tests<<endl;
    return 1;
  }
  if(debug)
  {
    cout<<"Number of tests to run: "<<num_tests<<endl;
  }

  std::vector<uint64_t> tests;
  tests.resize(num_tests);//allocates for all elements and constructs each elements

  //for each test, get the test data
  for(auto &test : tests)
  {
    std::getline (std::cin, input);
    ss.str(std::string()); ss.clear();
    ss.str(input);
    ss>>test;

    if(debug)
    {
      cout<<"input integer : "<<test<<endl;
    }

    if(test < 1 || test > MAX_VALUE)
    {
      cout<<"Input integer = "<<test<<", max_value = "<<MAX_VALUE<<endl;
      return 1;
    }
  }

  //solve each test
  if(debug) cout<<"======================== OUTPUT ==============================="<<endl;
  for(unsigned i=0;i<tests.size();i++)
  {
    if(debug) cout<<i+1<<" : "<<tests[i]<<endl;
    solve(i+1,tests[i]);
  }

  return 0;
}

void flip_str(std::string& val_str, unsigned idx)
{
  --val_str[idx];
  for(unsigned i=idx+1;i<val_str.size();i++)
  {
    val_str[i] = '9';
  }
}

bool is_tidy(uint64_t value)
{
  std::string val_str = std::to_string(value);
  char last_ch = '0';
  for(auto ch : val_str)
  {
    if(ch < last_ch)
      return false;
    last_ch = ch;
  }
  if(debug) cout<<"VERIFIED"<<endl;
  return true;
}

void solve(unsigned test_id, uint64_t input_value)
{
  if(debug) cout<<"INPUT: test_id = "<<test_id<<", input_value = "<<input_value<<endl;
  uint64_t max_tidy = 0;
  //solve
  std::string val_str = std::to_string(input_value);

  unsigned i=0;
  while(i<val_str.size()-1)
  {
    if(val_str[i] > val_str[i+1])
    {
      flip_str(val_str,i);
      i=0;
    }
    else
      i++;
  }
  stringstream ss(val_str);
  ss>>max_tidy;

  //error checks
  if(max_tidy > input_value)
    cout<<"ERROR: DEBUG: output is greater than input value"<<endl;

  if(!is_tidy(max_tidy))
    cout<<"ERROR: DEBUG: output is not tidy"<<endl;

  cout<<"Case #"<<test_id<<": "<<max_tidy<<endl;
}

#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

void solve(unsigned test_id, std::string& pancake_row, unsigned flip_capacity);
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

  class test_t
  {
    public:
      test_t():
        pancake_row("uninitialized"),
        flip_capacity(0)
    {};

      std::string pancake_row;
      unsigned flip_capacity;
  };

  std::vector<test_t> tests;
  tests.resize(num_tests);//allocates for all elements and constructs each elements

  //for each test, get the test data
  for(auto &test : tests)
  {
    std::getline (std::cin, input);
    ss.str(std::string()); ss.clear();
    ss.str(input);

    ss>>test.pancake_row;
    ss>>test.flip_capacity;

    if(debug)
    {
      cout<<"pancake row  : "<<test.pancake_row<<endl;
      cout<<"flip capacity: "<<test.flip_capacity<<endl;
    }

    if(test.flip_capacity < 2 || test.flip_capacity > test.pancake_row.size())
    {
      cout<<"Flip_capacity should be at least 2 and at most equal to length of pancake row size"<<endl;
      cout<<"Flip_capacity = "<<test.flip_capacity<<", row_size = "<<test.pancake_row.size()<<endl;
      return 1;
    }

    for(auto ch : test.pancake_row)
    {
      if(ch != '+' && ch != '-')
      {
        cout<<"pancake status should only contain '+' and '-'. Current value: "<<test.pancake_row<<endl;
        return 1; 
      }
    }
  }

  //solve each test
  if(debug) cout<<"======================== OUTPUT ==============================="<<endl;
  for(unsigned i=0;i<tests.size();i++)
  {
    if(debug) cout<<i+1<<" : "<<tests[i].pancake_row<<", "<<tests[i].flip_capacity<<endl;
    solve(i+1,tests[i].pancake_row, tests[i].flip_capacity);
  }

  return 0;
}


void solve(unsigned test_id, std::string& pancake_row, unsigned flip_capacity)
{
  if(debug) cout<<"INPUT: test_id = "<<test_id<<", pancake_row = "<<pancake_row<<", flip_capacity = "<<flip_capacity<<endl;

  unsigned num_pancakes = pancake_row.size();
  unsigned num_flips = 0;
  unsigned flip_idx = 0;
  unsigned max_flip_idx = num_pancakes - flip_capacity;
  
  if(debug) cout<<"max_flip_idx = "<<max_flip_idx<<endl;
  if(debug) cout<<"num_flips = "<<num_flips<<", flip_idx = "<<flip_idx<<", pancake_row = "<<pancake_row<<endl;
  while(flip_idx <= max_flip_idx)
  {
    if(pancake_row[flip_idx] == '-')
    {
      //flip:revert next flip_capacity elements
      for(unsigned i=flip_idx;i<flip_idx+flip_capacity;i++)
      {
        if(pancake_row[i] == '+')
          pancake_row[i] = '-';
        else
          pancake_row[i] = '+';
      }
      ++num_flips;
    }
    else
      ++flip_idx;

    if(debug) cout<<"num_flips = "<<num_flips<<", flip_idx = "<<flip_idx<<", pancake_row = "<<pancake_row<<endl;
  }

  if(pancake_row.rfind('-') != std::string::npos)
    cout<<"Case #"<<test_id<<": IMPOSSIBLE"<<endl;
  else
    cout<<"Case #"<<test_id<<": "<<num_flips<<endl;
}

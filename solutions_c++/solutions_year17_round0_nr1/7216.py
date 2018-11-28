#include <fstream>
#include "stdint.h"
#include <iterator>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <functional>
#include <queue>
#include <iterator>
#include <set>
#include <string>


struct TestCase
{
  uint64_t k_;
  std::string pancakes_;    
  
  friend std::istream& operator>>(std::istream & is, TestCase &test_case)
  {
    std::string line;
    std::getline(is, line);

    TestCase::parseData(line,test_case);

    return is;
  }

  static void parseData(const std::string &line, TestCase &test_case)
  {
    std::istringstream iss(line);

    iss >> test_case.pancakes_;
    iss >> test_case.k_;

    //std::cout << test_case.pancakes_ << " " << test_case.k_ <<std::endl;
  }
};

template <typename T>
class TestCaseResult
{
  std::vector<T> data_;

  friend std::ostream& operator<<(std::ostream &os,
				  const TestCaseResult<T> & result)
  {
    std::copy(
	      result.data_.begin(),
	      result.data_.end(),
	      std::ostream_iterator<T>(os, " "));

    return os;
  }

public:
  void addResult(const T& result)
  {
    data_.push_back(result);
  }

};


template<typename Out>
class PancakeFlipper
{
  private:
  template<typename Iter>
  bool NeedFlipping(Iter begin, Iter end)
  {
    return std::count(begin, end, '-');
  }
    
  template<typename Iter>
  bool CanFlip(Iter begin, Iter end, int k)
  {
    return std::distance(begin, end) >= k;
  }

  template<typename Iter>
  Iter FindNegative(Iter begin, Iter end)
  {
    return std::find(begin, end, '-');
  }

  template<typename Iter>
  void Flip(Iter begin, Iter end)
  {
    std::transform(begin, end, begin, [](char c) { if (c == '-') return '+'; else return '-';});
  }
  
public:
  TestCaseResult<Out> operator()(TestCase &test_case)
  {
    TestCaseResult<Out> test_case_result;

    auto num_of_flips = 0;
    auto end_iter = test_case.pancakes_.end();
    auto iter = test_case.pancakes_.begin();

    while (NeedFlipping(iter, end_iter))
      {
	std::cout << test_case.pancakes_ << std::endl;
	iter = FindNegative(iter, end_iter);
	if (CanFlip(iter, end_iter, test_case.k_))
	  {
	    Flip(iter, iter + test_case.k_);
	    ++num_of_flips; 
	  }
	else
	  {
	    num_of_flips = -1;
	    break;
	  }

      }
    std::cout << "Outcome is : " << num_of_flips << std::endl;
    
    test_case_result.addResult(num_of_flips >= 0 ? std::to_string(num_of_flips) : "IMPOSSIBLE");

    return test_case_result;
  }
};


template <typename Out>
class ProblemSolver
{
private:
  std::vector<TestCase> test_cases_;
  std::vector<TestCaseResult<Out>> test_case_results_;
  std::string input_file_name_;
  std::string output_file_name_;
  const std::function <TestCaseResult<Out>(TestCase&)> &algorithm_;
    
  void parseTestCases()
  {
    std::ifstream input_file(input_file_name_);
    uint64_t num_of_test_cases = 0;
		
    if (input_file.is_open())
      {
	std::string line;

	std::getline(input_file, line);
	std::istringstream iss(line);
	iss >> num_of_test_cases;

	for (uint64_t count = 0; count < num_of_test_cases; ++count)
	  {
	    std::copy(
		      std::istream_iterator<TestCase>(input_file),
		      std::istream_iterator<TestCase>(),
		      std::back_inserter(test_cases_));
	  }
	input_file.close();
      }
  }

  void applyAlgorithm()
  {		
    std::transform(begin(test_cases_), end(test_cases_),
		   std::back_inserter(test_case_results_),algorithm_ );
  }

  void printResults()
  {
    //Print results
    std::ofstream output_file(output_file_name_);
    size_t result_num = 0;

    for (auto & result : test_case_results_)
      {
	output_file << "Case #" << ++result_num << ": " 
		    << result << std::endl;;
      }
    output_file.close();
  }


public:
  ProblemSolver(const char *input_file_name,
		const char *output_file_name,
		const std::function <TestCaseResult<Out>(TestCase&)> &algorithm) :
    input_file_name_(input_file_name),
    output_file_name_(output_file_name),
    algorithm_(algorithm)
  {}

  void run()
  {
    parseTestCases();
    applyAlgorithm();
    printResults();
  }

};



int main(int argc, char* argv[])
{

  if (argc < 2)
    {
      std::cout << 
	"File name must be provided as a programm argument!" <<
	std::endl;

      return 1;
    }

  ProblemSolver<std::string> solver(argv[1], "output.txt", PancakeFlipper<std::string>());

  solver.run();

  return 0;
}


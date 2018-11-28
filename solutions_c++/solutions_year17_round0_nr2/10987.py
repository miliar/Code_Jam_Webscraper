//Jakob Gray

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <stdlib.h>

using namespace std;

double todubs (vector<int> vec) {

  double ret = 0;
  double multiplier = 1;

  for(int i=vec.size()-1; i>=0; i--) {
    //cout << vec[i] << endl;
    ret = ret + ((double)vec[i] * multiplier);
    multiplier = multiplier * 10;
    
  }
  return ret;
}



vector<int> organize (string str) {

  vector<int> nums;

  for (int i=0; i<str.length();i++) {

    nums.push_back(str.at(i)- '0');
    
  }

  if(nums.size() == 1) {
    return nums;
  }
  
  for(int i=0; i < nums.size()-1; i++) {
    
    if(nums[i+1] < nums[i]) {
      
      if(i==0) {
	nums[i] = nums[i] - 1;
	for(int j=i+1; j < nums.size(); j++) {
	    nums[j] = 9;
	  }
	
	return nums;
      }

      for(int j=i; j >= 0; j--) {
	if(j==0) {
	  nums[j] = nums[j] - 1;
	  for(int k=j+1; k < nums.size(); k++) {
	    nums[k] = 9;
	  }
	  return nums;
	  
	}

	if(nums[j-1] < nums[j]) {
	  nums[j] = nums[j] - 1;

	  for(int k=j+1; k < nums.size(); k++) {
	    nums[k] = 9;
	  }
	  return nums;
	}

      }
      
    }

  }

  return nums;
}


vector<string> readInFile(string filename) {
  vector<string> ret;
  string line;

  ifstream file(filename.c_str());

  getline (file,line);

  while(file.good()) {

    getline(file,line);
    ret.push_back(line);
  }
  
  return ret;

}

int main(int argc, char* argv[]) {

  string filename = argv[1];

  vector<string> numberList = readInFile(filename);
  
  for(int q=0; q < numberList.size()-1; q++) {

    vector<int> sorted = organize(numberList[q]);
    cout << "Case #" << q+1 << ": " << todubs(sorted) << endl;
    
    }

  return 0;
}

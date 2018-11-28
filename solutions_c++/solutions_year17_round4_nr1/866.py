#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

int getAnswer();

int main()
{
  int num_tests;
  cin >> num_tests;
  for (int test = 1; test <= num_tests; test++)
    cout << "Case #" << test << ": " << getAnswer() << "\n";
  return 0;
}

int getAnswer()
{
  int len, modval, result = 0;
  cin >> len >> modval;
  vector<int> nums(len);
  vector<int> num_copies(modval, 0);
  for (int i = 0; i < nums.size(); i++) {
    cin >> nums[i];
    num_copies[nums[i] % modval]++;
  }
  if (modval == 2) {
    result = num_copies[0] + (num_copies[1] + 1) / 2;
    return result;
  }
  else if (modval == 3) {
    result = num_copies[0];
    while (true) {
      if (num_copies[1] > 0 && num_copies[2] > 0) {
	num_copies[1]--;
	num_copies[2]--;
      }
      else if (num_copies[1] >= 3)
	num_copies[1] -= 3;
      else if (num_copies[2] >= 3)
	num_copies[2] -= 3;
      else {
	if (num_copies[1] > 0 || num_copies[2] > 0)
	  result++;
	return result;
      }
      result++;
    }
  }
  else if (modval == 4) {
    result = num_copies[0];
    // cout << num_copies[1] << endl;
    while (true) {
      if (num_copies[1] > 0 && num_copies[3] > 0) {
	num_copies[1]--;
	num_copies[3]--;
      }
      else if (num_copies[2] >= 2) {
	num_copies[2] -= 2;
	// cout << "Hi" << endl;
      }
      else if (num_copies[1] >= 2 && num_copies[2] >= 1) {
	// cout << "hi " << num_copies[1] << ' ' << num_copies[2] << endl;
	num_copies[1] -= 2;
	num_copies[2]--;
	// cout << "hello " << num_copies[1] << ' ' << num_copies[2] << endl;
      }
      else if (num_copies[2] >= 1 && num_copies[3] >= 2) {
	num_copies[2]--;
	num_copies[3] -= 2;
      }
      else if (num_copies[1] >= 4) {
	num_copies[1] -= 4;
	// cout << "here" << endl;
      }
      else if (num_copies[3] >= 4) {
	num_copies[3] -= 4;
      }
      else {
	// cout << result <<  ' ' << num_copies[1] << endl;
	if (num_copies[1] > 0 || num_copies[2] > 0 || num_copies[3] > 0) {
	  result++;
	}
	return result;
      }
      result++;
    }
  }
  else
    assert(false);
}


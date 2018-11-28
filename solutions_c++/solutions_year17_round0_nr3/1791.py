#include <iostream>
#include <map>

using namespace std;

long long finalLen(long long num_stalls, long long num_people);

int main()
{
  long long num_tests;
  cin >> num_tests;
  for (long long test = 1; test <= num_tests; test++) {
    long long num_stalls, num_people;
    cin >> num_stalls >> num_people;
    // cout << num_stalls << ' ' << num_people << endl;
    long long final_len = finalLen(num_stalls, num_people);
    cout << "Case #" << test << ": " << final_len / 2 << ' ' << (final_len - 1) / 2 << '\n';
  }
  return 0;
}

long long finalLen(long long num_stalls, long long num_people)
{
  num_people--;
  map<long long,long long> gaps;
  gaps[num_stalls] = 1;
  while (true) {
    map<long long,long long>::iterator it = gaps.end();
    it--;
    // cout << it->first << ' ' << it->second << ' ' << num_people << endl;
    if (it->second <= num_people) {
      num_people -= it->second;
      long long sub1 = (it->first - 1) / 2;
      long long sub2 = it->first / 2;
      if (gaps.count(sub1) > 0)
	gaps[sub1] += it->second;
      else
	gaps[sub1] = it->second;
      if (gaps.count(sub2) > 0)
	gaps[sub2] += it->second;
      else
	gaps[sub2] = it->second;
    }
    else
      return it->first;
    gaps.erase(it);
  }
}


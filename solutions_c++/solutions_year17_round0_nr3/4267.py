#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, m,k;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n >> m;  // read n and then m.
  //   int myints[] = {10,20,30,5,15};
  // std::vector<int> v(myints,myints+5);
  std::vector<int> v;

  v.push_back(n);
  std::make_heap (v.begin(),v.end());
  // std::cout << "initial max heap   : " << v.front() << '\n';
  for(k = 1;k<m;++k){

    int max = v.front();

    std::pop_heap (v.begin(),v.end());v.pop_back();

    v.push_back(max/2); std::push_heap (v.begin(),v.end());
    v.push_back((max-1)/2); std::push_heap (v.begin(),v.end());
  // std::cout << "max heap after push: " << v.front() << '\n';
  //
  // std::cout << "max heap after pop : " << v.front() << '\n';

  }

    // for(k=1;k<m;k*=2){}
    // k/=2;
    // int min = ((n)/k-1)/2;
    // int max = ((n)/k)/2;
    int min = ((v.front())-1)/2;
    int max = ((v.front()))/2;
    cout << "Case #" << i << ": " << max << " " << min << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}

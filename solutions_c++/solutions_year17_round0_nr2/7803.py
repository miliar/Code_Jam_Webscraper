#include <cmath>
#include <iostream>
#include <string>
#include <sstream>

using namespace std;

using ll = long long;

static ll stagger[] =
  { 1111111111111111111,
    111111111111111111,
    11111111111111111,
    1111111111111111,
    111111111111111,
    11111111111111,
    1111111111111,
    111111111111,
    11111111111,
    1111111111,
    111111111,
    11111111,
    1111111,
    111111,
    11111,
    1111,
    111,
    11,
    1
  };
			     
int main()
{
  int T;
  cin >> T;

  for(int i = 1; i <= T; ++i) {
    string input;
    cin >> input;

    stringstream sstr(input);
    ll ll_input;
    sstr >> ll_input;
    
    ll output = 0;

    for(int j = 0; j < input.size(); ++j) {
      ll val = stagger[19 - input.size() + j] * (input[j] - '0');
      ll marker = pow(10, input.size() - j - 1);
      
      if(val <= ll_input % (marker * 10)) {
	output -= output % (marker * 10);
	output += val;
      } else {
	ll header = ((val / marker) - 1) * marker;
	output -= output % (marker * 10);
	output += header + 9 * stagger[19 - input.size() + j + 1];
	break;
      }
    }

    cout << "Case #" << i << ": " << output << '\n';
  }
}

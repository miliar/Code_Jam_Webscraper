#include <iostream>
#include <sstream>

template <typename T> std::string NumberToString ( T Number ) {
	std::ostringstream ss;
	ss << Number;
	return ss.str();
}

using namespace std;

void main() {
  int t, n, result;
  string str;
  bool isTidy;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> n;

    for(int val = n; val >= 0; --val) {
	    str = NumberToString(val);
	    isTidy = true;

	    if(str.length() > 1) {

		    for(int j = 0; j < str.length() - 1; ++j) {
		    	char c1 = str[j];
		    	char c2 = str[j + 1];
		    	if(c1 - c2 > 0) {
		    		isTidy = false;
		    		break;
		    	}
		    }

	    }

	    if(isTidy) {
	    	result = val;
			break;
	    }
    }
    cout << "Case #" << i << ": " << result << endl;
  }

}

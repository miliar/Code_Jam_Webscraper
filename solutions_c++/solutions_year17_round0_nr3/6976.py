#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, num_stall, num_people;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> num_stall >> num_people;  // read n and then m.
    vector<int> v(1, num_stall);
    for(int j = 0; j < num_people; j++){
    	//vector<int> ml (0,v.size());    
    	//vector<int> mr (0,v.size());    
    	int ml, mr, index;
    	int maxL = 0;
    	int maxR = 0;
    	// for each interval, use the middlest
    	for(int k = 0; k < v.size(); k++) {
    		if(v[k] < 2){
    			ml = 0;
    			mr = 0;
    		}
    		else if(v[k]%2 == 1){
    			ml = (v[k]-1)/2;
    			mr = ml;
    		}
    		else{
    			mr = v[k]/2;
    			ml = mr-1;
    		}
			if(maxL < ml){
				maxL = ml;
				maxR = mr;
				index = k;
			}
			else if(maxL == ml && maxR < mr){
				maxL = ml;
				maxR = mr;
				index = k;
			}
		}
		if(j == num_people-1){
			cout << "Case #" << i << ": " << maxR << " " << maxL << endl;
		}
		// put divid k and provide the answer
		else{
			v[index] = maxL;
			v.insert(v.begin()+index, maxR);
		}
    }
    //cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}
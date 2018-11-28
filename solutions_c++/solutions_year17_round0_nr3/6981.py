#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
#include <math.h> 

using namespace std;  // since cin and cout are both in namespace std, this saves some text

void update(vector<long> & len, vector<long> & cn, long target, long cur_cn){
	if(target <= 0) return;
	if(len.empty()){
		len.push_back(target);
		cn.push_back(cur_cn);
		return;
	} 

	for(long i = len.size()-1; i>=0; i--){
		if(len[i] == target){
			cn[i] += cur_cn;
			break;
		}  
		else if(len[i] > target){
			len.insert(len.begin()+i+1, target);
			cn.insert(cn.begin()+i+1, cur_cn);
			break;
		}else if(i==0){
			len.insert(len.begin(),target);
			cn.insert(cn.begin(), cur_cn);
			break;
		}
	}
}

long* my_func(long n, long k){
	long lrs[2] = {0,0};
	vector<long> len (1,n);
	vector<long> cn (1,1);

	//pop the top of len_cn and calculate 
	long cur_len=0, cur_cn=0;
	while(k>0 && !len.empty()){
		cur_len = len.front(); // chose the largest subsection 
		cur_cn = cn.front();
		len.erase(len.begin());
		cn.erase(cn.begin());
		k -= cur_cn;
		cur_len--;
		lrs[0] = floor(cur_len / 2);
		lrs[1] = cur_len - lrs[0];

		// add lrs[1] to len_cn
		update(len, cn, lrs[1], cur_cn);
		update(len, cn, lrs[0], cur_cn);

		// for(int i=0; i<len.size();i++){
		// 	cout<< len[i]<<" "<<cn[i]<<endl;
		// }
		// cout<<"----------------"<<endl;
	}

	return lrs;


}


int main() {
  int t;
  long n, k;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n >> k;  // read n and then k.

    long* lrs = my_func(n,k);
    
    cout << "Case #" << i << ": " << lrs[1] << " " << lrs[0] << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 1;
}
#include <iostream>
#include <vector>

using namespace std;

int flips(string p, int k){
    //create an array of 1's and -1's
    vector<int> a(p.size());
    for(int i = 0; i < p.size(); ++i){
	(p[i]=='+') ? a[i] = 1 : a[i] = -1;
    }
    // find first -1 and flip n of them
    int counter = 0;
    int flips = 0;
    while(counter < a.size()){
       if(a[counter] == -1){
	  if(counter + k > p.size()) return -1;
	  for(int j = 0; j < k; j++){
	      a[counter + j]*=-1;
	  }
          flips++;
       }
       counter++;
    }
    return flips;
}

int main(){
   int t;
   cin >> t;

   for(int i = 0; i < t; ++i){
       string p = "";
       int k = 0;
       cin >> p >> k;
       cout <<"Case #" << i+1 << ": "<< flush; 
       int result = flips(p,k);
       if(result == -1){
           cout << "IMPOSSIBLE" << endl;
       } else {
           cout << result << endl;
       }
   }
   return 0;

}

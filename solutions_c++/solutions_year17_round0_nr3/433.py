#include <cstdlib>
#include <iostream>
#include <string.h>
using namespace std;
long long pow2[100];

void init_pow2(){
   pow2[0] = 1; 
   for(int i=1;i<100;i++)
       pow2[i] = 2*pow2[i-1];
}

int cal_level(long long k){
   int x = 1; 
   while(1) {
   	if(pow2[x-1] <= k && pow2[x]-1 >= k) break;
    else x++;
  }
   return x;
}

void cal_smaller_larger_count(long long * value, long long* count, long long n, int level){
   long long vacant = n - (pow2[level]-1);
   long long occu = pow2[level]; 
   count[1] = vacant - occu*(vacant/occu); // larger
   count[0] = pow2[level] - count[1]; 
   value[0] = vacant/occu; 
   value[1] = vacant/occu+1;
}

void parr(string str, long long * arr) {
   cout << str << "= [";
   cout << arr[0] << "," << arr[1] << "]" << endl;
}

int main(){
   init_pow2();
   int T; 
   cin >> T;
   for(int t=1;t<=T;t++){
   	  long long n, k;
      cin >> n >> k;
      int level = cal_level(k);
      int level_last = cal_level(n);
      cout << "Case #" << t << ": ";
      long long count_pre[2];
      long long value_pre[2];
      long long count[2];
      long long value[2]; 
      cal_smaller_larger_count(value, count, n, level);
      cal_smaller_larger_count(value_pre, count_pre, n, level-1);
      long long order_in_this_level = k-(pow2[level-1]-1);
      
      /*cout << "level=" << level << endl;
      parr("count_pre", count_pre);
      parr("value_pre", value_pre);
      parr("count", count);
      parr("value", value); */
      
      if(level != level_last) {
         if(value_pre[1]%2 == 0) { 
            if(order_in_this_level <= count_pre[1]) cout << value[1] << " " << value[0] << endl;
	        else cout << value[0] << " " << value[0] << endl;
	     }
	     else {
	  	    if(order_in_this_level <= count_pre[1]) cout << value[1] << " " << value[1] << endl;
	  	    else cout << value[1] << " " << value[0] << endl;
	     } 
      }
      else {
	     cout << "0 0" << endl;
	  
	  }
   }
}

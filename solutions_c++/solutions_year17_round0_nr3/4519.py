#include <iostream>
#include <math.h> 

using namespace std;

int main()
{
   int i, j, k, n_cases;
   long long int n_stalls, n_ppl, n_pplremain;
   long long int min_dist, max_dist, n_dist, n_distplusone;
   long long int pow2stall, pow2stall_length; //max(x) such that 2^x - 1 <= n_stalls 
   long long int pow2ppl, pow2ppl_length;     //max(y) such that 2^y - 1 <= n_ppl
   
   cin >> n_cases;
   
   for (i=0; i<n_cases; i++) {
       cin >> n_stalls >> n_ppl;

       // calculate max(x) such that 2^x - 1 <= n_stalls
       pow2stall = floor( log(n_stalls+1)/log(2) );
       pow2stall_length = pow(2,pow2stall);
       
       // calculate max(y) such that 2^y - 1 <= n_ppl
       pow2ppl = floor( log(n_ppl+1)/log(2) );
       pow2ppl_length = pow(2,pow2ppl);
       
       /* if n_ppl == 2^y-1 for integer y and n_stalls == 2^x-1 for integer x:
          there are 2^x groups of equal distance [calculated by first floor function]
          
          if n_stalls > 2^x-1, (n_stalls - 2^x + 1) is split evenly among the groups 
       */
       min_dist = floor( pow2stall_length/pow2ppl_length - 1 ) + 
                  floor( (n_stalls + 1.0 - pow2stall_length) / pow2ppl_length );
       
       // amount to split % amount of groups == leftover 1s that's spread into groups
       n_distplusone = (n_stalls + 1 - pow2stall_length) % pow2ppl_length;
       n_dist = pow2ppl_length - n_distplusone;
       
       
       /*
       cout << min_dist * n_dist + max_dist * n_distplusone + pow2ppl_length << endl;
       cout << "N_stalls: " << n_stalls << " N_ppl: " << n_ppl << " m: " << min_dist << endl;
       cout << "N_mplus: " << n_distplusone << " N_m: " << n_dist << endl;
       */
      
       /* At this point, we know what it looks like for n_stall and n_ppl == 2^y - 1
          Just have to adjust min/max dist for n_ppl - 2^y + 1 (ppl remaining)
       */
      
       n_pplremain = n_ppl - pow2ppl_length + 1;
       
       if (n_pplremain == 0 && n_dist>n_distplusone) {
           max_dist = min_dist;
       } else {
           max_dist = min_dist + (n_distplusone > 0);
       }
       
       if (n_pplremain > 0) {
           if (n_pplremain <= n_distplusone) {
                min_dist = floor( (max_dist-1.0)/2 );
                max_dist = ceil ( (max_dist-1.0)/2 );
            } else if (n_pplremain > n_distplusone) {
                max_dist = ceil ( (min_dist-1.0)/2 );
                min_dist = floor( (min_dist-1.0)/2 );
            }
       }

       cout << "Case #" << i+1 << ": " << max_dist << " " << min_dist;
       //n_pplremain = n_ppl>pow2stall_length;
       //cout << endl << "n>... : " << n_pplremain; 
       if (i < n_cases-1) {
           cout << endl; 
       }
   }
    
   return 0;
}
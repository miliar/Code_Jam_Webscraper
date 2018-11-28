#include <iostream>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

pair<long long int,long long int> 
take(long long int count, long long int n) {
       if(n==1){
           return make_pair(count/2, (count-1)/2);
       }
       if(n%2){
               return take((count-1)/2, n/2);
       } else {
               return take(count/2, n/2);
       }
}

int main()
{
    long long int N;
    long long int c,n;
    cin>>N;
    
    for(long long int i=0; i<N; ++i){
            cin>>c>>n;
            pair<long long int, long long int> p = take(c, n);
            cout<<"Case #"<<i+1<<": "<<p.first<<" "<<p.second<<"\n";
    
    }
return 0;
}
 

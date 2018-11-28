#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <iomanip>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
  
 
    long int t;
  
    cin>>t;
    for(int i=0;i<t;i++)
        {
        double max=0;
        long int d,n;
        cin>>d>>n;
        for(int j=0;j<n;j++)
            {
            long int h,s;
            cin>>h>>s;
            double temp=(d-h)*1.0/s*1.0;
            if(temp>max)
                max=temp;
            
        }
        double temp=d*1.0/max;
        cout<<"Case #"<<i+1<<": "<<setprecision(8)<<temp<<endl;
    }
}


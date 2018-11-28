#include <iostream>
#include <vector> 
#include <queue>
#include <map> 
#include <set>
#include <utility> //Pair
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <bitset>
#include <limits>
#include <iomanip>
#include <sstream>
#define pb push_back
#define mp make_pair
#define mod 1000000007
using namespace std;
double solve(){
    int d,n;
    cin>>d>>n;
    double grt=0;
    while(n--){
        double tempd,temps;cin>>tempd>>temps;
        double temp=(d-tempd)/temps;
        if(temp>grt){
            grt=(d-tempd)/temps; 
        }
    }
    return d/grt;
}
int main(){
	int t;
	cin>>t;
	int count=1;
	while(t--){
	    cout << fixed << setprecision(6);
		cout<<"Case #"<<count<<": "<<solve()<<endl;
		count++;
	}
}

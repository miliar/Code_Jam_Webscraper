#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>


#define MOD 1000000007
#define ll long long
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define pll pair<long long,long long>
#define PI 3.14159

using namespace std;

int main() {
	// your code goes here
    ll t;
    cin>>t;
    for(ll k=1;k<=t;k++){
        double d,n;
        cin>>d>>n;
        vector<double>kilo(n);
        vector<double>speed(n);
        
        for(ll i=0;i<n;i++){
            cin>>kilo[i]>>speed[i];
            
        }
        double maxi=-1;
        for(ll i=0;i<n;i++){
            if((d-kilo[i])/speed[i]>maxi){
                maxi=(d-kilo[i])/speed[i];
            }
        }
        printf("Case #%lld: %.6f\n",k,d/maxi);
    }
	return 0;
}

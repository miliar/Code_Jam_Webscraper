//chiragjn
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <climits>
#include <iomanip>
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define gibe_de_fast_io_b0ss ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;
const ll mod = 1e9 + 7;
const ll INF = 0x7FFFFFFFFFFFFFFF/2;
int main(){
    gibe_de_fast_io_b0ss;
    int t;
    cin>>t;
    const double pi = 3.14159265358979323;
    for(int T=1;T<=t;T++){
        int n,k;
        cin>>n>>k;
        vector<pair<double, double>> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i].ff>>arr[i].ss;
        }
        double gans = 0;
        sort(arr.begin(), arr.end());
        reverse(arr.begin(), arr.end());
        for(int z=0;z<arr.size();z++){
            double c = (arr[z].ff * arr[z].ff) + (2 * arr[z].ff * arr[z].ss);
            vector<double> surf;
            for(int i=z+1;i<arr.size();i++){
                surf.pb(2 * arr[i].ff * arr[i].ss);
            }
            if(surf.size() >= k-1){
                sort(surf.begin(), surf.end());
                reverse(surf.begin(), surf.end());
                for(int i=0;i<k-1;i++){
                    c += surf[i];
                }
                double ans = c * pi;
                gans = max(gans, ans);
            }
            
        }
    	cout<<"Case #"<<T<<": "<<setprecision(9)<<fixed<<gans<<"\n";
    }
    return 0;
}

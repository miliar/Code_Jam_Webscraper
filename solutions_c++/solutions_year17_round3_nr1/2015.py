#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

double ans;
const double pi=3.1415926535897932384626433832795028841971693;

void calculate(vector<int> combos, vector<pair<double,double> > pa){
  double i;
  double temp;
  for (i=combos.size()-1;i>0;i--){
    temp+=pi*2*pa[combos[i]].first*pa[combos[i]].second;
    temp+=pi*pa[combos[i]].first*pa[combos[i]].first;
    temp-=(pa[combos[i-1]].first*pi*pa[combos[i-1]].first);
  }
  temp+=pa[combos[0]].first*pa[combos[0]].first*pi+
        pi*2*pa[combos[0]].first*pa[combos[0]].second;
  if (temp>ans) ans=temp;
}

void permutate(int k, int n, int pre, vector<int> combos, vector<pair<double,double> > pa){
  if (combos.size()==k){
    calculate(combos,pa); 
    return;
  }
  int i;
  for (i=pre+1;i<n;i++){
    combos.push_back(i);
    permutate(k,n,i,combos,pa);
    combos.erase(combos.begin()+combos.size()-1);
  }
}

int main(){
  ifstream infile;
  ofstream outfile;
  infile.open("syrup.in");
  outfile.open("syrup.txt");
  double i,j,t,n,k,r,h;
  infile >> t;
  for (i=0;i<t;i++){
    infile >> n >> k;
    vector<pair<double,double> > pan;
    for (j=0;j<n;j++){
      infile >> r >> h;
      pan.push_back(make_pair(r,h)); 
    }
    sort(pan.begin(),pan.end());
    vector<int> combos;
    ans=-1;
    permutate(k,n,-1,combos,pan);
    outfile << "Case #" << (int) i+1 << ": " << fixed << setprecision(9) << ans << endl; 
  }
  return 0;
}

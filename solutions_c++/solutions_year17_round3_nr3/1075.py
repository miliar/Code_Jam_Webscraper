#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main(){
  ifstream infile;
  ofstream outfile;
  infile.open("ai.in");
  outfile.open("ai.txt");
  double i,j,i2,j2,n,k,t;
  double u,tp;
  infile >> t;
  for (i=0;i<t;i++){
    infile >> n >> k >> u;
    vector<double> prob;
    for (j=0;j<n;j++){
      infile >> tp;
      prob.push_back(tp); 
    } 
    sort(prob.begin(),prob.end());
    vector<double> final;
    int counter=0;
    for (j=prob.size()-1;j>=0;j--){
      if (counter==k) break;
      counter++;
      final.push_back(prob[j]);
    }
    sort(final.begin(),final.end());
    double num=1,ans=1,total=1;
    if (final.size()==1){
      //ans=(1-final[0]+min(u,1.0));
      //for (j=0;j<final.size();j++) total*=(1-prob[j]);
      //outfile << "Case #" << i+1 << ": " << fixed << setprecision(6)
      //        << 1-total*ans << endl; 
      outfile << "Case #" << (int) i+1 << ": " 
              << fixed << setprecision(6) << final[0]+min(u,1.0) << endl;
      continue;
    }
    while (1){
      double goal=num,amount=(final[num]-final[0])*num;
      if (goal>=final.size()){
        for (j=0;j<num;j++) final[j]+=(u/num); 
        break;
      }
      for (j=0;j<num;j++)
        final[j]+=min(u/num,amount/num);
      u-=amount;
      num++;
      if (u<=0) break;
    }
    for (j=final.size();j<prob.size();j++) prob[j]=final[j-final.size()];
    for (j=0;j<final.size();j++) ans*=final[j]; 
    for (j=0;j<final.size();j++) total*=(1-prob[j]);
    if (j==k){
      outfile << "Case #" << (int) i+1 << ": " << fixed << setprecision(6)
              << ans << endl; 
    }
  }
  return 0;
}

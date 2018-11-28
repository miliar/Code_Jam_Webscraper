#include <iostream>
#include <fstream>
#include <set>
#include <queue>
#include <utility>
using namespace std;

struct Comparator{
  bool operator()(const pair<pair<int,int>, int>& lhs,const pair<pair<int,int>,int>& rhs) const{
    if (lhs.first.first==rhs.first.first){
      if (lhs.first.second!=rhs.first.second) return lhs.first.second>rhs.first.second; 
      return lhs.second<rhs.second;
    } 
    else return lhs.first.first<rhs.first.first;
  }
};

pair<int,int> optimal(int start, int end){
  return make_pair(min((end-start-2)/2,end-start-2-(end-start-2)/2),
                   max((end-start-2)/2,end-start-2-(end-start-2)/2)); 
}

int main(){
  ifstream infile;
  ofstream outfile;
  infile.open("bath.in");
  outfile.open("bath.txt");
  int i,j,t,n,k;
  infile >> t;
  for (i=0;i<t;i++){
    infile >> n >> k;
    priority_queue<pair<pair<int,int> ,int> > ps;
    pair<int,int> find=optimal(0,n+1);
    ps.push(make_pair(find,0));
    for (j=0;j<k;j++){
      int biggest1=(ps.top()).first.first,biggest2=(ps.top()).first.second;
      int position=(ps.top()).second+1+biggest1;
      //pair<pair<int,int>, int> placeholder=make_pair(make_pair(biggest1,
      //                                     biggest2), position-1-biggest1);
      //ps.erase(placeholder);
      ps.pop();
      ps.push(make_pair(optimal(position-1-biggest1,position),
                          position-1-biggest1));
      ps.push(make_pair(optimal(position,position+1+biggest2),position));
      if (j==k-1) 
        outfile << "Case #" << i+1 << ": " << biggest2 << " " << biggest1 << endl;
    }
  }
  return 0;
}

#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int solve();

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    cout<<"Case #"<<i+1<<": "<<solve()<<'\n';
  }
}

const int NONE=999999999;

pair<int,int> make_range(int amount,int requirement);
int find_next_level(vector<vector<pair<int,int> > >& ranges,int level);
bool test(vector<vector<pair<int,int> > >& ranges,int level);

int solve(){
  int ingredients,packages;
  cin>>ingredients>>packages;
  vector<vector<pair<int,int> > > ranges(ingredients);
  vector<int> requirement(ingredients);
  for(int i=0;i<ingredients;i++)
    cin>>requirement[i];
  for(int i=0;i<ingredients;i++)
    for(int p=0;p<packages;p++){
      int amount;
      cin>>amount;
      //cout<<amount<<": ";
      pair<int,int> range=make_range(amount,requirement[i]);
      //cout<<range.first<<'-'<<range.second<<'\n';
      if(range.first<=range.second)
        ranges[i].push_back(range);
    }

  for(int i=0;i<ingredients;i++)
    sort(ranges[i].begin(),ranges[i].end());

  int ret=0,level=0;
  while(true){
    level=find_next_level(ranges,level);
    //cout<<"try: "<<level<<'\n';
    if(level==NONE)
      break;

    while(test(ranges,level))
      ret++;
  }

  return ret;
}

pair<int,int> make_range(int amount,int requirement){
  int min=(amount*10+11*requirement-1)/(11*requirement);
  int max=(amount*10)/(requirement*9);
  return make_pair(min,max);
}

bool in(int level,const pair<int,int>& range){
  return range.first<=level && level<=range.second;
}

bool test(vector<vector<pair<int,int> > >& ranges,int level){
  for(int i=0;i<ranges.size();i++)
    if(ranges[i].size()==0 || !in(level,ranges[i][0]))
      return false;
  for(int i=0;i<ranges.size();i++)
    ranges[i].erase(ranges[i].begin());
  return true;
}

bool better(int guess,int next,int level){
  return guess>level && guess<next;
}

int find_next_level(vector<vector<pair<int,int> > >& ranges,int level){
  int next=NONE;
  for(int i=0;i<ranges.size();i++){
    while(ranges[i].size()>0 && ranges[i][0].second<=level)
      ranges[i].erase(ranges[i].begin());
    if(ranges[i].size()==0)
      return NONE;
    if(better(ranges[i][0].first,next,level))
      next=ranges[i][0].first;
    if(better(ranges[i][0].second,next,level))
      next=ranges[i][0].second;
  }
  return next;
}

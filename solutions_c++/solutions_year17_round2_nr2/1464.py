#include<iostream>
#include<vector>
#include<algorithm>
#include <sstream>      // std::stringstream

using namespace std;

vector< pair<int,char> > inp;

int main(){
  int t,n,r,o,y,g,b,v,i;
  std::stringstream ss;
  cin>>t;
  string out;
  for(int zz=1;zz<=t;zz++){
    i=0;
    cin>>n;
    cin>>r;
    cin>>o;
    cin>>y;
    cin>>g;
    cin>>b;
    cin>>v;
    inp.push_back(make_pair(r,'R'));
    inp.push_back(make_pair(y,'Y'));
    inp.push_back(make_pair(b,'B'));
    sort(inp.begin(),inp.end());
    while(inp[2].first){
      if(inp[2].first){
        ss<<inp[2].second;
        inp[2].first--;
        i++;
      }
      if(inp[1].first){
        ss<<inp[1].second;
        inp[1].first--;
        i++;
        if(inp[1].first==0){
          if(inp[2].first){
            ss<<inp[2].second;
            inp[2].first--;
            i++;
          }
        }
        if(inp[2].first>inp[0].first){
          continue;
        }
      }
      if(inp[0].first){
        ss<<inp[0].second;
        inp[0].first--;
        i++;
      }
    }
    //out[i]='\0';
    ss>>out;
    if(out[out.length()-1]==out[out.length()-2]||out[out.length()-1]==out[0]){
      printf("Case #%d: IMPOSSIBLE\n",zz);
      // cout<<out;
    }
    else{
      printf("Case #%d: ",zz);
      cout<<out<<endl;
    }
    ss.clear();
    inp.clear();
  }
  return 0;
}

#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())



int main(){

  int i,k;
  int run,runs;
  scanf("%d",&runs);
  char buf[10000];
  for(run=1;run<=runs;run++){
    printf("Case #%d: ",run);
    scanf("%s %d",buf, &k);
    string s=buf;
    vector<bool> backflip(3*sz(s),false);
    bool oldflip=false;
    int numflips=0;
    for(i=0;i<sz(s);i++){
      if(backflip[i]) 
        oldflip=!oldflip;
      if(oldflip){
        s[i]='+'+'-'-s[i];
      }
      if(i<=sz(s)-k){
        if(s[i]=='-') {
          s[i]='+';        
          oldflip=!oldflip;
          numflips++;
          backflip[i+k]=true;
        }
      
      } else {
        if(s[i]=='-')
          numflips=-1;
      }
    }
    //printf("(%s) ", s.c_str());
    if(numflips==-1) printf("IMPOSSIBLE\n"); else printf("%d\n",numflips);
  
  }




  return 0;
}


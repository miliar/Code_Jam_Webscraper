#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

typedef pair<int,int> PII;
typedef long long LL;

#define ALL(x) x.begin(),x.end()

#define DEB(args...) fprintf(stderr,args)

#define PB push_back
#define MP make_pair
#define ST first
#define ND second 

const int INF = 0x3f3f3f3f;

int qtd[6];

map<string,int> mp;
char aux[] = {'R','O','Y','G','B','V'};


int main(){
    int t;
    scanf("%d", &t);
    for(int cas = 1; cas <= t; cas++){
        string ans = "";
        int n;
        scanf("%d", &n);
        mp["R"]=0;
        mp["O"]=1;
        mp["Y"]=2;
        mp["G"]=3;
        mp["B"]=4;
        mp["V"]=5;      
        for(int i = 0; i < 6; i++){
            scanf("%d",&qtd[i]);
        }
        qtd[mp["R"]]-=qtd[mp["G"]];
        qtd[mp["Y"]]-=qtd[mp["V"]];
        qtd[mp["B"]]-=qtd[mp["O"]];
        int ok = 1;
        if(qtd[mp["R"]]<0 || qtd[mp["Y"]]<0 || qtd[mp["B"]]<0){
            ok = 0;
        }
        int mx = 0, id = 0;
        int sum = 0;

        printf("Case #%d: ", cas);
        if(qtd[mp["G"]]>0 && qtd[mp["R"]]==0){

            if(qtd[mp["B"]]==0 && qtd[mp["O"]]==0 && qtd[mp["Y"]]== 0 && qtd[mp["V"]]==0){
                ans = "";
                for(int i = 0; i < qtd[mp["G"]]; i++){
                    ans += "RG";
                }
                printf("%s\n",ans.c_str());
            }
            else{
                puts("IMPOSSIBLE");                
            }
        }
        else if(qtd[mp["O"]]>0 && qtd[mp["B"]]==0){
            if(qtd[mp["R"]]==0 && qtd[mp["G"]]==0 && qtd[mp["Y"]]== 0 && qtd[mp["V"]]==0){
                ans = "";
                for(int i = 0; i < qtd[mp["O"]]; i++){
                    ans += "OB";
                }
                printf("%s\n",ans.c_str());
            }
            else{
                puts("IMPOSSIBLE");                
            }
        }
        else if(qtd[mp["V"]]>0 && qtd[mp["Y"]]==0){
            if(qtd[mp["R"]]==0 && qtd[mp["G"]]==0 && qtd[mp["O"]]== 0 && qtd[mp["B"]]==0){
                ans = "";
                for(int i = 0; i < qtd[mp["V"]]; i++){
                    ans += "VY";
                }
                printf("%s\n",ans.c_str());
            }
            else{
                puts("IMPOSSIBLE");              
            }
        }
        else{
          for(int i = 0; i < 6; i+=2){
              if(mx<qtd[i]){
                  mx = qtd[i];
                  id = i;

              }
              sum += qtd[i];
          }
          int id2,id3;
          if(id == 0){
              id2=2;
              id3=4;
          }
          else if(id == 2){
              id2 = 0;
              id3 = 4;
          }
          else{
              id2 = 0;
              id3 = 2;
          }
          //printf("%d %d\n",sum-mx, mx);

          if(sum-mx<mx){
              ok = 0;
          }
          else{

              for(int i = 0; i < mx; i++){
                  ans += aux[id];
                  if(qtd[id2]>qtd[id3]){
                      ans +=  aux[id2];
                      qtd[id2]--;
                  }
                  else{
                      ans +=  aux[id3];
                      qtd[id3]--;                    
                  }
              }
              while(qtd[id2]>0 || qtd[id3]>0){
                  if(qtd[id2]>qtd[id3]){
                      ans +=  aux[id2];
                      qtd[id2]--;
                  }
                  else{
                      ans +=  aux[id3];
                      qtd[id3]--;                    
                  }                
              }
          }
          //printf("%s\n",ans.c_str());
          if(ok){
              for(int i = 0; i < ans.size(); i++){

                  while(ans[i]=='R' && qtd[mp["G"]]>0){
                      printf("RG");
                      qtd[mp["G"]]--;
                  }
                  while(ans[i]=='B' && qtd[mp["O"]]>0){
                      printf("BO");
                      qtd[mp["O"]]--;
                  }
                  while(ans[i]=='Y' && qtd[mp["V"]]>0){
                      printf("YV");
                      qtd[mp["V"]]--;
                  }
                  printf("%c",ans[i]);
              }
              printf("\n");
          }
          else{
              puts("IMPOSSIBLE");
          }
        }
    }
    
}

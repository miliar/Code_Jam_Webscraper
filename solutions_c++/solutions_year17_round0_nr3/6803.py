#include<bits/stdc++.h>
using namespace std;

void open(){ freopen("input.txt","r",stdin);
				freopen("output.txt","w",stdout);}

int main(){
    open();
   int T,N,K;
   scanf("%d",&T);
   for(int t=1;t<=T;t++){
     scanf("%d%d",&N,&K);
     vector<int> vec;
     vec.push_back(1);
     vec.push_back(N+2);
     int si=0,ei=1,pos;
     for(int i=1;i<=K;i++){
        sort(vec.begin(),vec.end());
        int maxdiff=0;
        for(int j=0;j<vec.size()-1;j++){
            if(maxdiff<(vec.at(j+1)-vec.at(j))){
                maxdiff=(vec.at(j+1)-vec.at(j));
                si=j;
            }
        }
        pos=vec.at(si)+(int)ceil((maxdiff)/2.0);
        vec.push_back(pos);
     }
     sort(vec.begin(),vec.end());

     int left,right;
     for(int i=0;i<vec.size();i++){
        if(vec.at(i)==pos){
            left=vec.at(i)-vec.at(i-1)-1;
            right=vec.at(i+1)-vec.at(i)-1;
        }
     }
     printf("Case #%d: %d %d\n",t,left,right);
   }
  return 0;
}

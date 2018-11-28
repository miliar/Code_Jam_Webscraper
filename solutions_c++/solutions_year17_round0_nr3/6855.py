#include <iostream>
#include <vector>

using namespace std;

void lastmm(long long int n,long long int k){
  long long int left,right,i,j,in,ax,max,min;
  vector<bool> sides(n,0);

  for(int p=0;p<k;p++){

    vector<long long int> index_mins,index_maxs;
    max=-1,min=-1;

    for(i=0;i<n;i++){
        if(sides[i]==0){
          left=0;
          right=0;
          for(j=i-1;j>=0;j--){
            if(sides[j]==1)
              break;
            else
              left++;
          }
          for(j=i+1;j<n;j++){
            if(sides[j]==1)
              break;
            else
              right++;
          }
          if(left<right){
            in=left;
            ax=right;
          }
          else{
            in=right;
            ax=left;
          }
          if(in==min){
            index_mins.push_back(i);
            if(ax==max){
              index_maxs.push_back(i);
            }
            if(ax>max){
              max=ax;
              index_maxs.clear();
              index_maxs.push_back(i);
            }
          }
          if(in>min){
            min=in;
            index_mins.clear();
            index_maxs.clear();
            max=ax;
            index_mins.push_back(i);
            index_maxs.push_back(i);
          }
        }
    }
    sides[index_maxs[0]]=1;
  }
  
  cout << max << " " << min << endl;
}

int main( void ) {

  int T;
  long long int n,k;

  scanf("%d",&T);

  for(int t=0;t<T;t++){
    scanf("%lli",&n);
    scanf("%lli",&k);
    cout << "Case #" << t+1 << ": ";
    lastmm(n,k);
  }

  return 0;
}

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct stall_value{
  int LS = 0;
  int RS = 0;
};

// Row of stalls. true if occupied.
vector<bool> stalls;
int N,K;
int last_stall;

int LS( int n ){
  int ls = 0;
  while( !stalls[--n] ){
    ++ls;
  }
  return ls;
}

int RS( int n ){
  int rs = 0;
  while( !stalls[++n] ){
    ++rs;
  }
  return rs;
}

void pick_stall(){
  vector<stall_value> stall_values( stalls.size() );
  int max_Ls_Rs = 0;
  int min_Ls_Rs = 0;

  // Calculate Ls and Rs.
  for( int n=0; n<N+2; ++n ){
    if( !stalls[n] ){
      stall_values[n].LS = LS(n);
      stall_values[n].RS = RS(n);
      int minimum = min(stall_values[n].LS, stall_values[n].RS);
      if( minimum > min_Ls_Rs ){
        min_Ls_Rs = minimum;
      }
    }
  }
  // Calculate max_Ls_Rs for stalls where min(Ls,Rs) == min_Ls_Rs.
  for( int n=0; n<N+2; ++n ){
    if(min(stall_values[n].LS, stall_values[n].RS) == min_Ls_Rs){
      int maximum = max(stall_values[n].LS, stall_values[n].RS);
      if( maximum > max_Ls_Rs ){
        max_Ls_Rs = maximum;
      }
    }
  }
  // Pick stall.
  for( int n=0; n<N+2; ++n){
    if( !stalls[n] ){
      int minimum = min(stall_values[n].LS, stall_values[n].RS);
      int maximum = max(stall_values[n].LS, stall_values[n].RS);
      if(minimum == min_Ls_Rs && maximum == max_Ls_Rs){
        stalls[n] = true;
        last_stall = n;
        return;
      }
    }
  }
}

int main(){
  int T;
  cin >> T;
  for( int t=1; t<=T; ++t ){
    cin >> N >> K;
    stalls = vector<bool>( N+2 );
    stalls[0] = true;
    stalls[stalls.size()-1] = true;

    for( int k=0; k<K; ++k ){
      pick_stall();
    }

    cout << "Case #" << t << ": " << max(LS(last_stall),RS(last_stall)) << " " << min(LS(last_stall),RS(last_stall)) << endl;
  }
}

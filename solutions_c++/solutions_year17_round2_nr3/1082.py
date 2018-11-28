#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;


int main(){
  ios_base::sync_with_stdio(false);
  int T;
  int N, q, i, j;
  cin >> T;
  for(int ind=0; ind<T; ind++){
    cin >> N >> q;
    vector<int>e(N, 0);
    vector<int>s(N, 0);
    for(i=0; i<N; i++)
      cin >> e[i] >> s[i];
    vector<long long>d(N-1, 0);
    for(i=0; i<N; i++){
      long long temp;
      if(i<N-1){
        for(j=0; j< (i+2); j++) cin >> temp;
        d[i] = temp;
        for(;j<N; j++) cin >> temp;
      } else {
        for(int j=0; j<N; j++) cin >> temp;
      }
    }
    int temp;
    cin >> temp >> temp;
    vector<long long>D(N, 0);
    D[N-1]  = 0;
    for(i=N-2; i>=0; i--) D[i] = D[i+1]+d[i];
    
//    for(i=0; i<N-1; i++)
//      cout << "d["<<i<<"] = " << d[i] << endl;
    
//   for(i=0; i<N; i++)
//      cout << "D["<<i<<"] = " << D[i] << endl;
    
    
    vector<double>F(N, 0);
    F[0] = 0;
    //cout << "go" << endl;
    for(i=1; i<N; i++){
      double minim=-1;
      double temp;
      for(j=0; j<i; j++){
        if(D[j]-D[i] > e[j]) continue;
        //cout << "i = " << i << ", j = " << j << endl;
        temp = F[j] + (double)(D[j]-D[i]+0.0)/s[j];
        //cout << D[j]-D[i] << ", " << s[j] << endl;
        //cout << "temp = " << temp << endl;
        if(minim<0) minim = temp;
        else if(minim > temp) minim = temp;
      }
      if(minim==-1)
        cout <<"WRONG" << endl;
            F[i] = minim;
    //cout << "F["<<i<<"] =" << F[i] << endl;
    } 
  
    cout << "Case #" << (ind+1) << ": " << setprecision(10) << F[N-1] << endl;
  }
  return 0;
}
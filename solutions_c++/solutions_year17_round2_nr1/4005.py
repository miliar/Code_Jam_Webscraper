#include <iostream>
using namespace std;
int main() {
  int t, n, dist;
  cin >> t; 
  for (int i = 1; i <= t; ++i) {
    cin >> dist >> n;
    double d,s,t,max=0;
    for(int j=0;j<n;j++){
    	cin>>d>>s;
    	t=(dist-d)/s;
    	if(max<t){
    		max=t;
    	}
    }
    
    double ans=dist/max;
    printf("Case #%d: %6f\n",i,ans);
    //cout << "Case #" << i << ": " << ans <<  endl;
    
  }

  return 0;
}
 
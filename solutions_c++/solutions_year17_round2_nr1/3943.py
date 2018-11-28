#include <iostream>
#include <iomanip>
using namespace std;
int main() {
   int a,d,n,i,t,te,w;
   double t2,t1;
   cin>>t;
   for(a=1;a<=t;a++){
   	cin>>d>>n;
   	int k[n],s[n];
   	for (i=0;i<n;i++){
   	    cin>>k[i]>>s[i];
   	}
   	for (i = 1 ; i <= n - 1; i++) {
    w = i;
 
    while ( i > 0 && k[i] < k[i-1]) {
      te          = k[w];
      k[w]   = k[w-1];
      k[w-1] = te;
      te          = s[w];
      s[w]   = s[w-1];
      s[w-1] = te;
      w--;
    }
  }
   	t2=(double)(d-k[0])/s[0];
   	for (i=1;i<n;i++){
   	    t1=(double)(d-k[i])/s[i];
   	    if(t1>t2)
   	     t2=t1;
   	}
   	double q=(double)d/t2;
   	std::cout << std::fixed;
    std::cout << std::setprecision(6);
   	cout<<"Case #"<<a<<": "<<q<<endl;
   	
   }
	return 0;
}
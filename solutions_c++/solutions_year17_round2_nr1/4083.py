#include <bits/stdc++.h>
using namespace std;

int main() {

long long int T,i,min;

long double s;int k=1;

cin >> T;
while(T--)
{
    long long int D,N;
    cin >> D >> N;
    long double a[N];
    long double  b[N];
    
    for(i=0;i<N;i++)
    {
        cin >> a[i] >> b[i];
        
    }
    long double t=(D-a[0])/b[0];
    for(i=0;i<N;i++)
    {
       if((D-a[i])/b[i]>t)
       t=(D-a[i])/b[i];
    }
  
    s=D/t;
    cout << "Case #"<<k <<": "<< fixed<<setprecision(6) <<s<< endl ;
    k++;
    
}
	return 0;
}

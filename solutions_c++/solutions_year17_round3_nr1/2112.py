#include<bits/stdc++.h>
#define LL long long
#define pi 22.0/7.0
using namespace std;
struct pans{
double r , h ;
  double sol;
}pan[1005];


int cmp(pans a,pans b){
    return a.r >= b.r ;
}


int main()
{
  int t, n, m ,p ;

    double maxp[1005]={0.00};
    double maxp2[1005]={0.00};
  cin >> t;
  for (int k = 1; k <= t; ++k)
  {
    cin >> n >> p;

    for(int i=0; i<n; i++){
        cin>>pan[i].r>>pan[i].h;
        pan[i].sol = ( 2.0 * pan[i].r * pan[i].h  ) ;
    }

    sort(pan,pan+n,cmp);

    memset(maxp,0.00,sizeof(maxp));
    memset(maxp2,0.00,sizeof(maxp2));

    for(int i=0; i<n; i++){

        maxp2[1]=max(maxp[1], pan[i].sol + (  pan[i].r * pan[i].r ) );

        for(int j=2; j<=p; j++){

            if( maxp[j-1]>0.00001 ){
                maxp2[j]=max(maxp[j],maxp[j-1] +  pan[i].sol );
            }
        }

        for(int j=1; j<=p; j++){
                maxp[j]=maxp2[j];
                //cout<<i<<" "<<maxp[j]<<endl;
        }

    }

    double ans=maxp[p];
    ans = double( ans )*double(3.1415926535897932384626433);

    cout << "Case #" << k << ": " ;
    std::cout << std::fixed;
    std::cout << std::setprecision(12);
    cout<< ans << endl;
  }
  return 0;
}

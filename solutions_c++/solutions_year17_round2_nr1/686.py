#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int tests;
    cin>>tests;
    for (int test=0;test<tests;test++){
        int d,n;
        cin>>d>>n;
        double answer=1e300;
        for (int i=0;i<n;i++){
            int k,s;
            cin>>k>>s;
            double t = (d-k+0.0)/s;
            double sp=d/t;
            if (sp<answer) answer=sp;
        }

            cout<<"Case #"<<(test+1)<<": "<<std::setprecision(9)<<answer<<endl;

    }




}

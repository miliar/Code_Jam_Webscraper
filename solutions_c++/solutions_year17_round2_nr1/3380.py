#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int t, count  =1;
    
    cin>>t;
    while(count <= t)
    {
double  min = -1.0;
        double D, time;
        int N;
        cin>>D>>N;
        double H[N][2];
        for(int i=0;i<N;i++)
        {
            cin>>H[i][0]>>H[i][1];
            time = (D-H[i][0])/H[i][1];

            if(time>min)
                min =time;

       
        }
	//cout<<min<<"\n";
        double ans = D/min;

        cout<<"Case #"<<count<<": ";
	cout<<fixed;
	cout<<setprecision(6)<<ans<<"\n";

        count++;
    }

    return 0;
}


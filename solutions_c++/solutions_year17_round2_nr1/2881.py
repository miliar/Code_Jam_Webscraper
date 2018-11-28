#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.out","w",stdout);
    long long int T,x,y,n,d,c=1,i;
    double time;
    cin>>T;
    while(T--)
    {
        vector<double> vc;
        cin>>d>>n;
        for(i=0;i<n;i++)
        {
            cin>>x>>y;
            time=(double)(d-x)/y;
            vc.push_back(time);
        }
        time=*max_element(vc.begin(),vc.end());
        //cout<<time;
        time=(double)d/time;
        std::cout << std::fixed << std::showpoint;
        std::cout << std::setprecision(6);
        printf("Case #%d: ",c);
        cout<<time<<endl;
        c++;
    }
}


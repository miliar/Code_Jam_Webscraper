#include<bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    freopen("input.in", "r", stdin); 
    freopen("output.out", "w", stdout);
    cout<<setprecision(25)<<fixed;
    int T;
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        long long int K, S, D, N;
        cin>>D>>N;
        vector <pair<long long int, long long int> > horses;
        for(int i=0; i<N; i++)
        {
            cin>>K>>S;
            horses.push_back(make_pair(K,S));
        }
        sort(horses.begin(), horses.end());
        long double currSpeed = horses[0].second, currPos = horses[0].first;
        long double timespent= 0;
        for(int i=1; i<N; i++)
        {
            if(horses[i].second>=currSpeed)
                break;
            long double distance = (1.0*(horses[i].first-currPos));
            long double currtime=distance/(1.0*(currSpeed-horses[i].second));
            long double newPos = (1.0*(1.0*currPos+currtime*currSpeed));
            if(newPos>=D)
                break;
            currSpeed = horses[i].second;
            currPos = newPos; 
            timespent+=currtime;
        }
        timespent+=(D-currPos)/(1.0*currSpeed);
        long double ans = (D/(1.0*timespent));
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
    return 0;
}

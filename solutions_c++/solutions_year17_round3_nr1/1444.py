#include<bits/stdc++.h>

using namespace std;

#define pi 3.141593

int main()
{
    ios::sync_with_stdio(0);
    freopen("input.in", "r", stdin); 
    freopen("output.out", "w", stdout);
    int T;
    cin>>T;
    cout<<setprecision(15)<<fixed;
    for(int t=1; t<=T; t++)
    {
        int N, K;
        cin>>N>>K;
        long double Ri, Hi;
        vector <pair<long double, long double> > data;
        long double fans = 0;
        for(int i=0; i<N; i++)
        {
            cin>>Ri>>Hi;
            data.push_back(make_pair(Ri,Hi));
        }
        sort(data.begin(), data.end());
        for(int k = K-1; k<N; k++)
        {
            //first maximize area + height
            long double ans = 0;
            vector <pair<long double, int> > Area2;
            long double A;
            for(int i=0; i<=k; i++)
            {
                long double R = data[i].first, H = data[i].second;
                A = (2.0*pi*R*H);
                Area2.push_back(make_pair(A, i));
            }
            long double Area1 = (1.0*pi*data[k].first*data[k].first+ 2.0*pi*data[k].first*data[k].second);
            ans += Area1;
            int index = k;
            int count=0, idx=k;
            sort(Area2.begin(), Area2.end());
            while(count!=K-1)
            {
                if(Area2[idx].second!=index)
                {
                    ans += Area2[idx].first;
                    count++;
                }
                idx--;
            } 
            fans = max(ans, fans);
        }
        cout<<"Case #"<<t<<": "<<fans<<endl;
    }
    return 0;
}

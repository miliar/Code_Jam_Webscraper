#include <bits/stdc++.h>
typedef long long ll;
typedef long double ld;

using namespace std;

/*class cmp {
    public:
        bool operator()(pair<int , int> a ,pair<int , int> b){
            return a.second < b.second;
        }
};*/

int tc , n ;
ld d ;
pair <ld , ld> horses[1005];

bool solve (ld in){
    ld t , a = d/in;
    for(int i = 0 ; i<n ; i++){
        t = (d-horses[i].first) / horses[i].second ;
        if (t > a)
            return 0;
    }
    return 1;
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin>>tc;
    for(int i = 1 ; i<= tc ; i++){
        cin>>d>>n;
        for(int j = 0 ; j<n ; j++)
            cin>>horses[j].first>>horses[j].second;

        ld low = 0  , mid , high = 1e18;

        for(int i_i = 0 ; i_i < 1000 ; i_i++){
            mid = ( low + high )/2.0 ;

            if(solve(mid)==1)
                low = mid  ;
            else
                high = mid ;

            //cout<<low<<"\t"<<high<<endl;
        }

        cout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<mid<<endl;

    }

    return 0;
}

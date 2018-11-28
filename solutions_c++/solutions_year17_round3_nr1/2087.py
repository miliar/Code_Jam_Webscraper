#include<bits/stdc++.h>
#define PI 3.141592653589793238462643383279502884197169399375105820974944592307816406286
using namespace std;

int fact(int n){
    int ans=1;
    for(int cnt=1;cnt<=n;cnt++)
        ans*=cnt;
    return ans;
}

int main(){
    int T;
    cin>>T;
    cout<<fixed<<setprecision(9);
    for(int t=1;t<=T;t++){
        int n,k;
        cin>>n>>k;
        vector<pair<int,int> > arr(n);
        for(int cnt=0;cnt<n;cnt++){
            scanf("%d%d",&arr[cnt].first,&arr[cnt].second);
            arr[cnt].first*=-1;
            arr[cnt].second*=-1;
        }
        sort(arr.begin(),arr.end());
        double best=-1;
        int bound=fact(n);
        for(int tr=0;tr<bound;tr++){
            double ans=pow(arr[0].first,2)*PI;
            for(int cnt=0;cnt<k;cnt++)
                ans+=2*PI*arr[cnt].first*arr[cnt].second;
            if(best<ans)best=ans;
            next_permutation(arr.begin(),arr.end());
        }
        printf("Case #%d: ",t);
        cout<<best<<"\n";
    }
    return 0;
}

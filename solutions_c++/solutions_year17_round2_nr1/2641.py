#include<bits/stdc++.h>
using namespace std;
typedef pair<double,int> pdi;
const double eps=1e-9;
int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;cin>>T;
	for(int ks=1;ks<=T;ks++)
    {
        int D,N;cin>>D>>N;
        pdi tm[1010];
        for(int i=0;i<N;i++)
        {
            int K,S;cin>>K>>S;
            double time=(double)(D-K)/S;
            if(time<eps) continue;
            tm[i]={time,i};
        }
        sort(tm,tm+N);
        cout<<"Case #"<<ks<<": ";
        cout<<fixed<<setprecision(6)<<D/tm[N-1].first<<endl;
    }
	return 0;
}

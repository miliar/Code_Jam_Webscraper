#include <bits/stdc++.h>
using namespace std;
void fastInOut() {
	ios_base::sync_with_stdio(0);
	cin.tie(NULL), cout.tie(NULL);
}

int dx[] = { 0, 0, 1, -1, -1, -1, 1, 1 };
int dy[] = { 1, -1, 0, 0, -1, 1, -1, 1 };



int main()
{
   // fastInOut();
    freopen("A-large.in","rt",stdin);
    freopen("ans.txt","wt",stdout);
    int t;
    cin>>t;
    int cnt=1;
    while(t--)
    {
        double d,n,x,y;
        cin>>d>>n;
        double ma=0;
        for(int i=0;i<n;i++)
        {
            cin>>x>>y;
            double temp=(d-x)/y;
            if(temp>ma)
                ma=temp;
        }
        double ans=d/ma;
        cout<<"Case #"<<cnt<<": "<<fixed<<setprecision(6)<<ans<<endl;
        cnt++;
    }

    return 0;
}

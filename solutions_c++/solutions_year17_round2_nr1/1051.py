 #include <bits/stdc++.h>
using namespace std;

double t, n, d, x, y;

int main()
{
   freopen("r.txt","r",stdin);
   freopen("output.txt", "w", stdout);
   cin>>t;
   for(int i=0;i<t;i++){
    double ans=0, tm=0;
    cin>>d>>n;
    for(int j=0;j<n;j++){
        cin>>x>>y;
        if(x<d){
            double s=double((d-x)/y);
            //printf("%f,%f,%f   ", d-x, y, s);
            //cout<<s<<" ";
            tm=max(tm, s);
        }
    }
    ans=double(d/tm);
    printf("Case #%d: %f\n", i+1, ans);
   }


    return 0;
}

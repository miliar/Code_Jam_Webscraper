#include <bits/stdc++.h>
#define ll long long
using namespace std;
#define file_input freopen("in.txt","r",stdin)
#define file_output freopen("op.txt","w",stdout)
int main() {
    file_input;
    file_output;

    int test_case;
    cin>>test_case;
    for(int t=1;t<=test_case;t++){
        double d,ans;
        int n;
        cin>>d>>n;
        double ar[10005];
        for(int i=0;i<n;i++)
        {
            double a,b;
            cin>>a>>b;
            ar[i]=(d-a)/b;
        }
        sort(ar,ar+n);
        ans=d/ar[n-1];
        printf("Case #%d: %.6f\n",t,ans);
    }
	return 0;
}

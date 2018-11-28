#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin ("C:\\Users\\ADMIN\\Desktop\\folders\\CodeJam17\\input.txt");
    ofstream fout ("C:\\Users\\ADMIN\\Desktop\\folders\\CodeJam17\\sol.txt");

    int t,n,i,j;
    long long int d;
    long long int k[1010]={0};
    long long int s[1010]={0};
    long double mx=0.0,cmx;
    fin>>t;
    for(i=1;i<=t;i++){
        fin>>d>>n;
        mx=0.0;
        for(j=0;j<n;j++)
        {
            fin>>k[j]>>s[j];
            cmx = (d-k[j])/(s[j]*1.0);
            if(cmx>mx){
                mx=cmx;
            }
        }
        cmx = d/mx;
        fout<<"Case #"<<i<<": "<<fixed<<setprecision(6)<<cmx<<"\n";
    }
}

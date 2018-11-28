#include <bits/stdc++.h>
using namespace std;

#define x first
#define y second

int n,t,d;
pair <int,int> C[1010]; //poz, viteza

double timp,v,vit;

int main(){
    ifstream cin ("horses.in");
    ofstream cout ("horses.out");
    cin>>t;
    for (int w=1; w<=t; w++){
        timp=0;
        cin>>d>>n;
        for (int i=1; i<=n; i++) cin>>C[i].x>>C[i].y;
        sort(C+1,C+1+n);
        for (int i=1; i<=n; i++){
            double dist=d-C[i].x;
            double timp1=dist/C[i].y;
            timp=max(timp,timp1);
        }
        v=d/timp;
        cout<<fixed<<setprecision(6)<<"Case #"<<w<<": "<<v<<"\n";
    }
    return 0;
}

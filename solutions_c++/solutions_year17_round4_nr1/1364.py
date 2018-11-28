#include <bits/stdc++.h>
#define PB push_back
#define ll long long
using namespace std;

int tab3[101][101];
int tab4[101][101][101];

void tolt3() {
    for(int i=0;i<=100;i++) {
        for(int j=0;j<=100;j++) {
            int maxi=0;
            if(i>0 && maxi<(tab3[i-1][j]+((i-1+j*2)%3==0 ? 1 : 0))) {
                maxi=(tab3[i-1][j]+((i-1+j*2)%3==0 ? 1 : 0));
            }
            if(j>0 && maxi<(tab3[i][j-1]+((i+j*2-2)%3==0 ? 1 : 0))) {
                maxi=(tab3[i][j-1]+((i+j*2-2)%3==0 ? 1 : 0));
            }
            tab3[i][j]=maxi;
        }
    }
    return;
}

void tolt4() {
    for(int i=0;i<=100;i++) {
        for(int j=0;j<=100;j++) {
            for(int k=0;k<=100;k++) {
                int maxi=0;
                if(i>0 && maxi<(tab4[i-1][j][k]+((i-1+j*2+k*3)%4==0 ? 1 : 0))) {
                    maxi=(tab4[i-1][j][k]+((i-1+j*2+k*3)%4==0 ? 1 : 0));
                }
                if(j>0 && maxi<(tab4[i][j-1][k]+((i+j*2-2+k*3)%4==0 ? 1 : 0))) {
                    maxi=(tab4[i][j-1][k]+((i+j*2-2+k*3)%4==0 ? 1 : 0));
                }
                if(k>0 && maxi<(tab4[i][j][k-1]+((i+j*2+k*3-3)%4==0 ? 1 : 0))) {
                    maxi=(tab4[i][j][k-1]+((i+j*2+k*3-3)%4==0 ? 1 : 0));
                }
                tab4[i][j][k]=maxi;
            }
        }
    }
    return;
}

int main()
{
    freopen("be.txt","r",stdin);
    freopen("ki.txt","w",stdout);
    int t;
    cin>>t;
    tolt3();
    tolt4();
    for(int tc=1;tc<=t;tc++) {
        int n, p;
        cin>>n>>p;
        vector<int> t(4,0);
        for(int i=0;i<n;i++) {
            int z; cin>>z;
            t[z%p]++;
        }
        int sol=0;
        if(p==2) {
            sol=t[0]+((t[1]+1)/2);
        }
        if(p==3) {
            sol=t[0]+tab3[t[1]][t[2]];
        }
        if(p==4) {
            sol=t[0]+tab4[t[1]][t[2]][t[3]];
        }
        cout<<"Case #"<<tc<<": "<<sol<<endl;
    }
    return 0;
}

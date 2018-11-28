/* ahmed akef*/
#include <bits/stdc++.h>
#define CCC(x,a,b) cout << ((x)?(a):(b))
#define all(v)			((v).begin()), ((v).end())
#define sz(v)			((int)((v).size()))
#define fa(a,n)   for(int i = 0; i < n; i++){cin>>a[i];}  //fill array /* akef */
#define clr(v, d) memset(v, d, sizeof(v))
#define rep(i,n) for(int i = 0; i < n; i++)
#define MX_Z 1e6

using namespace std;

void setup();



int main()
{
    setup();
    freopen("B-large.in", "rt", stdin);
    freopen("B-large.out", "wt", stdout);


    int T;  cin>>T;
    string n;
    rep(Case,T){
        cin>>n;
        int z=sz(n);
        bool flag=false;
        for(int i = 0; i+1 < z; i++){
            if(flag){
                n[i]='9';
            }
            else if(n[i]>n[i+1]){
                char temp = n[i];
                int j;
                for( j=i; j>=0 && n[j]==temp ;j--)
                    n[j]='9';
                n[j+1]=temp-1;
                flag=true;
            }
        }
        if(flag)   n[z-1]='9';
        if(n[0]=='0'){
            n=n.substr(0,z-1);
            rep(k,z-1)  n[k]='9';
        }

        cout<<"Case #"<<Case+1<<": "<<n<<endl;
    }

    return 0;
}



void setup()
{
    ios_base::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
    freopen("test.in","rt",stdin);
    //freopen("s.out","wt",stdout);
#endif // ONLINE_JUDGE
}

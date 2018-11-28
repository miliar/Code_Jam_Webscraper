#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef  vector<unsigned long long > vull;

#define pb push_back
#define rep(i,n) for(int i=0;i<(n);i++)
#define Rep(i,a,b) for(int i=(a);i<(b);i++)
#define repr(i,n) for(int i=(n-1);i>=0;i--)
#define tc(t) while(t--)
#define  cout fout
#define cin fin



ofstream fout("lo.txt");
ifstream fin("li.txt");

int main()
{

	ull t,r,c,tmp,T;
	ll i,j;
	cin>>T;
	rep(t,T){
	    string s;
            cin >>r>>c;
            vector<string> a;
            tmp=r;
            tc(tmp)   {
                cin>>s;
                a.pb(s);
            }
            for(i=0;i<a.size();i++){
                for(j=0;j<a[i].size();j++){
                    if(j+1<c&&a[i][j+1]=='?'){
                        a[i][j+1]=a[i][j];
                    }
                }
            }
            for(i=0;i<a.size();i++){
                for(j=a[i].size()-1;j>=0;j--){
                  if(j-1>=0&&a[i][j-1]=='?'){
                        a[i][j-1]=a[i][j];
                    }
                }
            }
            for(i=0;i<a.size();i++){
                for(j=0;j<a[i].size();j++){
                    if(i+1<r&&a[i+1][j]=='?'){
                        a[i+1][j]=a[i][j];
                    }
                }
            }
            for(i=a.size()-1;i>=0;i--){
                   for(j=0;j<a[i].size();j++){
                   if(i-1>=0&&a[i-1][j]=='?'){
                        a[i-1][j]=a[i][j];
                    }
                }
            }
                cout<<"Case #"<<t+1<<":\n";
            for(i=0;i<a.size();i++){
                for(j=0;j<a[i].size();j++){
             cout<<a[i][j];
                    }
                    cout<<"\n";
                     }

            }

	}


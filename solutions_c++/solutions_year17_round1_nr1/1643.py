#include<bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;

	string s;
	unsigned long long int n,m=0,pre,val,p,r,c;

	for (int test = 1; test <= t; ++test)
	{
        string mat[30];
        cin>>r>>c;
        set< char > s;
        for(int i=0;i<r;i++){
                cin>>mat[i];

        }

        for(int i=0;i<r-1;i++){
            for(int j=0;j<c;j++){
                if( mat[i][j]!='?' && mat[i+1][j]=='?'){
                mat[i+1][j]=mat[i][j];
                }

            }
        }

        for(int i=r-1;i>0;i--){
            for(int j=0;j<c;j++){
                if( mat[i][j]!='?' && mat[i-1][j]=='?'){
                mat[i-1][j]=mat[i][j];
                }

            }
        }


        for(int i=0;i<c-1;i++){
            for(int j=0;j<r;j++){
                if( mat[j][i]!='?' && mat[j][i+1]=='?'){
                mat[j][i+1]=mat[j][i];
                }

            }
        }


        for(int i=c-1;i>0;i--){
            for(int j=0;j<r;j++){
                if( mat[j][i]!='?' && mat[j][i-1]=='?'){
                mat[j][i-1]=mat[j][i];
                }

            }
        }

		cout<<"Case #"<<test<<": "<<endl;
		        for(int i=0;i<r;i++){
                cout<<mat[i]<<endl;

        }
	}



	return 0;
}

#include<bits/stdc++.h>
#define LL long long
using namespace std;
int main() {
  int t, n, m;
  cin >> t;
  for (int k = 1; k <= t; ++k) {
    cin >> n >> m;
//    LL ans=0;
    string ans[40];
    for(int i=0; i<n; i++)cin>>ans[i];



    for(int i=0; i<n; i++){
        for(int j=0; j<m; j++){
            if(ans[i][j]=='?'&&j>0){
                ans[i][j]=ans[i][j-1];
            }
        }
    }
    for(int i=0; i<n; i++){
        for(int j=m-1; j>=0; j--){
            if(ans[i][j]=='?'&&j<m-1){
                ans[i][j]=ans[i][j+1];
            }
        }
    }
    int flag=1;
    while(flag==1)
    {
        flag=0;
        for(int i=0; i<n; i++){
            //cout<<i<<" ";
            if(ans[i][0]=='?'&&i>0&&ans[i-1][0]!='?'){
                flag=1;
                for(int j=0; j<m; j++){
                    ans[i][j]=ans[i-1][j];
                }
            }else if(ans[i][0]=='?'&&i<n-1&&ans[i+1][0]!='?'){
                flag=1;
                //cout<<"ok";
                for(int j=0; j<m; j++){
                    ans[i][j]=ans[i+1][j];
                }
            }
        }
    }


    cout << "Case #" << k << ":\n";
    for(int i=0; i<n; i++)
        cout<<ans[i]<<endl;
  }
  return 0;
}

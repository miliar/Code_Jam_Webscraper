#include <bits/stdc++.h>
using namespace std;

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for(int p=1;p<=t;p++){
        int n,m;
        cin >> n >> m;
        string str[n];
        int temp[26];
        for(int i=0;i<26;i++){
            temp[i]=0;
        }
        for(int i=0;i<n;i++){
            cin >> str[i];
        }
        char fill='?';
        int x=0;
        int y=0;
        int flag=0;
        while(x<n){
            while(y<m){
                while(y<m && str[x][y]=='?'){
                    y++;
                }
                if(y==m){
                    if(flag==1){
                        for(int i=x;i>=0;i--){
                            for(int j=y-1;j>=0;j--){
                                if(str[i][j]=='?'){
                                    str[i][j]=fill;
                                }
                            }
                        }
                    }
                }
                else{
                    fill=str[x][y];
                    temp[str[x][y]-'A']=1;
                    flag=1;
                    for(int i=x;i>=0;i--){
                        for(int j=y;j>=0;j--){
                            if(str[i][j]=='?'){
                                str[i][j]=fill;
                            }
                        }
                    }
                    y++;
                }
            }
            flag=0;
            y=0;
            x++;
        }
        if(str[n-1][m-1]=='?'){
            x=n-1;
            while(str[x][m-1]=='?'){
                x--;
            }
            for(int k=m-1;k>=0;k--){
                for(int i=x+1;i<n;i++){
                    str[i][k]=str[x][k];
                }
            }
        }
        cout << "Case #" << p << ":" << endl;
        for(int i=0;i<n;i++){
            cout << str[i] << endl;
        }
    }
    // your code goes here
    return 0;
}

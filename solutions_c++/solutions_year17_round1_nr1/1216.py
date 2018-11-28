// AUTHOR VINAYAK SINGLA
#include<bits/stdc++.h>
using namespace std;
#define ff first 
#define ss second 

string s[25];

int main()
{
    std::ios::sync_with_stdio(false);
    int a,q,b,c,n,r;
    cin>>q;
    for(int k=0;k<q;k++){
        cin>>r>>c;
        for(int i=0;i<r;i++){
            cin>>s[i];
        }
        for(int i=0;i<r;i++){
            a=0;
            for(int j=0;j<c;j++)
                if(s[i][j]!='?'){
                    a++;
                    break;
				}
            if(a!=0){
                s[0]=s[i];
                break;
            }    
        }
        for(int i=0;i<r;i++){
            a=0;
            for(int x=0;x<c;x++) if(s[i][x]!='?') a++;
            if(a!=0){
                for(int j=0;j<c;j++){
                    if(s[i][j]!='?'){
                        b=j-1;
                        while(b>-1&&s[i][b]=='?'){
                            s[i][b]=s[i][j];
                            b--;
                        }
                        b=j+1;
                        while(b<c && s[i][b]=='?'){
                            s[i][b]=s[i][j];
                            b++;
                        }
                    }
                }    
            }
            else{
                for(int j=0;j<c;j++){
                    s[i][j]=s[i-1][j];
                }
            }
        }
        cout<<"Case #"<<k+1<<":"<<endl;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                cout<<s[i][j];
            }
            cout<<endl;
        }
	}
    return 0;
}

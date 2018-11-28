#include <iostream>
#include <string>
using namespace std;

int main()
{
    char n[25][25],a='?';
    int t,r,c,count=0,k;
    cin>>t;
    for(int tc=1; tc<=t; tc++){
        cin>>r>>c;
        count=0;
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                cin>>n[i][j];
                if(n[i][j]!='?')
                    {count++;
                    a=n[i][j];}
            }
        }
        if(count==1){
            for(int i=0; i<r; i++){
                for(int j=0; j<c; j++){
                    n[i][j] = a;
                }
            }
        }
        else{
            for(int i=0; i<r; i++){
                a='?';
                k=0;
                for(int j=0; j<c; j++){
                    if(n[i][j]!='?'){
                        a = n[i][j];
                        if(k>0){
                           for(int ind=1;ind<=k; ind++){
                               n[i][j-ind] = a;
                               //cout<<a<<endl;
                           } 
                           k=0;
                        }
                    }
                    else if(n[i][j]=='?'){
                        if(a=='?'){
                            k++;
                            continue;
                        }else{
                            n[i][j] = a;
                            //cout<<a<<endl;
                        }
                    }
                }
            }
            
            for(int j=0; j<c; j++){
                a='?';
                k=0;
                for(int i=0; i<r; i++){
                    if(n[i][j]!='?'){
                        a = n[i][j];
                        if(k>0){
                           for(int ind=1;ind<=k; ind++){
                               n[i-ind][j] = a;
                               //cout<<a<<endl;
                           } 
                           k=0;
                        }
                    }
                    else if(n[i][j]=='?'){
                        if(a=='?'){
                            k++;
                            continue;
                        }else{
                            n[i][j] = a;
                            //cout<<a<<endl;
                        }
                    }
                }
            }
        
        }
        
        
        cout<<"Case #"<<tc<<": "<<endl;
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                cout<<n[i][j];
            }
            cout<<endl;
        }
    }
    return 0;
}

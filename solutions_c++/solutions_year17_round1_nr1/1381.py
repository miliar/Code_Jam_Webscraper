#include<bits/stdc++.h>
#include <string>

using namespace std;
#include <sstream>

template <typename T>
std::string NumberToString ( T Number ){std::ostringstream ss;ss << Number;return ss.str();}
typedef unsigned long long ll;
char arr[26][26];

int main()
{
    freopen("in.txt.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int tt=0;
    while(t--){
        cout<<"Case #"<<++tt<<": ";
        int r,c;
        cin>>r>>c;
        map<int,int> mp;
        for(int i=0;i<r;i++){
            int is=0;
            for(int j=0;j<c;j++){
                    arr[i][j]='?';
                cin>>arr[i][j];
                if(arr[i][j]!='?')
                    is=1;
            }
            if(is)
            mp[i]=1;
        }
        for(int i=0;i<r;i++){
            if(mp.find(i)!=mp.end())
            {
                int lstfnd=0;
                for(int j=0;j<c;j++){
                    if(arr[i][j]!='?'){
                        lstfnd = j;
                        int k=j-1;
                        while(k>=0){
                            if (arr[i][k]!='?')break;
                            arr[i][k]=arr[i][j];
                            k--;
                        }
                    }
                }
                lstfnd++;
                while(lstfnd<c){
                    arr[i][lstfnd]=arr[i][lstfnd-1];
                    lstfnd++;
                }

            }
        }
        if(mp.size()==0){
            for(int i=0;i<r;i++)
                for(int j=0;j<c;j++)
                    arr[i][j]='A';
        }
        else{
            int fst = mp.begin()->first;
            for(int i=0;i<fst;i++)
            {
                for(int j=0;j<c;j++)
                    arr[i][j]=arr[fst][j];
            }
            for(int i=fst+1;i<r;i++)
            {
                if(arr[i][0]=='?')
                    for(int j=0;j<c;j++)
                        arr[i][j]=arr[i-1][j];
            }
        }
        cout<<endl;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++)
                cout<<arr[i][j];
                cout<<endl;
        }
    }
}
